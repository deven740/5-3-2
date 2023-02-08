from random import shuffle

class Deck:

    suits = 'H D C S'.split()
    ranks = '7 8 9 10 J Q K A'.split()

    def __init__(self) -> None:
        pass

    @classmethod
    def create_deck(cls):
        full_deck = {}

        for suit in cls.suits:
            for score, rank in enumerate(cls.ranks, 7):
                full_deck[f'{rank}{suit}'] = {'score': score}

        return full_deck
    

    def _shuffle(full_deck):
        return full_deck
        return shuffle(list(full_deck))



class Player:
    def __init__(self, name, websocket) -> None:
        self.name = name
        self.websocket = websocket
        self.cards = set()

class Game:
    def __init__(self) -> None:
        self.deck = Deck.create_deck()._shuffle()
        

    
    def start(self):
        pass


        

        