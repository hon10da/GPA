from turtle import *
import math

def heart_curve(t):
    x = 100 * (math.sin(t) ** 3)  # زيادة قيمة x
    y = 80 * math.cos(t) - 35 * math.cos(2 * t) - 19 * math.cos(3 * t) - math.cos(4 * t)
    return x, y

def draw_heart():
    pensize(2)
    color("red")
    begin_fill()  # Begin filling the heart shape with color
    penup()
    goto(heart_curve(0))
    pendown()
    for t in range(0, 500):
        x, y = heart_curve(math.radians(t))
        goto(x, y)
    end_fill()  # End filling the heart shape with color

bgcolor("black")
speed(0)

# تحديد موقع رسم القلب لترك مساحة لوضع الكلمة "NOUR" داخل القلب
penup()
goto(0, -20)
pendown()
draw_heart()

penup()
goto(0, -240)  # تحريك النص إلى الأسفل
color("brown")
write("I love you 🤍", align="center", font=("Comic Sans MS", 30))  # Second line

# رسم الكلمة "NOUR" داخل القلب
goto(0, -50)
color("white")
write("N O U R", align="center", font=("Courier", 30))

hideturtle()
done()
