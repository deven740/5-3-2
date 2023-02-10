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
    current_round = {}
    is_trump_set = None
    round_start_suit = None
    
    def __init__(self) -> None:
        pass

    @classmethod
    def shuffle_deck(cls):
        return Deck.shuffle_deck(cls.deck)

    @classmethod  
    def check_winner(cls):
        round_winner = None
        max_score = 0
        for player in cls.current_round:
            if cls.deck[cls.current_round[player]]['score'] > max_score:
                max_score = max(max_score, cls.deck[cls.current_round[player]]['score'])
                round_winner = player
            print(player, cls.deck[cls.current_round[player]], cls.current_round[player], max_score)

        return round_winner
        

    
    def start(self):
        pass


        

        