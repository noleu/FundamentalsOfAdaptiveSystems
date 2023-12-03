from api.app.connectors.KafkaConsumerMonitor import consumer
from api.app.Models.Database import Historic_Car_Data
import json

async def get_messages_from_kafka(lastIndex):
    messages = []
    await consumer.start()
    try:
        print('# KafkaConsumerMonitor Connected!')
        # constantly replace with the most up-to-date value
        async for message in consumer:
            if message.offset > lastIndex:
                messages.append(message.value)
    except Exception as e:
        print("Connection to Kafka failed! Error:", e)
        raise e
    finally:
        await consumer.stop()

    return messages

async def insert_latest_message_into_db(db, message):

    # convert json kafka message to object
    for

    db.add(Historic_Car_Data)
    db.commit()
    db.refresh(message)
    return message


def convert_messages_to_objects(messages):
    objects = {"cars": [], "config": []}

    for message in messages:
        car = Historic_Car_Data()
        objects["cars"].append(Car)
    return objects