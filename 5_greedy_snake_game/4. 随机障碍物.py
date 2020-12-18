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
times = vector(200, 0)
delta_speed = 25


def change(x, y):
    "Change snake direction."
    if (aim.x * x < 0 or aim.y * y < 0):
        print("后退减速")
        times.x += delta_speed
        return
    if (aim.x == x and aim.y == y):
        print("前进加速")
        times.x = max(10, times.x - delta_speed)
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def get_obstacles():
    obstacles=[]
    for i in range(5):
        while True:
            obstacle = vector(
                randrange(-15, 15) * s,
                randrange(-15, 15) * s,
            )
            if obstacle in snake or (obstacle.x==food.x and obstacle.y==food.y):
                pass
            else:
                break
        obstacles.append(obstacle)
    return obstacles

obstacles = get_obstacles()  # 增加障碍物向量


def move():
    "Move snake forward one segment."
    global obstacles
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake or head in obstacles:
        square(head.x, head.y, s - 1, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * s
        food.y = randrange(-15, 15) * s
        obstacles = get_obstacles()
        # times.x = 200  # 注释掉这行代码， 蛇吃食物后速度不再还原
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, s - 1, 'black')

    for obstacle in obstacles:
        square(obstacle.x, obstacle.y, s - 1, 'red')

    square(food.x, food.y, s - 1, 'green')
    update()
    # ontimer(move,200- times.x)
    ontimer(move, times.x)


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
