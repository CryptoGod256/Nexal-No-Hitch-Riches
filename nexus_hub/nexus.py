import os
import requests
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/nexus", tags=["Nexus Master Orchestrator"])

DO_INFERENCE_URL = "https://inference.do-ai.run/v1/chat/completions"
API_KEY = os.getenv("DO_MODEL_KEY")

class TaskPayload(BaseModel):
    task_type: str  
    content: str

@router.post("/dispatch")
async def dispatch_task(payload: TaskPayload):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    system_prompt = (
        "You are Nexus, the Master Orchestrator of Nexal Intelligence. "
        "Analyze the incoming task and route it to the appropriate specialist: "
        "OpenCode (engineering), OpenClaw (operations), or AdClaw (marketing/growth)."
    )
    
    data = {
        "model": "claude-sonnet",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Task Type: {payload.task_type}\nDetails: {payload.content}"}
        ],
        "temperature": 0.2
    }
    
    try:
        response = requests.post(DO_INFERENCE_URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        
        assigned_agent = payload.task_type.lower()
        return {
            "status": "success",
            "orchestrator": "Nexus (Claude Sonnet)",
            "routed_to": assigned_agent,
            "response": result['choices'][0]['message']['content']
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
