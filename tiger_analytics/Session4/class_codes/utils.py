import csv
import json

class Reader():
    def __init__(self,path):
        self.path = path
        self.keys = None
        self.rows = None
        self.cols = None
        self.col_names = None
    
    def read_flat_file(self,delimiter):
        data = []
        with open(self.path,"r",encoding="utf-8") as f:
            reader = csv.DictReader(f,delimiter=delimiter)
            for row in reader:
                data.append(row)
        self.rows = len(data)
        self.cols = len(data[0])
        self.col_names = data[0].keys()
        return data 
    
    def read_json(self):
        with open(self.path,"r",encoding="utf-8") as f:
            raw_json = f.read()
        json_data = json.loads(raw_json)
        self.keys = json_data.keys()
        return json_data
