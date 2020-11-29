class Person:

    friends = []

    def __init__(self, firstname, secondname, place):
        self.firstname = firstname
        self.secondname = secondname
        self.place = place

    def relocate(self, place):
        self.place = place

    def fullname(self):
        return self.firstname + " " + self.secondname

    def info(self):
        return self.fullname() + " from " + self.place


class Worker(Person):

    def __init__(self, firstname, secondname, place, company):
        super().__init__(firstname, secondname, place)
        self.compony = company

    def info(self):
        return super().info() + " work at " + self.compony
