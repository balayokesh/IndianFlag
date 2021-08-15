import turtle
from pygame import mixer

t = turtle.Turtle()

# Music player
mixer.init()
mixer.music.load('song.mp3')
mixer.music.play()

t.pensize(5)

def move (x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def drawFlag (color):
    t.color(color)
    t.begin_fill()
    t.forward(1000)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(1000)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.end_fill()

# Draw chakra
t.color('#050F88')
for i in range(24):
    t.forward(75)
    t.backward(75)
    t.left(15)
move(0, -80)
t.circle(80, 360)

# Draw green
move(-500, -85)
drawFlag('green')

# Draw orange
move(-500, 85 + 200)
drawFlag('orange')

turtle.done()