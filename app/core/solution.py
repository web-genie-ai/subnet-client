from pydantic import BaseModel, Field

class Solution(BaseModel):
    html: str = Field("", description="The html solution")
    css: str = Field("", description="The css solution")