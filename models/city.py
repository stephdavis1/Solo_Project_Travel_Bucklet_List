class City:
    def __init__(self, name, city_type, country, id=None, visited=False):
        self.name = name
        self.city_type = city_type
        self.country = country
        self.id = id
        self.visited = visited