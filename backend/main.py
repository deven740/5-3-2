from fastapi import FastAPI, Response, HTTPException, WebSocket, WebSocketDisconnect
from uuid import UUID, uuid4
from room import Room
from connection import Connection
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

room = Room()
connection = Connection()


@app.get("/create_room")
def create_room():
    # room_id = uuid4()
    room_id = "test"
    room.create_room(room_id=room_id)
    return {"room_id": room_id}


@app.post("/join_room")
def join_room(room_id: UUID):
    print(room, room_id)
    if room.is_room_created(room_id):
        return Response(status_code=200)
    raise HTTPException(status_code=404, detail="Room not found")


@app.websocket("/ws")
async def connect(ws: WebSocket, room_id: str, player_name: str):
    await connection.connect(ws)
    game = room.get_room(room_id)
    await game.add_players(player_name, ws)

    try:
        while True:
            data = await ws.receive_text()
            data = json.loads(data)
            if not game.trump_suit:
                await game.set_trump_suit(player_name, data)
            else:
                await game.play(player_name, data)
    except WebSocketDisconnect:
        pass
