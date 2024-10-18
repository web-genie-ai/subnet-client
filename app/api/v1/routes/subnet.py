from fastapi import APIRouter

from app.api.v1.services.btc_synapse_service import BTCSynapseService


router = APIRouter()

synapse_service = BTCSynapseService()

@router.post("/generate")
async def generate():
    solution = await synapse_service.generate()
    return {"message": "Welcome to the BTCopilot Subnet Interface", "solution": solution}
