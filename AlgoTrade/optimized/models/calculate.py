

class Calculate:
    def __init__(self, data_table = []) -> None:
        self.data_table = data_table
        self.limit = 500
        self.total_cost = 0
        self.total_gain = 0
        self.total = 0
        self.best_buy = []
    
    def result(self):
        for act in self.data_table:
            if self.total_cost + act.cost <= self.limit and act.is_not_null():
                self.total_cost += act.cost
                self.total_gain += act.final_gain
                self.best_buy.append([act.name,act.cost,act.percent_gain])
            else:
                next
            self.total = self.total_cost + self.total_gain
        return self.best_buy,round(self.total_cost,2),round(self.total_gain,2),round(self.total,2)