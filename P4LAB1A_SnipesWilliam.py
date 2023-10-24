import turtle

# Function to draw a square
def draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.left(90)

# Function to draw a triangle
def draw_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)


# Draw a square
draw_square(100)

# Move to a new position for the triangle
turtle.penup()
turtle.goto(150, 0)
turtle.pendown()

# Draw a triangle
draw_triangle(100)


turtle.done()
