import os
import csv
from models.action import Action


class Open:
    def __init__(self, path: str) -> None:
        self.path = path

    def open_data(self):
        dataset = open(self.path, mode="r", encoding="UTF-8")
        data = csv.reader(dataset)
        table_data = []
        next(data, None)
        for row in data:
            table_data.append(Action(row[0], float(row[1]), float(row[2])))
        table_data = sorted(
            table_data, key=lambda act: act.percent_gain, reverse=True)
        return table_data
