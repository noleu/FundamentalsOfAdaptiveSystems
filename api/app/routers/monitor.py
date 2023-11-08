from fastapi import APIRouter
from .src import KafkaConsumerMonitor

router = APIRouter()

@router.get("/")
def monitor():
  return { "message": KafkaConsumerMonitor.data_store["latest_message"] }