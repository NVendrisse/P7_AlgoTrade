
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