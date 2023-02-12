from random import shuffle


class Deck:

    suits = "H D C S".split()
    ranks = "7 8 9 0 J Q K A".split()

    def __init__(self) -> None:
        self.deck = self.create_deck()

    def create_deck(self):
        full_deck = {}

        for suit in self.suits:
            for score, rank in enumerate(self.ranks, 7):
                full_deck[f"{rank}{suit}"] = {"score": score}

        for key in ["7D", "7C"]:
            full_deck.pop(key)

        return full_deck

    def shuffle_deck(self):
        cards = list(self.deck.keys())
        shuffle(cards)
        return cards

    def distribute_cards(self):
        cards = self.shuffle_deck()
        n = len(cards) // 3
        return [cards[:n], cards[n : 2 * n], cards[2 * n :]]

    @staticmethod
    def create_cards_dict(cards_list):
        cards = {}
        for card in cards_list:
            cards[card[1]] = cards.get(card[1], set()).union({card[0]})
        return cards

    @staticmethod
    def create_cards_list(cards_dict):
        return [card + suit for suit, cards in cards_dict.items() for card in cards]
