from consumption_and_processing.kafka_consumer import MetadatConsumer
from consumption_and_processing.MongoDAL import MongoDAL
from consumption_and_processing.esDAL import ElasticsearchClient
import uuid
class Manager:

    def __init__(self,kafka_host:str = "localhost",topic:str = "metadata",mongo_conn:str = "mongodb://localhost:27017/",mongo_db:str = "metadata",es_conn:str = "http://localhost:9200"):
        self.consumer = MetadatConsumer(kafka_host,topic).get_consumer()
        self.mongo_dal = MongoDAL(mongo_conn, mongo_db)
        self.es_dal = ElasticsearchClient(es_conn)

    def run(self):
        for message in self.consumer:
            message.value["unique_id"] = uuid.uuid4().hex
            self.mongo_dal.upload_audio(message.value["path"],message.value["unique_id"])
            self.es_dal.create_index("metadata",message.value["unique_id"])



