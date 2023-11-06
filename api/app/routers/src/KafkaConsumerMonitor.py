from kafka import KafkaConsumer
import json

data_store = {"latest_message": None}
consumer = None

def connect():
  try:
    global consumer
    consumer = KafkaConsumer(
        bootstrap_servers="kafka:9092",
        api_version=(0, 10, 1),
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        request_timeout_ms=5000,
        group_id=None,
        auto_offset_reset='earliest')
    
    consumer.subscribe(["crowd-nav-monitored-stats"])
    print('# KafkaConsumerMonitor Connected!')

    for message in consumer:
      data_store["latest_message"] = message.value   

  except Exception as e:
      print("Connection to Kafka failed! Error:", e)
      raise e
   