from models.open_dataset import Open
from models.calculate import Calculate
from views.display import Display

class Trade:
    
    def begin(file_path:str):
        table = Open(file_path).open_data()
        best_combination = Calculate(table).result()
        Display.draw(best_combination)