from abc import ABC, abstractmethod

# Наслідування
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass

    def info(self):
        return f"This is an animal named {self.name}."

# Інкапсуляція та реалізація абстрактного методу
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.__breed = breed  # Приватний атрибут

    def speak(self):
        return "Woof!"

    def get_breed(self):
        return self.__breed

    def set_breed(self, breed):
        self.__breed = breed

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.__color = color  # Приватний атрибут

    def speak(self):
        return "Meow!"

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

# Поліморфізм
animals = [Dog("Buddy", "Labrador"), Cat("Whiskers", "Gray"), Dog("Max", "Bulldog")]

for animal in animals:
    print(animal.info())
    print("Sound:", animal.speak())
