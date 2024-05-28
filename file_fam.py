import json, csv

def map_to(file_name):
    name,type = file_name.split('.')
    match type:
        case "txt":
            return TextFile(file_name)
        case "json":
            return JsonFile(file_name)
        case "csv":
            return CSVFile(file_name)
        case _:
            print("Error file type not supported.")

class BaseFile:
    #base file should
    type = ""
    content = ""
    def __init__(self,file_name):
        self.base_file = file_name
        return
    def describe(self,string):
        self.short_description = string
        return
    def name(self):
        return self.base_file
    def descript(self):
        return self.short_description
    def type(self):
        return self.type
    #print
    def ptot(self):
        print(self.content)
    def plines(self):
        for line in self.content:
            print(line)
    
class TextFile(BaseFile):
    size = ""
    def read(self):
        self.type = "txt"
        with open(self.base_file,'r') as f:
            self.content = f.readlines()

    def remove_n(self):
        lines = list()
        for line in self.content:
            split = line.split('\n')
            line = split[0]
            lines.append(line)
        self.content = lines

class JsonFile(BaseFile):
    def read(self):
        self.type = "json"
        with open(self.base_file, 'r') as f:
            self.content = json.load(f)

class CSVFile(BaseFile):
    def read(self):
        self.type = "csv"
        with open(self.base_file, 'r') as f:
            self.content = csv.DictReader(f, delimiter=',')

#main start
file_name = "requirements.txt"
#file_name = "movie.json"
base_file = map_to(file_name)

base_file.read()
#base_file.remove_n()
base_file.plines()
