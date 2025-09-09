import json

class JsonBuilder:

    def __init__(self):
        self.metadata = {}


    def get_metadata(self,path,name, created_at, size):
        self.metadata["path"] = path
        self.metadata["name"] = name
        self.metadata["created_at"] = created_at
        self.metadata["size"] = size
        return self.metadata
