from uuid import UUID
from pydantic import BaseModel
from typing import Dict


class Room(BaseModel):
    rooms: Dict = {}

    def create_room(self, room_id: UUID):
        self.rooms[room_id] = {}

    def is_room_created(self, room_id: UUID):
        return room_id in self.rooms
