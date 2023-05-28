import os
import sys
import csv
from itertools import combinations
class Action:
    def __init__(self, name:str, cost:float, percent_gain:float):
        self.name = name
        self.cost = cost
        self.percent_gain = percent_gain
        self.final_gain = cost*(percent_gain/100)
    
    def is_not_null(self):
        if self.cost > 0:
            if self.percent_gain > 0:
                return True
        else:
            return False

dataset = open(str(sys.argv[1]), mode="r", encoding="UTF-8")
data = csv.reader(dataset)
table_data = []
next(data, None)
for row in data:
    table_data.append(Action(row[0], float(row[1]), float(row[2])))

for i in range(2,len(table_data)):
    table=combinations(table_data,i)
    
    for e in table:
        tot=0
        for j in e:
            tot+=j.cost
        print(tot)