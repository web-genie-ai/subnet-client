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
    html: str = pydantic.Field(
        "",
        title="HTML",
        description="The HTML received from miners."
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
    html: str = pydantic.Field(
        "",
        title="HTML",
        description="The HTML received from miners."
    )