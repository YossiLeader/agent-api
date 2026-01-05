from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import OpenAI

app = FastAPI()   # 👈 זה הקריטי!

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

class AgentRequest(BaseModel):
    input: str

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/agent")
def agent(req: AgentRequest):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=req.input
    )
    return {"answer": response.output_text}
