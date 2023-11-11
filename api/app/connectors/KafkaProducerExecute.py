# basic idea of this class is from RTX project
import logging
from colorama import Fore
from kafka import KafkaProducer
import json

from kafka.errors import KafkaTimeoutError


class KafkaProducerEx():
    """ implements a change provider based on kafka publish """

    def __init__(self):
        # load config
        try:
            self.kafka_uri = "kafka:9092"
            self.topic = "crowd-nav-commands"
            logging.info("> KafkaProducer  |  JSON  | URI: " + self.kafka_uri + " | Topic: " +
                         self.topic, Fore.CYAN)
        except KeyError:
            logging.error("configuration.kafka_producer was incomplete")
            exit(1)
        # look at the serializer
        self.serialize_function = lambda v: json.dumps(v).encode('utf-8')

        # try to connect
        try:
            # stop annoying logging
            logging.getLogger("kafka.coordinator.consumer").setLevel("ERROR")
            logging.getLogger("kafka.conn").setLevel("ERROR")
            self.producer = KafkaProducer(bootstrap_servers=self.kafka_uri,
                                          value_serializer=self.serialize_function,
                                          request_timeout_ms=5000)
        except:
            logging.error("connection to kafka failed")
            exit(1)

    def applyChange(self, message):
        """ send out a message through kafka """
        logging.debug("Sending out Kafka Message:" + str(message))

        try:
            return self.producer.send(self.topic, message)
        except KafkaTimeoutError as timeOutError:
            logging.error("KafkaTimeoutError: " + str(timeOutError))
            raise timeOutError
