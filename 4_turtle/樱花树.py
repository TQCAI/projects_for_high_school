import turtle as T
import random
import time

sleep_time = 1e-4
# 选取颜色的网站 ：  https://trinket.io/docs/colors
# 画布背景
canvas_bg = '#F5DEB3'
# 树干颜色
trunk_color = '#8B4513'
# 花瓣颜色1 （白色）
petal_color1 = "#F8F8FF"
# 花瓣颜色2 （粉色）
petal_color2 = "lightcoral"


# 画樱花的躯干(60,t)
def Tree(branch, t):
    # 修改枝丫生长的时间
    time.sleep(sleep_time)
    if branch <= 3:
        return
    if 8 <= branch <= 12:
        if random.randint(0, 2) == 0:
            t.color(petal_color1)
        else:
            t.color(petal_color2)
        t.pensize(branch / 3)
    elif branch < 8:
        if random.randint(0, 1) == 0:
            t.color(petal_color1)
        else:
            t.color(petal_color2)
        t.pensize(branch / 2)
    else:
        t.color(trunk_color)
        t.pensize(branch / 10)
    t.forward(branch)
    # a: 随机数，控制转向
    a = 1.5 * random.random()
    # b: 随机数，控制枝丫的宽度
    b = 1.5 * random.random()
    # 递归绘图
    t.right(20 * a)
    Tree(branch - 10 * b, t)
    t.left(40 * a)
    Tree(branch - 10 * b, t)
    # 还原状态
    t.right(20 * a)
    t.up()
    t.backward(branch)
    t.down()


# 掉落的花瓣
def Petal(m, t):
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        t.color(petal_color2)
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)


# 绘图区域
t = T.Turtle()
# 画布大小
w = T.Screen()
t.hideturtle()  # 隐藏画笔
t.getscreen().tracer(5, 0)
w.screensize(bg=canvas_bg)  # 画布背景色
t.left(90)
t.up()
t.backward(150)
t.down()

# 画樱花的躯干
Tree(60, t)
# 掉落的花瓣
Petal(200, t)
w.exitonclick()
