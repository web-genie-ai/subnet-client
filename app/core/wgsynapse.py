import pydantic
from typing import Union, Any
import bittensor as bt
from app.core.task import Task
from app.core.solution import Solution

class WGSynapse(bt.Synapse):
    """
    A protocol for the WebGenieAI.
    """
    task: Union[Task, None] = pydantic.Field(
        None,
        title="Task",
        description="A task to be sent to miners."
    )
    solution: Union[Solution, None] = pydantic.Field(
        None,
        title="Solution",
        description="A solution received from miners."
    )
    completion: str = pydantic.Field(
        "",
        title="Completion",
        description="The completion response from miners."
    )
    def deserialize(self) -> Union[Any, None]:
        return self