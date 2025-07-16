class Student:
    def __init__(self, name, lst):
        self.name = name
        self.lst = lst

    def add_grade(self, grade):
        self.lst.append(grade)

    def average_grade(self):
        avg = sum(self.lst) / len(self.lst)
        return avg
    
    def is_excellent(self):
        return self.average_grade() > 4.5

