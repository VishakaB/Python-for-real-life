def greet(name):
    print(f"Hello, {name}!")

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")