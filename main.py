from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

API_KEY = "eclectic-secret-123"

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/claude")
def claude(req: dict, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return {
        "output": f"Received: {req.get('prompt')}"
    }