from dispatcher import dispatch_alert

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Nexal Core API")

# In-memory storage for logs
log_storage = []

class LogEntry(BaseModel):
    tool_name: str
    message: str

@app.post("/log")
async def add_log(entry: LogEntry):
    log_storage.append(entry)
    dispatch_alert(entry.tool_name, entry.message) # <-- ADD THIS LINE
    return {"status": "success"}


@app.get("/logs")
async def get_logs():
    return {"logs": log_storage}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

