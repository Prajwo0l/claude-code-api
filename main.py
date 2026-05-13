from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import subprocess

app = FastAPI()

API_KEY = "eclectic-secret-123"

class Prompt(BaseModel):
    prompt: str

@app.post("/claude")
def run_claude(req: Prompt, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    # TEMP SAFE RESPONSE (for Railway test)
    # We remove Docker dependency for now
    return {
        "output": f"Received: {req.prompt}"
    }