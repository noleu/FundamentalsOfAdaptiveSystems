from kafka.errors import KafkaTimeoutError

import RequestTypes as rt
from fastapi import APIRouter
from api.app.connectors.KafkaProducerExecute import KafkaProducerEx
from RequestTypes import Adaption_options

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

