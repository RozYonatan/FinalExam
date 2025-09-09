from elasticsearch import Elasticsearch


class ElasticsearchClient:

    def __init__(self,conn):
        self.client = Elasticsearch(conn)


    def create_index(self,index_name:str,mapping:dict):
        # if not self.client.indices.exists(index=index_name):
        self.client.index(index=index_name, document=mapping)