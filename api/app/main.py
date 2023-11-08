from fastapi import FastAPI
from .routers import example, execute_schema, monitor_schema, monitor
from .routers.src import KafkaConsumerMonitor
from threading import Thread
import asyncio

app = FastAPI()

app.include_router(example.router, prefix="/example")
app.include_router(monitor.router, prefix="/monitor")
app.include_router(monitor_schema.router)
app.include_router(execute_schema.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!----"}

@app.on_event("startup")
async def startup_event():
    await asyncio.sleep(35)
    thread = Thread(target=KafkaConsumerMonitor.connect)
    thread.start()