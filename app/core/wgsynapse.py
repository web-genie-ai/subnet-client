import pydantic
from typing import Union, Any
import bittensor as bt
from app.core.solution import Solution

class WebgenieTextSynapse(bt.Synapse):
    """
    A protocol for the webgenie text task.
    """
    prompt: str = pydantic.Field(
        "",
        title="Prompt",
        description="The prompt to be sent to miners."
    )

    solution: Union[Solution, None] = pydantic.Field(
        None,
        title="Solution",
        description="A solution received from miners."
    )

class WebgenieImageSynapse(bt.Synapse):
    """
    A protocol for the webgenie image task.
    """
    base64_image: str = pydantic.Field(
        "",
        title="Base64 Image",
        description="The base64 image to be sent to miners."
    )

    solution: Union[Solution, None] = pydantic.Field(
        None,
        title="Solution",
        description="A solution received from miners."
    )

