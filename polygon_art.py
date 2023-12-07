import turtle

class Polygon:
    def __init__(self, num_sides, size, orientation, location, color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(num_sides):
            turtle.forward(self.size)
            turtle.left(360 /self.num_sides)
        turtle.penup()







Polygon_create = input("Which art do you want to generate? Enter a number between 1 to 8,inclusive: ")



