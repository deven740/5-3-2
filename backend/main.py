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
        print(player.name) 

        if room_code in self.rooms:
            self.rooms[room_code]['players'].append(player)

            if len(self.rooms[room_code]['players']) == 3:
                self.rooms[room_code]['game'] = Game()
                deck = Deck.shuffle_deck(self.rooms[room_code]['game'].deck)

                n = len(deck) // 3
                split_cards = [deck[:n], deck[n:2*n], deck[2*n:]]
                for player, split_card in zip(self.rooms[room_code]['players'], split_cards):
                    player.cards.update(split_card)

                for player in self.rooms[room_code]['players']:
                    print(player.cards)
                    await self.send_cards(player.cards, player.websocket)
                    # self.
        else:
            self.rooms[room_code] =  {'game': None, 'players': [player]}

    def disconnect(self, websocket: WebSocket, room_code:str):
        self.rooms[room_code].remove(websocket)

    async def send_cards(self, cards: List, websocket: WebSocket):
        data = {
            "event": "init",
            "cards": list(cards) 
        }
        print(data)
        await websocket.send_text(json.dumps(data))

    async def send_personal_message(self, cards: str, websocket: WebSocket):
        await websocket.send_text(cards)

    async def broadcast(self, message: dict, room_code: str, player_name: str):
        print(player_name)
        for player in self.rooms[room_code]['players']:
            if self.rooms[room_code]['game']:
                game = self.rooms[room_code]['game']
                game.current_round.add(message['player_card'])
                print(len(game.current_round))
                # print(type(message), message)
                event = {
                    "type": "play",
                    "player": player_name,
                    "cardPlayer": message['player_card']
                }
                await player.websocket.send_text(json.dumps(event))
            else:
                game = 'game not started'
            # await player.websocket.send_text({game})


rooms = Rooms()


@app.websocket("/ws/{room_code}")
async def websocket_endpoint(websocket: WebSocket, room_code: str, player_name: str):
    await rooms.connect(websocket, room_code, player_name)
    try:
        while True:
            data = await websocket.receive_text()
            data = json.loads(data)
            await rooms.broadcast(data, room_code, player_name)
    except WebSocketDisconnect:
        rooms.disconnect(websocket, room_code)
        await rooms.broadcast(f"Client #{room_code} left the chat")