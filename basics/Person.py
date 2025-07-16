class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f'Привет, меня зовут {self.name} и мне {self.age} лет'

    def is_adult(self):
        return self.age > 18
person_1 = Person('Тимур', 20)
person_2 = Person('Руслан', 10)

print(person_1.greet())
print(person_2.greet())

print(person_2.is_adult())