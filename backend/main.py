from typing import Union, List

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from game import Player, Game, Deck
import json
import uuid

app = FastAPI()


class Rooms:
    def __init__(self):
        self.rooms = {}

    async def connect(self, websocket: WebSocket, room_code: str, player_name: str):

        if len(self.rooms.get(room_code, [])) == 3:
            raise RuntimeError('Room is full')

        await websocket.accept()

        player = Player(player_name, websocket)
        # print(player.name) 

        if room_code in self.rooms:
            self.rooms[room_code]['players'].append(player)

            if len(self.rooms[room_code]['players']) == 3:
                self.rooms[room_code]['game'] = Game()
                deck = Deck.shuffle_deck(self.rooms[room_code]['game'].deck)

                n = len(deck) // 3
                player_cards = [deck[:n], deck[n:2*n], deck[2*n:]]
                for player, cards in zip(self.rooms[room_code]['players'], player_cards):
                    # player.cards.update(card)
                    for card in cards:
                        print(card)
                        if card[1] in player.cards:
                            player.cards[card[1]].add(card[0])
                        else:
                            player.cards[card[1]] = {card[0]}

                for player in self.rooms[room_code]['players']:
                    cards_list = []
                    for suit in player.cards.keys():
                        for rank in player.cards[suit]:
                            cards_list.append(rank + suit)
                    print('cards_list', cards_list)

                    await self.send_cards(cards_list, player.websocket)
                    cards_list = []
                    # self.
        else:
            self.rooms[room_code] =  {'game': None, 'players': [player]}

    def disconnect(self, websocket: WebSocket, room_code:str):
        self.rooms[room_code].remove(websocket)

    async def send_cards(self, cards: List, websocket: WebSocket):
        data = {
            "type": "init",
            "cards": cards 
        }
        # print(data)
        await websocket.send_text(json.dumps(data))

    async def send_personal_message(self, cards: str, websocket: WebSocket):
        await websocket.send_text(cards)

    async def broadcast(self, message: dict, room_code: str, player_name: str):
        # print(player_name)
        for player in self.rooms[room_code]['players']:
            if self.rooms[room_code]['game']:
                game = self.rooms[room_code]['game']

                event = {
                    "type": "play",
                    "player": player_name,
                    "cardPlayed": message['player_card']
                }
                await player.websocket.send_text(json.dumps(event))
            else:
                game = 'game not started'
            # await player.websocket.send_text({game})

    async def already_played(self, websocket, data, room_code, player_name):
        game = self.rooms[room_code]['game']  
        if player_name in game.current_round:
            print(f'{player_name} has already played')
            event = {
                        "type": "error",
                        "error": "It isn't your turn"
                    }
            await websocket.send_text(json.dumps(event))
        else:
            if len(game.current_round) == 0:
                game.round_start_suit = data['player_card'][1]
                print(game.round_start_suit)
            for player in self.rooms[room_code]['players']:
                if player.name == player_name:
                    if game.round_start_suit in player.cards and data['player_card'][1] != game.round_start_suit:
                        event = {
                            "type": "error",
                            "error": "You cannot play this card"
                        }
                        await websocket.send_text(json.dumps(event))
                        return

                    game.current_round[player_name] = data['player_card']
                    player.cards[data['player_card'][1]].remove(data['player_card'][0])
                    if len(player.cards[data['player_card'][1]]) == 0:
                        player.cards.pop(data['player_card'][1])

                    # print(player.cards)
            if len(game.current_round) == 3:
                round_winner = game.check_winner()
                game.current_round.clear()
                pass
            await rooms.broadcast(data, room_code, player_name) 


        


rooms = Rooms()


@app.websocket("/ws/{room_code}")
async def websocket_endpoint(websocket: WebSocket, room_code: str, player_name: str):
    await rooms.connect(websocket, room_code, player_name)
    try:
        while True:
            data = await websocket.receive_text()
            data = json.loads(data)
            await rooms.already_played(websocket, data, room_code, player_name)
            # await rooms.broadcast(data, room_code, player_name)
    except WebSocketDisconnect:
        rooms.disconnect(websocket, room_code)
        await rooms.broadcast(f"Client #{room_code} left the chat")