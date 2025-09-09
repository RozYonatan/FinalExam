from manager import Manager
from dotenv import load_dotenv,find_dotenv
import os
load_dotenv(find_dotenv())

path = os.getenv("PATH")


manager = Manager("C:/Users/Yonatan/podcasts")
manager.get_metadata()
manager.load_kafka()
print(manager.get_json())
