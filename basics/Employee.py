class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def info(self):
        return f'Сотрудник {self.name}, зарплата {self.salary}'

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def info(self):
        all_result = super().info()
        return f'{all_result}, департамент - {self.department}'

empl = Employee('Федор', 35000)
print(empl.info())

man = Manager('Макс', 25000, 2)
print(man.info())

