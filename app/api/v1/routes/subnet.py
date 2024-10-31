from fastapi import APIRouter, Body
from pydantic import BaseModel

from app.api.v1.services.btc_synapse_service import BTCSynapseService


router = APIRouter()

synapse_service = BTCSynapseService()

class PromptRequest(BaseModel):
    prompt: str

@router.post("/generate")
async def generate(request: PromptRequest = Body(...)):
    print("=== request ===>", request)
    solution = await synapse_service.generate(request.prompt)
    return {"message": "Welcome to the BTCopilot Subnet Interface", "solution": solution}
