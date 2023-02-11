from pydantic import BaseModel
from uuid import uuid4, UUID


class RoomResponseModel(BaseModel):
    room_id: UUID


class RoomSchema(BaseModel):
    room_id: UUID
