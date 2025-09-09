from kafka import KafkaConsumer
import json


class MetadatConsumer:

    def __init__(self, host,topic):
        self.consumer = KafkaConsumer(topic,
                                      group_id=topic,
                                      value_deserializer=lambda x: json.loads(x.decode('utf-8')),
                                      bootstrap_servers=f'{host}:9092',
                                      auto_offset_reset='earliest')
    def get_consumer(self):
        return self.consumer