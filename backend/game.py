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
    def __init__(self, name, websocket) -> None:
        self.name = name
        self.websocket = websocket
        self.cards = {}

class Game:
    deck = Deck.create_deck()
    current_round = set()
    
    def __init__(self) -> None:
        pass

    @classmethod
    def shuffle_deck(cls):
        return Deck.shuffle_deck(cls.deck)
        

    
    def start(self):
        pass


        

        