class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.width*self.length


    def perimetr(self):
        return 2*(self.length+self.width)

rectangle_first = Rectangle(10, 3)
rectangle_second = Rectangle(30, 5)

print(f'Площадь первого {rectangle_first.area()}, периметр  первого {rectangle_first.perimetr()}')
print(f'Площадь второго {rectangle_second.area()}, периметр  второго {rectangle_second.perimetr()}')