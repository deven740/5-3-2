# Simple 5-3-2 card game using Websockets

A traditional Indian Card game played between 3 players. The objective is for each player to win the specified number of tricks.

**Deck**

1. A Deck of 30 cards is used, all the cards between 2 - 6 are removed, and 7 of SPADES and HEARTS are kept in the deck.
2. The cards in each suit are ranked in decreasing order from A-K-Q-J-10-9-8-7.

**Game Rules**

1. The leading player who selects the trump must complete 5 tricks.
2. The player on their left must complete 3 tricks.
3. The last player to the right of the dealer must complete 2 tricks.
4. First 15 cards are dealt evenly among the players, the leading player must select the Trump card from the 5 cards dealt to him.
5. Players must always try to follow the suit set by the first player in a trick. Only if they don’t have that particular suit in hand can they play another card from a different suit.
6. The player who had the highest-ranking card of a particular suit in a given trick wins.
7. If there are multiple trump cards played, then the highest-ranking trump card wins.
8. A player who fulfills their contract and exceeds the number can only exchange a card with the player who did not fulfill their contract.
