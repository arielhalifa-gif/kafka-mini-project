import json
import uuid
import models

from confluent_kafka import Producer


def producer_kafka(user: dict):
    producer_config = {
        "bootstrap.servers": "localhost:9092"
    }

    producer = Producer(producer_config)

    def delivery_report(err, msg):
        if err:
            print(f"❌ Delivery failed: {err}")
        else:
            print(f"✅ Delivered {msg.value().decode("utf-8")}")
            print(f"✅ Delivered to {msg.topic()} : partition {msg.partition()} : at offset {msg.offset()}")

    # user = models.User(full_name="moshe", email="moshe@gmail.com", age=20, phone= "0541234567", city="yerushalaim")

    value = json.dumps(user).encode("utf-8")

    producer.produce(
        topic="users",
        value=value,
        callback=delivery_report
    )

    producer.flush()