from random import shuffle

class Deck:

    suits = 'H D C S'.split()
    ranks = '7 8 9 0 J Q K A'.split()

    def __init__(self) -> None:
        pass

    @classmethod
    def create_deck(cls):
        full_deck = {}

        for suit in cls.suits:
            for score, rank in enumerate(cls.ranks, 7):
                full_deck[f'{rank}{suit}'] = {'score': score}

        [full_deck.pop(key) for key in ['7D', '7C']]

        return full_deck
    

    @staticmethod
    def shuffle_deck(deck):
        deck_keys_list = list(deck.keys())
        shuffle(deck_keys_list)
        return deck_keys_list
        # shuffled_cards = (shuffle(list(deck.keys())))
        # shushuffle(list(deck.keys()))
    

class Player:
    def __init__(self, name, websocket, next=None) -> None:
        self.name = name
        self.websocket = websocket
        self.cards = {}
        self.next = None
        self.tricks_required = None

class Game:
    deck = Deck.create_deck()
    current_round = {}
    trump_suit = None
    round_start_suit = None
    last_round_winner = None
    current_player = None
    
    def __init__(self) -> None:
        pass

    @classmethod
    def shuffle_deck(cls):
        return Deck.shuffle_deck(cls.deck)
  
    def set_round_winner(self):
        max_score = 0
        for player in self.current_round:
            card = self.current_round[player]
            card_score = self.deck[card]['score']
            if card[1] == self.round_start_suit:
                card_score += 50
            if card[1] == self.trump_suit:
                card_score += 100
            if card_score > max_score:
                max_score = max(max_score, card_score)
                self.last_round_winner = player
            # print(player, self.deck[self.current_round[player]], self.current_round[player], max_score)

        return self.last_round_winner
    
    def set_trump_card(self, card):
        self.set_trump_card = card
        

    
    def start(self):
        pass


        

        