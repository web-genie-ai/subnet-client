# The MIT License (MIT)
# Copyright © 2023 Yuma Rao
# Copyright © 2023 Dominique Hayes

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import pydantic
import json
from typing import AsyncIterator, Union, Any
from starlette.responses import StreamingResponse

import bittensor as bt

from app.core.solution import Solution
from app.core.task import Task

class BtCopilotSynapse(bt.StreamingSynapse):
    """
    A protocol for the BtCopilot.
    """

    task: Union[Task, None] = pydantic.Field(
        None, title="Task", description="A task to be sent to miners."
    )

    solution: Union[Solution, None] = pydantic.Field(
        None, title="Solution", description="A solution received from miners."
    )

    completion: str = pydantic.Field(
        "", title="Completion", description="The completion response from miners."
    )

    async def process_streaming_response(
        self, response: StreamingResponse
    ) -> AsyncIterator[str]:
        """
        Processes a streaming response from a miner.
        """
        if self.completion is None:
            self.completion = ""
        async for chunk in response.content.iter_any():
            tokens = chunk.decode("utf-8")

            for token in tokens:
                if token:
                    self.completion += token
            yield tokens

    def deserialize(self) -> Union[Any, None]:
        """
        Deserializes the response.
        """
        try:
            json_response = json.loads(self.completion)
            css = None
            html = None
            for key, value in json_response.items():
                if key.lower() == "css":
                    css = value
                elif key.lower() == "html":
                    html = value

            if css is None and html is None:
                bt.logging.error(f"Invalid response: {json_response}")
                return None

            css = str(css)
            html = str(html)

            process_time = self.dendrite.process_time
            bt.logging.debug(f"css: {css}, html: {html}, process_time: {process_time}")
            self.solution = Solution(
                css=css, html=html, process_time=process_time, miner_uid=0
            )
            return self
        except Exception as e:
            bt.logging.error(f"Failed to parse completion: {e}")
            return None

    def extract_response_json(self, response: StreamingResponse) -> dict:
        """
        Extracts the response JSON.
        """
        headers = {
            k.decode("utf-8"): v.decode("utf-8")
            for k, v in response.__dict__["_raw_headers"]
        }

        def extract_info(prefix: str) -> dict:
            return {
                key.split("_")[-1]: value
                for key, value in headers.items()
                if key.startswith(prefix)
            }

        return {"completion": self.completion}
