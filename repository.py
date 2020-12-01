class Repository:
    def __init__(self, name, number_of_stars, language):
        self.name = name
        self.number_of_stars = number_of_stars
        self.language = language

    def __str__(self):
        return f"Repository: '{self.name}' on {self.language}' with {self.number_of_stars} ⭐️"
