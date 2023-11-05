from logging import error

from kafka import KafkaConsumer
from kafka import KafkaProducer
from app import Config
from colorama import Fore
import json

consumer = None
producer = None

def connect():
    """Try to connect to Kafka, else exits the process."""
    if Config.kafkaUpdates:
       initializeConsumer()
       initializeProducer()  

def initializeConsumer():
  try:
    global consumer
    consumer = KafkaConsumer(
        bootstrap_servers=Config.kafkaHost,
        api_version=(0, 10, 1),
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        request_timeout_ms=5000,
        group_id=None,
        auto_offset_reset='earliest')
    
    consumer.subscribe([Config.kafkaTopicMonitoring])
    print(Fore.GREEN + '# KafkaMonitorC Connected!' + Fore.RESET)
  except Exception as e:
      print(Fore.RED + "Connection to Kafka failed! Error:", e, Fore.RESET)

def initializeProducer():
  try:
    global producer
    producer = KafkaProducer(
        bootstrap_servers=Config.kafkaHost,
        api_version=(0, 10, 1),
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        request_timeout_ms=5000)
    
    print(Fore.GREEN + '# KafkaMonitorP Connected!' + Fore.RESET)
  except Exception as e:
      print(Fore.RED + "Connection to Kafka failed! Error:", e, Fore.RESET)

def publish(msg):
   producer.send(Config.kafkaTopicMonitoring, msg)

def monitor():
  for message in consumer:
      print(message.value)