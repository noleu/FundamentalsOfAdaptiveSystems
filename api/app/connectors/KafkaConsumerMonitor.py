from aiokafka import AIOKafkaConsumer
import json

data_store = {"latest_message": None}

KAFKA_INSTANCE = "kafka:9092"
KAFKA_TOPIC = 'crowd-nav-monitored-stats'

consumer = AIOKafkaConsumer( 
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_INSTANCE,
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id=None)

async def connect():
    await consumer.start()
    try:
        print('# KafkaConsumerMonitor Connected!')
        # constantly replace with the most up-to-date value
        async for message in consumer:
            data_store["latest_message"] = message.value   
    except Exception as e:
        print("Connection to Kafka failed! Error:", e)
        raise e
    finally:
        await consumer.stop()
   