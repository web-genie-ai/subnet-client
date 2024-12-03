from fastapi import APIRouter, Body
from pydantic import BaseModel
from typing import Optional

from app.api.v1.services.wg_synapse_service import WGSynapseService

router = APIRouter()
synapse_service = WGSynapseService()

class PromptRequest(BaseModel):
    prompt: str
    img_data: Optional[str] = None

@router.post("/generate")
async def generate(request: PromptRequest = Body(...)):
    solution = await synapse_service.generate(request.prompt, request.img_data)
    return {"solution": solution}
