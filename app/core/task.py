from typing import List
from pydantic import BaseModel

class Task(BaseModel):
    query: str
    
    timeout: float = 50

    reward_models: List[tuple] = [
        ("gpt", 0.5),
        ("speed", 0.5),
    ]

    penalty_models: List[tuple] = [
        ("penalty", 0.5),
    ]

    reward_weight: float = 0.8
    penalty_weight: float = 0.2
