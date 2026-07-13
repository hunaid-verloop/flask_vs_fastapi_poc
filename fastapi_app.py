import asyncio
from fastapi import FastAPI
from tasks import compute_fibanocci
import uvicorn

app = FastAPI()


@app.get("/io_bound")
async def io_bound_task():
    await asyncio.sleep(1)
    return {"task": "iobound"}

@app.get("/cpu_bound")
async def cpu_bound_task():
    compute_fibanocci(32)
    return {"task": "cpu_bound"}


@app.get("/io_and_cpu")
async def mixed_task():
    await asyncio.sleep(1)
    compute_fibanocci(32)
    return {"task": "mixed"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000)