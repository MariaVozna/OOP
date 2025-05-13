from abc import ABC, abstractmethod

# Принцип єдиної відповідальності (SRP): кожен клас має одну чітку відповідальність

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Клас Rectangle відповідає тільки за прямокутник
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Клас Circle відповідає тільки за коло
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Принцип відкритості/закритості (OCP): ми можемо додавати нові фігури, не змінюючи існуючий код

class AreaPrinter:
    def print_area(self, shape: Shape):
        print(f"Площа фігури: {shape.area()}")

# --- Приклад використання ---
if __name__ == "__main__":
    rectangle = Rectangle(4, 5)
    circle = Circle(3)

    printer = AreaPrinter()
    printer.print_area(rectangle)
    printer.print_area(circle)
