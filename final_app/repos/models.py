class GitHubRepo():
    def __init__(self, name, language, num_stars):
        self.name = name
        self.language = language
        self.num_stars = num_stars

    def __str__(self):
        return f"name: {self.name}, language: {self.language}, stars: {self.num_stars}"

    def __repr__(self):
        return f"GitHubRepo({self.name}, {self.language}, {self.num_stars})"
