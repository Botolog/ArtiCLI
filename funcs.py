import json

def readData(filename:str="data.json") -> dict:
    with open(filename, "r") as data:
        json_data = data.read()
        
    return json.loads(json_data)

class Command:
    def __init__(self, name:str, action:callable):
        self.name = name
        self.action = action
    def __call__(self, *args, **kwds):
        self.action(*args)



