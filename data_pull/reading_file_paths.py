from pathlib import Path



class ReadingFilePaths:

    def __init__(self, path):
        self.folder_path = Path(path)
        self.original_path = path
        self.file_paths = []

    def read_file_paths(self):
        self.file_paths = []
        for file in self.folder_path.iterdir():
            if file.is_file():
                self.file_paths.append(self.original_path + "/" + file.name)
        return self.file_paths

