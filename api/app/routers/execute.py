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


class Knobs(BaseModel):
    routeRandomSigma: float
    explorationPercentage: float
    maxSpeedAndLengthFactor: int
    averageEdgeDurationFactor: int
    freshnessUpdateFactor: int
    freshnessCutOffValue: int
    reRouteEveryTicks: int


class AdaptionOptions(BaseModel):
    # Knobs: Knobs
    routeRandomSigma: float | None = None
    explorationPercentage: float | None = None
    maxSpeedAndLengthFactor: int | None = None
    averageEdgeDurationFactor: int | None = None
    freshnessUpdateFactor: int | None = None
    freshnessCutOffValue: int | None = None
    reRouteEveryTicks: int | None = None
    totalCarCounter: int | None = None
    edgeAverageInfluence: float | None = None


loop = asyncio.get_event_loop()

KAFKA_INSTANCE = "kafka:9092"
kafkaproducer = AIOKafkaProducer(loop=loop, bootstrap_servers=KAFKA_INSTANCE, api_version="0.10.1")


@router.put("/")
async def execute(options: AdaptionOptions):

    message = ""
    status = "error"
    await kafkaproducer.start()
    try:
        future = await kafkaproducer.send("crowd-nav-commands", json.dumps(options.dict()).encode("ascii"))
        response = await future
        status = "success"
        message = "The message was successfully sent to the kafka broker, the message is: " + str(options)
    except KafkaTimeoutError:
        logging.error("KafkaTimeoutError: " + str(KafkaTimeoutError))
        message = "While sending the message to the kafka broker a timeout occurred"
    except KafkaError:
        logging.error("KafkaError: " + str(KafkaError))
        message = "While sending the message to the kafka broker a KafkaError occurred"

    return {"status": status, "message": message}
