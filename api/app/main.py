from fastapi import FastAPI
from .routers import execute_schema, monitor_schema, monitor, adaption_options_schema, adaption_options, execute
from .connectors import KafkaConsumerMonitor
import asyncio
app = FastAPI()

app.include_router(monitor.router)
app.include_router(monitor_schema.router)
app.include_router(execute.router)
app.include_router(execute_schema.router)
app.include_router(adaption_options.router)
app.include_router(adaption_options_schema.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!----"}

@app.on_event("startup")
async def startup_event():
    # wait for Kafka to be ready
    await asyncio.sleep(35)
    asyncio.create_task(KafkaConsumerMonitor.connect())




