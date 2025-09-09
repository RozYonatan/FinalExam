from pymongo import MongoClient
import gridfs

class MongoDAL:

    def __init__(self,connection_string,db_name):
        self.client = MongoClient(connection_string)
        db = self.client[db_name]
        self.fs = gridfs.GridFS(db)

    def upload_audio(self, file_path,unique_id):
        with open(file_path, "rb") as f:
            self.fs.put(f, filename=file_path,unique_id=unique_id)


