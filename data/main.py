from manager import Manager

manager = Manager("C:/Users/Yonatan/podcasts")
manager.get_metadata()
print(manager.get_json())
