import turtle
import math

# Function to draw a crescent using lines
def draw_crescent():
    # Set up the turtle
    turtle.speed(0)
    turtle.bgcolor("black")
    turtle.pensize(5)
    turtle.color("white")

    # Define the radius for the larger and smaller circles
    radius_large = 100
    radius_small = 75

    # Calculate the offset to position the smaller circle
    offset = radius_large - radius_small

    # Draw the larger circle using lines
    turtle.penup()
    for i in range(350):
        rad = math.radians(i)
        x = radius_large * math.cos(rad)
        y = radius_large * math.sin(rad)
        turtle.goto(x, y)
        turtle.pendown()
    
    # Shade the crescent shape
    turtle.penup()
    turtle.goto(radius_small - offset, 0)
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    for i in range(360):
        rad = math.radians(i)
        x = offset + radius_small * math.cos(rad)
        y = radius_small * math.sin(rad)
        turtle.goto(x, y)
    turtle.goto(radius_small - offset, 0)
    turtle.end_fill()

# Function to write text
def write_text(text, position, font_size, font_color, font_type):
    turtle.penup()
    turtle.goto(position)
    turtle.color(font_color)
    turtle.write(text, align="center", font=(font_type, font_size, "bold"))
    turtle.pendown()

# Draw the crescent
draw_crescent()


write_text("Eid Mubarak", (0, -180), 27, "brown", "Comic Sans MS")  # تغيير الخط لـ Comic Sans MS

# Hide the turtle cursor and finish drawing
turtle.hideturtle()
turtle.done()
