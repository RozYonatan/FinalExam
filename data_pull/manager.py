from reading_file_paths import ReadingFilePaths
from creating_metadata import Metadata
from json_builder import JsonBuilder
from kafka_producer import KafkaLoader

class Manager:

    def __init__(self, path):
        self.folder_path = path
        self.all_data = []


    def get_file_paths(self):
        return ReadingFilePaths(self.folder_path).read_file_paths()

    def get_metadata(self):
        for path in self.get_file_paths():
            data = Metadata(path)
            data.get_name()
            data.get_size()
            data.get_created_at()
            self.all_data.append(data)


    def get_json(self):
        results = []
        for data in self.all_data:
            results.append(JsonBuilder().get_metadata(data.original_path,data.name,data.created_at,data.size))
        return results

    def load_kafka(self):
        KafkaLoader().insert("metadata", self.get_json())




