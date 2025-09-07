from kafka import KafkaProducer
import json



class KafkaLoader:

    def __init__(self, host) -> None:
        self.producer = KafkaProducer(
            bootstrap_servers=f'{host}:9092',
            value_serializer=lambda v: v.encode('utf-8')
        )

    def insert(self, topic, data: list[dict]):

        for line in data:
            line = json.dumps(line)
            self.producer.send(topic, line)

        self.producer.flush()

