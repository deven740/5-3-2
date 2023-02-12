from player import Player
from typing import Dict

from connection import Connection
from deck import Deck

connect = Connection()


class Game:
    players: Dict[str, Player] = {}
    trump_suit: str | None = None
    current_player: str | None = None
    starting_suit: str | None = None
    round_winner: str | None = None
    current_round: Dict[str, str] = {}
    rounds_completed: int = 0

    async def add_players(self, player_name, ws):
        player = Player(player_name=player_name, ws=ws)

        if self._check_player_count() == 3:
            return {"type": "error", "msg": "Room is full"}

        self.players[player.player_name] = player

        await connect.send_message(
            ws, {"type": "success", "msg": "You have joined the room successfully"}
        )

        if self._check_player_count() == 3:
            players = self.players
            p1, p2, p3 = players.values()

            p1.next_turn = p2.player_name
            p2.next_turn = p3.player_name
            p3.next_turn = p1.player_name

            await self.start_game()

    def _check_player_count(self):
        return len(self.players)

    async def start_game(self):
        players = self.players

        all_cards = Deck().distribute_cards()

        for player_name, player_cards, tricks_required in zip(
            players, all_cards, [5, 3, 2]
        ):
            player = players[player_name]
            if player.tricks_required == 0:

                player.tricks_required = tricks_required

            if player.tricks_required == 5:
                self.current_player = player.player_name

            player.cards = Deck.create_cards_dict(player_cards)

        await self.distribute_cards(start_index=0)

    async def set_trump_suit(self, player_name, data):
        if self.not_valid_turn(player_name):
            player = self.players[player_name]
            message = {"type": "error", "message": "It isn't your turn"}
            await connect.send_message(player.ws, message)
            return
        self.trump_suit = data["played_card"][1]
        await self.distribute_cards(start_index=5)

    async def play(self, player_name, data):
        player = self.players[player_name]
        played_card = data["played_card"]

        current_round = self.current_round

        if len(current_round) == 0:
            self.starting_suit = played_card[1]

        if self.not_valid_turn(player_name):
            message = {"type": "error", "message": "It isn't your turn"}
            await connect.send_message(player.ws, message)
            return

        if self.not_valid_card(player_name, played_card):
            message = {"type": "error", "message": "You cannot play this card"}
            await connect.send_message(player.ws, message)
            return

        self.current_player = player.next_turn

        current_round[player_name] = played_card

        self.pop_card(player_name, played_card)

        await self.notify_players(player_name, played_card)

        if len(current_round) == 3:

            self.decide_winner()
            self.rounds_completed += 1
            self.check_score()

            if self.rounds_completed == 10:
                await self.reset_game()

    def pop_card(self, player_name, played_card):
        player = self.players[player_name]
        player.cards[played_card[1]].remove(played_card[0])

        if len(player.cards[played_card[1]]) == 0:
            player.cards.pop(played_card[1])

    async def reset_game(self):
        self.trump_suit = None
        self.rounds_completed = 0
        self.update_tricks_required()
        await self.start_game()

    def decide_winner(self):
        max_score = 0
        deck = Deck()

        for player in self.current_round:
            card = self.current_round[player]
            card_score = deck.deck[card]["score"]
            if card[1] == self.starting_suit:
                card_score += 50
            if card[1] == self.trump_suit:
                card_score += 100
            if card_score > max_score:
                max_score = max(max_score, card_score)
                self.current_player = player

        player = self.players[self.current_player]

        player.tricks_won += 1
        self.current_round = {}

    def already_played(self, player_name):
        return player_name in self.current_round

    def not_valid_turn(self, player_name):
        player = self.players[player_name]
        return not player.player_name == self.current_player

    def not_valid_card(self, player_name, played_card):
        player = self.players[player_name]
        if self.starting_suit in player.cards and played_card[1] != self.starting_suit:
            return True
        return False

    async def distribute_cards(self, start_index):
        players = self.players
        for player in players.values():
            cards_list = Deck.create_cards_list(player.cards)
            message = {
                "type": "set_trump",
                "cards": cards_list[start_index : start_index + 5],
            }
            await connect.send_message(player.ws, message)

    async def notify_players(self, player_name, played_card):
        players = self.players

        for player in players.values():
            message = {
                "type": "play",
                "player_name": player_name,
                "played_card": played_card,
            }
            await connect.send_message(player.ws, message)

    def check_score(self):
        players = self.players

        for name in players:
            player = players[name]

    def update_tricks_required(self):
        players = self.players

        for player in players.values():
            if player.tricks_required == 5:
                player.tricks_required = 2
            elif player.tricks_required == 3:
                player.tricks_required = 5
            else:
                player.tricks_required = 3
