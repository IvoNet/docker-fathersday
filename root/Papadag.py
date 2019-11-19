import turtle

import math


def pytha(varA, varB):
    return math.sqrt(varA ** 2 + varB ** 2)


def pappadag():
    sem = turtle.Turtle()
    turtle.setup(width=900, height=720, startx=0, starty=0)
    turtle.bgcolor('black')
    sem.hideturtle()
    sem.speed(20)

    sem.color('#005597')
    sem.pensize(15)
    sem.penup()
    sem.backward(420)
    sem.left(90)
    sem.forward(345)
    sem.pendown()
    sem.backward(200)
    sem.forward(100)
    sem.right(90)
    sem.forward(100)
    sem.left(90)
    sem.forward(100)
    sem.backward(200)
    sem.right(90)

    sem.penup()
    sem.forward(50)
    sem.left(74)
    sem.pendown()

    # sem.forward(223.6067977)
    sem.forward(pytha(100, 200))
    sem.right(148)
    sem.forward(pytha(100, 200))
    sem.backward(103.0776406)
    sem.right(106)
    sem.forward(68)
    sem.penup()
    sem.backward(124)
    sem.right(90)

    sem.pendown()
    sem.backward(100)
    sem.forward(200)
    sem.right(90)
    sem.forward(100)
    sem.right(90)
    sem.forward(100)
    sem.right(90)
    sem.forward(100)
    sem.penup()
    sem.backward(150)

    sem.pendown()
    sem.right(90)
    sem.backward(100)
    sem.forward(200)
    sem.right(90)
    sem.forward(100)
    sem.right(90)
    sem.forward(100)
    sem.right(90)
    sem.forward(100)
    sem.penup()
    sem.backward(200)
    sem.right(63)

    sem.pendown()
    sem.forward(111.8033989)
    sem.backward(111.8033989)
    sem.right(54)
    sem.forward(111.8033989)
    sem.backward(111.8033989)
    sem.left(27)
    sem.backward(100)
    sem.penup()
    sem.backward(50)
    sem.left(90)
    sem.forward(550)

    sem.color('white')
    sem.pendown()
    sem.forward(75)
    sem.left(90)
    sem.forward(150)
    sem.backward(75)
    sem.left(90)
    sem.forward(50)
    sem.penup()
    sem.forward(50)
    sem.pendown()
    sem.forward(50)
    sem.right(72)
    sem.forward(79.0569415)
    sem.backward(158.113883)
    sem.right(36)
    sem.forward(158.113883)
    sem.left(108)
    sem.penup()
    sem.forward(125)
    sem.left(90)
    sem.pendown()
    sem.forward(150)
    sem.left(90)
    sem.forward(50)
    sem.backward(100)
    sem.penup()
    sem.right(180)
    sem.forward(25)
    sem.right(90)
    sem.pendown()
    sem.forward(150)
    sem.backward(75)
    sem.left(90)
    sem.forward(75)
    sem.left(90)
    sem.forward(75)
    sem.backward(150)
    sem.right(90)
    sem.penup()
    sem.forward(25)
    sem.left(90)
    sem.pendown()
    sem.forward(150)
    sem.right(90)
    sem.forward(75)
    sem.penup()
    sem.right(90)
    sem.forward(75)
    sem.right(90)
    sem.forward(25)
    sem.pendown()
    sem.forward(50)
    sem.left(90)
    sem.forward(75)
    sem.left(90)
    sem.forward(75)
    sem.penup()
    sem.forward(25)
    sem.left(90)
    sem.pendown()
    sem.forward(150)
    sem.right(90)
    sem.forward(75)
    sem.right(90)
    sem.forward(75)
    sem.right(90)
    sem.forward(75)
    sem.left(135)
    sem.forward(106.0660172)
    sem.left(45)
    sem.penup()
    sem.forward(25)

    sem.left(90)
    sem.pendown()
    sem.forward(50)
    sem.backward(50)
    sem.right(90)
    sem.forward(75)
    sem.left(90)
    sem.forward(50)
    sem.left(58)
    sem.forward(90.13878189)
    sem.right(58)
    sem.forward(50)
    sem.right(90)
    sem.forward(75)
    sem.right(90)
    sem.forward(50)

    sem.color('#327506')
    sem.penup()
    sem.forward(150)
    sem.right(90)
    sem.forward(225)
    sem.left(90)
    sem.pendown()
    sem.forward(200)
    sem.right(90)
    sem.forward(100)
    sem.right(90)
    sem.forward(100)
    sem.right(90)
    sem.forward(100)

    sem.penup()
    sem.right(90)
    sem.forward(100)
    sem.left(90)
    sem.forward(25)
    sem.left(74)
    sem.pendown()
    sem.forward(223.6067977)
    sem.right(148)
    sem.forward(223.6067977)
    sem.backward(223.6067977 / 2)
    sem.right(106)
    sem.forward(60)

    sem.penup()
    sem.backward(135)
    sem.right(63)
    sem.pendown()
    sem.forward(111.8033989)
    sem.backward(111.8033989)
    sem.right(54)
    sem.forward(111.8033989)
    sem.backward(111.8033989)
    sem.left(27)
    sem.backward(100)

    turtle.done()


if __name__ == '__main__':
    pappadag()