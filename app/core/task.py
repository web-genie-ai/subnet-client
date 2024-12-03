from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional
from pydantic import BaseModel
from app.core.solution import Solution

class Task(BaseModel):
    query: Optional[str] = None
    img_data: Optional[str] = None
    timeout: float = 50
    original_html: Optional[str] = None
    reward_models: List[tuple] = [
        ("gpt", 0.5),
        ("speed", 0.5),
    ]
    penalty_models: List[tuple] = [
        ("is_valid", 2),
    ]
    reward_weight: float = 0.8
    penalty_weight: float = 0.2