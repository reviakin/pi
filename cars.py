class Car:
    runs = True

    def start(self, name):
        self.name = name
        if self.runs:
            print(f"{name} is started")
        else:
            print(f"{name} is broken")
