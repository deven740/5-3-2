from uuid import UUID
from pydantic import BaseModel
from typing import Dict
from fastapi import WebSocket
from game import Game
from player import Player


class Room(BaseModel):
    rooms: Dict[str, dict] = {}

    def create_room(self, room_id: UUID):
        self.rooms[room_id] = {"game": Game()}

    def is_room_created(self, room_id: UUID):
        return room_id in self.rooms

    # async def add_to_game(self, player_name: str, room_id: UUID, ws):
    #     player = Player(player_name=player_name, ws=ws)
    #     game = self.rooms[room_id]["game"]
    #     await game.add_players(player, ws)

    def get_room(self, room_id: UUID):
        return self.rooms[room_id]["game"]
