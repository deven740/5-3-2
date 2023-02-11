from fastapi import FastAPI, Response, HTTPException
from uuid import uuid4
from schemas import RoomResponseModel, RoomSchema
from room import Room


app = FastAPI()

room = Room()


@app.get("/create_room", response_model=RoomResponseModel)
def create_room():
    room_id = uuid4()
    room.create_room(room_id=room_id)
    return {"room_id": room_id}


@app.post("/join_room")
def join_room(r: RoomSchema):
    if room.is_room_created(r.room_id):
        return Response(status_code=200)
    raise HTTPException(status_code=404, detail="Room not found")
