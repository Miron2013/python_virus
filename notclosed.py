import pyautogui
import time
import pyperclip
import keyboard

time.sleep(5)

def spam(text: str, amount: int):
    pyperclip.copy(text)
    for _ in range(amount):
        time.sleep(0.2)
        keyboard.press_and_release('ctrl + v')
        pyautogui.press("enter")
spam("Вы заражены вирусом", 10000)

import turtle
from math import tan, sqrt, pi

def prepare(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()

def draw_polygon(num_sides, side_length):
    angle = 360.0 / num_sides
    for i in range(num_sides):
        turtle.forward(side_length)
        turtle.right(angle)
    turtle.end_fill()

def calc_s(num_sides, side_length):
    return num_sides * side_length ** 2 / (4 * tan(pi/num_sides))

def calc_side(square):
    return sqrt(4 * square * tan(pi/num_sides) / num_sides)

turtle.hideturtle()
turtle.speed(10)

colors = ['red', 'green', 'blue', 'cyan', 'magenta', 'black', 'yellow', 'pink', 'brown']
xcoords = [0, 150, -150, 150, -150, 270, -270, 270, -270]
ycoords = [0, 150, -150, -150, 150, 270, -270, -270, 270]

squares = []
numsides = []
for i in range(9):
    num_sides = i + 3
    square = round(calc_s(num_sides, 100), 2)
    side_length = round(calc_side(10000), 3)
    squares.append(square)
    numsides.append(num_sides)
    print("Углов:", num_sides, "была площадь:", square, "стала длина грани:", side_length,
          "изменение в", round(side_length/100, 2), "раз")
    prepare(xcoords[i], ycoords[i], colors[i])
    draw_polygon(num_sides, side_length)

turtle.exitonclick()
print("Список количество углов:", numsides, end="")
print("Список площади:", squares)

from turtle import *
color('blue')
for i in range(1,100,6):
    up()
    goto(i*2,0)
    down()
    circle(i)
