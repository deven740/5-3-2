from fastapi import WebSocket
from typing import Dict
import json


class Connection:
    def __init__(self) -> None:
        pass

    async def connect(self, ws: WebSocket):
        await ws.accept()

    async def send_message(self, ws: WebSocket, message: Dict[str, str]):
        await ws.send_json(message)
