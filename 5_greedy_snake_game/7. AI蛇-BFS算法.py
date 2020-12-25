"""Snake, classic arcade game.
Excercises
1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.
"""

import random
from random import randrange

# random.seed(0)
from turtle import *

from freegames import square, vector

s = 10
food = vector(0, 0)
snake = [vector(s, 0)]
aim = vector(0, -s)

aim_list = []


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def get_vis_dict(val=False):
    res = {}
    rng = range(-19, 20)
    for x in rng:
        for y in rng:
            res[(x * s, y * s)] = val
    return res


def get_food(snake):
    for _ in range(100):
        food = vector(randrange(-15, 15) * s,
                      randrange(-15, 15) * s)
        if food not in snake:
            return food
    return food


def move():
    # AI程序做的事情： 调整aim
    global aim,food
    head = snake[-1].copy()
    # ---------------------------------
    if not aim_list:
        vis: dict = get_vis_dict()
        pre: dict = get_vis_dict(None)
        queue = [(head.x, head.y)]
        while queue:
            top = queue.pop(0)
            if vector(*top) == food:
                parent = top
                path = []
                while parent:
                    path.insert(0, parent)
                    parent = pre[parent]
                for i in range(len(path) - 1):
                    aim_list.append(
                        vector(*path[i + 1]) -
                        vector(*path[i]))
            tx, ty = top
            children = [(tx - s, ty), (tx + s, ty),
                        (tx, ty - s), (tx, ty + s)]

            for child in children:
                if child in vis and vis[child] == False \
                        and vector(*child) not in snake:
                    pre[child] = top
                    vis[child] = True
                    queue.append(child)
    aim = aim_list.pop(0)
    # ---------------------------------
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, s - 1, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food=get_food(snake)
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, s - 1, 'black')

    square(food.x, food.y, s - 1, 'green')
    update()
    ontimer(move, 5)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
move()
done()
