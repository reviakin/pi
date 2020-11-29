#import importlib
# importlib.reload()

class Car:
    runs = True
    number_of_wheels = 4

    def __init__(self, name):
        print("new car!")
        self.name = name

    def __str__(self):
        return f"My car the {self.name} is {self.runs}"

    def start(self):
        if self.runs:
            print(f"{self.name} is started")
        else:
            print(f"{self.name} is broken")
