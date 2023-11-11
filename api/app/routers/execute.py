from kafka.errors import KafkaTimeoutError

from fastapi import APIRouter
from ..connectors.KafkaProducerExecute import KafkaProducerEx
from pydantic import BaseModel

router = APIRouter()


@router.put("/")
def example_endpoint(options: Adaption_options):
    kafkaproducer = KafkaProducerEx()
    message = ""
    status = ""
    try:
        future = kafkaproducer.applyChange("test")
        future.get(timeout=10)
        status = "success"
        message = "The message was successfully sent to the kafka broker, the message is: " + str(options)
    except KafkaTimeoutError as timeoutError:
        status = "error"
        message = "While sending the message to the kafka broker a timeout occurred"

    return {"status": status, "message": message}


class AdaptionOptions(BaseModel):
    Knobs: Knobs
    totalCarCounter: int
    edgeAverageInfluence: float


class Knobs(BaseModel):
    routeRandomSigma: float
    explorationPercentage: float
    maxSpeedAndLengthFactor: int
    averageEdgeDurationFactor: int
    freshnessUpdateFactor: int
    freshnessCutOffValue: int
    reRouteEveryTicks: int