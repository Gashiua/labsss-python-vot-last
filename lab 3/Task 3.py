from abc import ABC, abstractmethod
import math

# Абстрактный базовый класс Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Класс Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Класс Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Класс Triangle
class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self.a = side_a
        self.b = side_b
        self.c = side_c

    def area(self):
        # Полупериметр
        s = self.perimeter() / 2
        # Формула Герона
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

# Функция для демонстрации полиморфизма
def print_shape_info(shape):
    print(f"Площадь: {shape.area()}")
    print(f"Периметр: {shape.perimeter()}")

# Пример использования:
rect = Rectangle(3, 4)
circle = Circle(2)
triangle = Triangle(3, 4, 5)

print("Rectangle:")
print_shape_info(rect)

print("\nCircle:")
print_shape_info(circle)

print("\nTriangle:")
print_shape_info(triangle)