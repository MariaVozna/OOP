# Патерн Composite
class Component:
    def operation(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class Leaf(Component):
    def __init__(self, name):
        self.name = name

    def operation(self):
        print(f"Leaf: {self.name}")

class Composite(Component):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def operation(self):
        print(f"Composite: {self.name}")
        for child in self.children:
            child.operation()

# Патерн Facade
class SubsystemA:
    def operation_a(self):
        print("Subsystem A operation")

class SubsystemB:
    def operation_b(self):
        print("Subsystem B operation")

class SubsystemC:
    def operation_c(self):
        print("Subsystem C operation")

class Facade:
    def __init__(self):
        self.subsystem_a = SubsystemA()
        self.subsystem_b = SubsystemB()
        self.subsystem_c = SubsystemC()

    def operation(self):
        print("Facade: Simplifying complex operations...")
        self.subsystem_a.operation_a()
        self.subsystem_b.operation_b()
        self.subsystem_c.operation_c()

# Демонстрація
if __name__ == "__main__":
    # Демонстрація патерну Composite
    leaf1 = Leaf("Leaf 1")
    leaf2 = Leaf("Leaf 2")
    composite = Composite("Composite 1")
    composite.add(leaf1)
    composite.add(leaf2)

    print("Composite pattern demonstration:")
    composite.operation()

    # Демонстрація патерну Facade
    facade = Facade()
    print("\nFacade pattern demonstration:")
    facade.operation()
