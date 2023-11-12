from fastapi import FastAPI
from .routers import adaptation_options, adaptation_options_schema, execute_schema, monitor_schema, monitor, execute
from .connectors import KafkaConsumerMonitor
from threading import Thread
import asyncio
from aiokafka import AIOKafkaProducer
app = FastAPI()

app.include_router(monitor.router)
app.include_router(monitor_schema.router)
app.include_router(execute.router)
app.include_router(execute_schema.router)
app.include_router(adaptation_options.router)
app.include_router(adaptation_options_schema.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!----"}

@app.on_event("startup")
async def startup_event():
    await asyncio.sleep(35)
    consumerThread = Thread(target=KafkaConsumerMonitor.connect)
    consumerThread.start()
