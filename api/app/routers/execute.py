import asyncio
import logging

from aiokafka import AIOKafkaProducer
from kafka.errors import KafkaTimeoutError, KafkaError

from fastapi import APIRouter
from pydantic import BaseModel
import json


router = APIRouter(
    prefix="/execute",
    tags=["execute"],
    responses={404: {"description": "Not found"}},)


class AdaptationOptions(BaseModel):

    route_random_sigma: float | None = None
    exploration_percentage: float | None = None
    max_speed_and_length_factor: int | None = None
    average_edge_duration_factor: int | None = None
    freshness_update_factor: int | None = None
    freshness_cut_off_value: int | None = None
    re_route_every_ticks: int | None = None
    total_car_counter: int | None = None
    edge_average_influence: float | None = None


loop = asyncio.get_event_loop()

KAFKA_INSTANCE = "kafka:9092"
kafkaproducer = AIOKafkaProducer(loop=loop, bootstrap_servers=KAFKA_INSTANCE, api_version="0.10.1")


@router.put("/")
async def execute(options: AdaptationOptions):

    message = ""
    status = "error"
    await kafkaproducer.start()
    try:
        future = await kafkaproducer.send_and_wait("crowd-nav-commands", json.dumps(options.dict()).encode("ascii"))
        # response = await future
        status = "success"
        message = "The message was successfully sent to the kafka broker, the message is: " + str(options)
    except KafkaTimeoutError:
        logging.error("KafkaTimeoutError: " + str(KafkaTimeoutError))
        message = "While sending the message to the kafka broker a timeout occurred"
    except KafkaError:
        logging.error("KafkaError: " + str(KafkaError))
        message = "While sending the message to the kafka broker a KafkaError occurred"

    return {"status": status, "message": message}
