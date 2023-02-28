from graphics import *  # импортируем библиотеку graphics

win = GraphWin("Окно для графики", 400, 400)  # создаём окно для графики размером 400 на 400 пикселей

# рисуем систему координат
obj = Line(Point(0, 200), Point(400, 200))
obj.setOutline("blue")
obj.draw(win)
obj = Line(Point(200, 0), Point(200, 400))
obj.setOutline("blue")
obj.draw(win)

# график y=x
obj = Line(Point(400, 400), Point(0, 0))
obj.setOutline("black")
obj.draw(win)

import random  # импортируем библиотеку random

# получаем случайные числа от 0 до 400 (по всему окну),
# используем их как координаты
for i in range(10000):
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    # print(x,y)

    if x < y:
        obj = Point(x, y)  # создаём точку в координатах (x, y)
        obj.setOutline("grey")
        obj.draw(win)  # отображаем точку в окне для графики

win.getMouse()  # ждём нажатия кнопки мыши
win.close()  # закрываем окно для графики
