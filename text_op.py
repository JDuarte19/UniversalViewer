import csv
import json

working_file = ['txt', 'json', 'csv']

class Textfile:
    lines = [0]
    size = 0
    file_name = ""
    file_type = ""

    #initilization function
    # checks to see if instance is of a working file type
    # if not returns false
    # if yes then
    def __init__(self,file_name):
        file = file_name.split('.')
        type = file[1]
        self.file_name = file_name
        self.type = type

        checker = False
        for x in working_file:
            if x == type:
                checker = True

        if checker == False:
            print("ERROR FILE TYPE")
            return False

        lines = list()

        with open(self.file_name, 'r') as f:
            if self.type == 'csv':
                content = csv.DictReader(f, delimiter=',')
            elif self.type == 'json':
                content = json.load(f)
                self.lines = content
                return
            elif self.type == 'txt':
                content = f
            
            for line in content:
                lines.append(line)

        self.lines = lines
        
    def remove_n(self,n):
        lines = list()
        for line in self.lines:
            split = line.split(n)
            line = split[0]
            lines.append(line)
        self.lines = lines

    def print(self):
        print(self.lines)
    
    def type_of(self):
        return self.file_type
    def size_of(self):
        return self.size
    def name_of(self):
        return self.file_name

    def printlines(self):
        if self.type == 'json':
            self.print()
            return
        for line in self.lines:
            print(line)
