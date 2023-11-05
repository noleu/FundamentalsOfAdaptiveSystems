from fastapi import FastAPI
from .routers import example, execute_schema

app = FastAPI()

app.include_router(example.router, prefix="/example")
app.include_router(execute_schema.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!----"}