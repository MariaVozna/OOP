import copy

# Базовий клас
class Sheep:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Sheep(name={self.name}, color={self.color})"

# Демонстрація
if __name__ == "__main__":
    original = Sheep("Dolly", "White")
    print("Original:", original)

    # Клонування
    clone1 = original.clone()
    clone1.name = "Daisy"  # змінюємо ім'я, щоб побачити відмінність
    print("Clone 1:", clone1)

    clone2 = original.clone()
    clone2.color = "Black"
    print("Clone 2:", clone2)
