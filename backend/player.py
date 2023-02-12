from pydantic import BaseModel
from typing import Dict, Union, Any


class Player(BaseModel):
    player_name: str
    cards: Dict[str, set] = {}
    tricks_required: int = 0
    tricks_won: int = 0
    next_turn: Union[None, str] = None
    ws: Any
