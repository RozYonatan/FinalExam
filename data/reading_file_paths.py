from pathlib import Path



class ReadingFilePaths:

    def __init__(self, path):
        self.folder_path = Path(path)
        self.file_paths = []

    def read_file_paths(self):
        self.file_paths = [file for file in self.folder_path.iterdir() if file.is_file()]
        return self.file_paths

