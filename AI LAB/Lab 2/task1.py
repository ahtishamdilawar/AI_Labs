class AquaFlow:
    def __init__(self, dimensions):
        self.length, self.width, self.depth = dimensions
        self.area = 0
        self.volume = 0

    def calculate_area(self):
        self.area = self.length * self.width

    def calculate_volume(self):
        self.volume = self.area * self.depth

    def display(self):
        print(f"Area: {self.area}")
        print(f"Volume: {self.volume} ")


length = float(input("Enter length: "))
width = float(input("Enter width: "))
depth = float(input("Enter depth: "))
dimensions = (length, width, depth)

aquaflow = AquaFlow(dimensions)
aquaflow.calculate_area()
aquaflow.calculate_volume()
aquaflow.display()
print("Irrigation Starts...")
