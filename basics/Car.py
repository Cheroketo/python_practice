from datetime import datetime


class Car:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year

    def car_info(self):
        return f'Марка машины - {self.mark}\nМодель машины - {self.model}\nГод выпуска - {self.year}'

    def is_oldtimer(self):
        return datetime.now().year - self.year > 30