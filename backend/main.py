from typing import Union, List

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from game import Player, Game

app = FastAPI()


class Rooms:
    def __init__(self):
        self.rooms = {}

    async def connect(self, websocket: WebSocket, room_code: str):

        if len(self.rooms.get(room_code, [])) == 3:
            raise RuntimeError('Room is full')

        await websocket.accept()

        player = Player(f'test', websocket) 

        if room_code in self.rooms:
            self.rooms[room_code]['players'].append(player)

            if len(self.rooms[room_code]['players']) == 3:
                self.rooms[room_code]['game'] = Game()
                print(self.rooms[room_code]['game'].deck)
                

        else:
            self.rooms[room_code] =  {'game': None, 'players': [player]}

    def disconnect(self, websocket: WebSocket, room_code:str):
        self.rooms[room_code].remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str, room_code: str):
        for player in self.rooms[room_code]['players']:
            if self.rooms[room_code]['game']:
                game = self.rooms[room_code]['game']
                game = 'game started'
            else:
                game = 'game not started'
            await player.websocket.send_text({game})


rooms = Rooms()


@app.websocket("/ws/{room_code}")
async def websocket_endpoint(websocket: WebSocket, room_code: str):
    await rooms.connect(websocket, room_code)
    try:
        while True:
            data = await websocket.receive_text()
            await rooms.broadcast(data, room_code)
    except WebSocketDisconnect:
        rooms.disconnect(websocket, room_code)
        await rooms.broadcast(f"Client #{room_code} left the chat")