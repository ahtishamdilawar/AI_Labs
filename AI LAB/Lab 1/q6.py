def Calculate_Area(length, width):
   return length * width

def Calculate_Volume(length, width, height):
   return length * width * height

length = float(input("Enter length of room: "))
width = float(input("Enter width of room: "))
height = float(input("Enter height of room: "))

area = Calculate_Area(length, width)
volume = Calculate_Volume(length, width, height)

print("Area of room: %.2f" % area)
print("Volume of room: %.2f" % volume)
print("Cleaning Starts...")