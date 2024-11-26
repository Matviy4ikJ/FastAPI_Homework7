from fastapi import FastAPI, Path, Query, Header, HTTPException
from datetime import datetime

app = FastAPI()


@app.get("/user/{user_id}")
async def get_user(
        user_id: int = Path(..., description="ID користувача"),
        timestamp: str = Query(None, description="Мітка часу"),
        x_client_version: str = Header(..., description="Версія клієнта")
):
    
    if not timestamp:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {
        "message": f"Hello, user {user_id}!",
        "user_id": user_id,
        "timestamp": timestamp,
        "x_client_version": x_client_version,
    }