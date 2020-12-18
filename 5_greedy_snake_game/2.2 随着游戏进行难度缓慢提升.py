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
delta=190




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
    "Move snake forward one segment."
    global delta
    head = snake[-1].copy()
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
        delta*=0.95
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, s - 1, 'black')

    square(food.x, food.y, s - 1, 'green')
    update()
    ontimer(move, int(delta+10))


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(s, 0), 'Right')
onkey(lambda: change(-s, 0), 'Left')
onkey(lambda: change(0, s), 'Up')
onkey(lambda: change(0, -s), 'Down')
move()
done()
