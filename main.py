from fastapi import FastAPI
import uvicorn
from app.api.v1.routes.subnet import router as subnet_router
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the BTCopilot Subnet Interface"}

app.include_router(router=subnet_router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
