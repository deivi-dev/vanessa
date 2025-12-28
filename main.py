from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["Content-Type"]
)

class Prompt(BaseModel):
    input: str

@app.post("/generate-response")
def handle_request(prompt: Prompt):
    try:
        response = agent.generate_response(prompt.input)
        return response
    
    except requests.exceptions.Timeout:
        return {"error": "The request timed out."}, 504
    
    except requests.exceptions.HTTPError:
        return {"error": "An HTTP error occurred while processing the request."}, 502