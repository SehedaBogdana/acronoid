#план:
#імпортувати модулі
#задаємо розміри поля
#задаємо розміри ігрових штучок
#працюємо з функціями ігрового поля
#функція, яка буде відповідати за логіку гри
#функція, що буде відповідати за платформу
#функція життів


# Импортируем необходимые модули
import pgzrun
from actors import Ball, Life, Obstacle, Paddle # импортируем классы игровых актеров

# Определяем ширину и высоту игрового поля
WIDTH = 600
HEIGHT = 800

#----------------------------------------------------------------------------------------------------------
# Создаем объекты игровых актеров
paddle = Paddle(300, 785)  # ракетка с начальными координатами
ball = Ball(100, 300)  # мяч с начальными координатами


#----------------------------------------------------------------------------------------------------------
# Функция, отвечающая за отрисовку игрового поля
def draw():


#----------------------------------------------------------------------------------------------------------
# Функция, отвечающая за логику игры
def update():

#----------------------------------------------------------------------------------------------------------
# Функция, отвечающая за передвижение ракетки при движении мыши
def on_mouse_move(pos):
    paddle.x = pos[0]  # изменяем координату ракетки по оси X

#----------------------------------------------------------------------------------------------------------
# Функция, отвечающая за потерю жизни при вылете мяча
def lose_life():

pgzrun.go()
