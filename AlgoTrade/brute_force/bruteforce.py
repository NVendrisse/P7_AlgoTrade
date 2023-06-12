import sys
import csv
from itertools import combinations


class Action:
    def __init__(self, name: str, cost: float, percent_gain: float):
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


def create_data_table(dataset_path: str):
    dataset = open(dataset_path, mode="r", encoding="UTF-8")
    data = csv.reader(dataset)
    table_data = []
    next(data, None)
    for row in data:
        table_data.append(Action(row[0], float(row[1]), float(row[2])))
    return table_data


def create_all_investment(data):
    all_buy = []
    for combination_length in range(1, len(data)):
        combination_table = combinations(data, combination_length)
        for elements in combination_table:
            tot = 0
            tot_gain = 0
            acts = []
            for action in elements:
                acts.append(action.name)
                tot += action.cost
                tot_gain += action.final_gain
        all_buy.append((acts, tot, tot_gain))
    return all_buy


def get_best_investment(invest_data):
    best_invest = invest_data[0]
    for invest_combination in invest_data:
        if invest_combination[1] <= 500:
            if invest_combination[2] > best_invest[2]:
                best_invest = invest_combination
    return best_invest

try:
    data_table = create_data_table(str(sys.argv[1]))
    all_combination = create_all_investment(data_table)
    best_solution = get_best_investment(all_combination)

    retrieve = best_solution[1] + best_solution[2]
    for i in best_solution[0]:
        print(i)
    print("Total cost : {}".format(best_solution[1]))
    print("Total gain : {}".format(best_solution[2]))
    print("For an investment of {} you'll retrieve {}".format(best_solution[1],round(retrieve,2)))
except IndexError:
    print("\nVous devez entrer un nom de fichier de données\n")
except FileNotFoundError:
    print("\nVous devez sélectionner fichier de données existant\n")
