from fastapi import FastAPI

import httpx
import uvicorn

app = FastAPI()

external_api = "http://localhost:6000"

@app.get("/bot")
async def bot_task():
    async with httpx.AsyncClient() as client:
        response = await client.get(external_api)
    return response.json()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)