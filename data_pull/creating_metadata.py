import datetime
from pathlib import Path

class Metadata:

    def __init__(self, path):
        self.original_path = path
        self.path = Path(path)
        self.name = ""
        self.size = 0
        self.created_at = ""

    def get_name(self):
        self.name = self.path.name

    def get_size(self):
        self.size = self.path.stat().st_size

    def get_created_at(self):
        self.created_at = str(datetime.datetime.fromtimestamp(self.path.stat().st_ctime))




