import turtle

# Function to draw the letter W
def draw_W():
    turtle.penup()
    turtle.goto(-50, 0)
    turtle.pendown()
    turtle.color("blue")
    turtle.pensize(3)
    turtle.left(250)
    turtle.forward(100)
    turtle.right(140)
    turtle.forward(100)
    turtle.left(140)
    turtle.forward(100)
    turtle.right(140)
    turtle.forward(100)

# Function to draw the letter S
def draw_S():
    turtle.penup()
    turtle.goto(30, 0)
    turtle.pendown()
    turtle.left(60)
    turtle.circle(23, 180)
    turtle.circle(-23, 220)
    
# Draw the letter W
draw_W()

# Draw the letter S
draw_S()

turtle.done()
