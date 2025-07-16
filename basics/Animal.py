class Animal:
    def speak(self):
        return f'Животное издает звук'

class Dog(Animal):
    def speak(self):
        return f'Гав!'

class Cat(Animal):
    def speak(self):
        return f'Мяу!'

animal = Animal()
animal.speak()

dog = Dog()
dog.speak()

cat = Cat()
cat.speak()