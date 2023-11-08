from kafka import KafkaProducer
from app import Config
from colorama import Fore
import json

producer = None

def connect():
    """Try to connect to Kafka, else exits the process."""
    if Config.kafkaUpdates:
      try:
        global producer
        producer = KafkaProducer(
            bootstrap_servers=Config.kafkaHost,
            api_version=(0, 10, 1),
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            request_timeout_ms=5000)
        
        print(Fore.GREEN + '# KafkaProducerMonitor Connected!' + Fore.RESET)
      except Exception as e:
        print(Fore.RED + "Connection to Kafka failed! Error:", e, Fore.RESET)  

def publish(topic, message):
  producer.send(topic, message)