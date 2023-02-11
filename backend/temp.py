# class Player:
#     def __init__(self, name, next = None) -> None:
#         self.name = name
#         self.next = None

# temo_list = []

# p1 = Player('p1')

# temo_list.append(p1)

# p2 = Player('p2')

# temo_list[len(temo_list) - 1].next = p2 0

# temo_list.append(p2)

# p3 = Player('p3')
# temo_list[len(temo_list) - 1].next = p3 1

# temo_list.append(p3)
# temo_list[len(temo_list) - 3].next = p3

# p1.next = p2
# p2.next = p3
# p3.next = p1

# pl = p1

# count = 0

# while count < 50:
#     print(pl.name)
#     pl = pl.next
#     count += 1

# To do 
# 1) Setting Trump
# 2) Rotate tricks_required

import itertools

colors = itertools.cycle(["red", "green", "blue"])
for i in range(10):
    print(next(colors))

class temp:
    def __init__(self, name) -> None:
        self.name = name

t = temp('t')

test = {}

test[t] = [1]

print(test)

rooms = {
    "room1" : {
        "game" : {
            "current_round" : {},
            "trump_card" : None,
            "round_start_suit" : None,
            "current_player" : "player1",
            "last_round_winner": "player3",
            "game_cards" : [], 
            "players": [
                    {
                        "player1" : {
                            "websocket": "websocket",
                            "name" : "name",
                            "cards" : {
                                "H" : {"7", "8", "9"},
                                "S" : {"7", "8", "9"},
                                "D" : {"7", "8", "9"},
                                "J" : {"7", "8", "9"}
                            },
                            "tricks_required": 5,
                            "tricks_completed": 0,
                            "next" : "player2"
                        }
                    },
                    {
                        "player2" : {
                            "websocket": "websocket",
                            "name" : "name",
                            "cards" : {
                                "H" : {"7", "8", "9"},
                                "S" : {"7", "8", "9"},
                                "D" : {"7", "8", "9"},
                                "J" : {"7", "8", "9"}
                            },
                            "tricks_required": 3,
                            "tricks_completed": 0,
                            "next" : "player3"
                        }
                    },
                    {
                        "player3" : {
                            "websocket": "websocket",
                            "name" : "name",
                            "cards" : {
                                "H" : {"7", "8", "9"},
                                "S" : {"7", "8", "9"},
                                "D" : {"7", "8", "9"},
                                "J" : {"7", "8", "9"}
                            },
                            "tricks_required": 2,
                            "tricks_completed": 0,
                            "next" : "player1"
                        }
                    },
                ]
            }
    },
    "room2" : {
        "game"
    }
}


        
        