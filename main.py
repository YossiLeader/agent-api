import os
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

class AgentRequest(BaseModel):
    input: str

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/agent")
def agent(req: AgentRequest):
    resp = client.responses.create(
        model="gpt-4.1-mini",
        input=req.input,
    )
    return {"answer": resp.output_text}
