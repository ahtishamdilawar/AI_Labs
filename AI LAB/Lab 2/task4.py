class CityGraph:
    def __init__(self):
        self.city_map = {}

    def add_location(self, location):
        if location not in self.city_map:
            self.city_map[location] = {}
        else:
            print('already exist')

    def add_road(self, location1, location2, distance):
        if location1 not in self.city_map:
            print("doesnt exist")
            return
        if location2 not in self.city_map:
            print("doesnt exist")
            return
        self.city_map[location1][location2] = distance
        self.city_map[location2][location1] = distance

    def display_city_map(self):
        for location in self.city_map:
            print(f'{location}: {self.city_map[location]}')

city = CityGraph()
city.add_location('A')
city.add_location('B')
city.add_location('C')
city.add_road('A', 'B', 5)
city.add_road('B', 'C', 10)
city.add_road('A', 'C', 15)

city.display_city_map()
