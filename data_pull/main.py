from manager import Manager

manager = Manager("C:/Users/Yonatan/podcasts")
manager.get_metadata()
manager.load_kafka()
print(manager.get_json())
