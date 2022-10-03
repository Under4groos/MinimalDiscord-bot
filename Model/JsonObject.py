import json

class JsonModel:
    def __init__(self, path):
        Path = path
    def Serialization(self):
        with open("Data\data.json") as file:
            DATA = file.read()
            return json.loads(DATA)
        return null