"""Snake, classic arcade game.
Excercises
1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.
"""

from random import randrange
from turtle import *

from freegames import square, vector

s = 10
food = vector(0, 0)
snake = [vector(s, 0)]
aim = vector(0, -s)


# aim_list=[]

def change(x, y):
    "Change snake direction."
    if (aim.x * x < 0 or aim.y * y < 0):
        print("无效的方向改变")
        return
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    # AI程序做的事情： 调整aim
    global aim
    head = snake[-1].copy()
    dx, dy = food.x - head.x, food.y - head.y
    ax, ay = abs(dx), abs(dy)
    if ax > ay:
        aim = vector((dx / ax) * s, 0)
    else:
        aim = vector(0, (dy / ay) * s)
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, s - 1, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * s
        food.y = randrange(-15, 15) * s
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, s - 1, 'black')

    square(food.x, food.y, s - 1, 'green')
    update()
    ontimer(move, 20)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
move()
done()
