class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width


    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return (self.height + self.width) * 2



task = Rectangle(10, 25)

print("Площа:", task.calculate_area())
print("Периметр:", task.calculate_perimeter())



