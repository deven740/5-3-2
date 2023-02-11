from fastapi import FastAPI, Response, HTTPException, WebSocket
from uuid import UUID, uuid4
from room import Room


app = FastAPI()

room = Room()


@app.get("/create_room")
def create_room():
    room_id = uuid4()
    room.create_room(room_id=room_id)
    return {"room_id": room_id}


@app.post("/join_room")
def join_room(room_id: UUID):
    print(room, room_id)
    if room.is_room_created(room_id):
        return Response(status_code=200)
    raise HTTPException(status_code=404, detail="Room not found")
