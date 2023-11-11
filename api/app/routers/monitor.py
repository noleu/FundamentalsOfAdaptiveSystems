from fastapi import APIRouter
from ..connectors import KafkaConsumerMonitor

router = APIRouter()

@router.get("/")
def monitor():
  return { "message": KafkaConsumerMonitor.data_store["latest_message"]}