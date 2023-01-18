import pgzrun
from new_vector import Vector
from pgzero.actor import Actor
import random
WIDTH = 800
HEIGHT = 800
x_speed = -10
y_speed = -7
hearts = [Actor("heart", center=(30, 50)), Actor("heart", center=(80, 50)), Actor("heart", center=(130, 50))]
coloured_box_list = ["element_blue_rectangle_glossy.png", "element_green_rectangle_glossy.png", "element_red_rectangle_glossy.png"]
# x_heart = 400


class Obstacle2(Actor): #клас преград
    def __init__(self, x, y, i, **kwargs):  # инициализирует параметры преграды
        super().__init__(coloured_box_list[i], **kwargs)
        self.x = x  # задает х координату преграды
        self.y = y  # задает у координату преграды
        self.radius = self.width / 2  # задает радиус преграды
        self.hp = 100  # задает здоровье преграды


class Obstacle(Actor):
    def __init__(self, x, y, **kwargs): # инициализирует параметры преграды (метод)
        super().__init__("obstacle.png", **kwargs)  # super функція, яка звертається до класу, від якого наслідуєтья теперішній
        self.x = x
        self.y = y
        self.radius = self.width / 2


class Ball:
    def __init__(self, vector: Vector):
        self.position = vector
        self.x_speed = -10
        self.y_speed = -7


class Paddle:
    def __init__(self, vector: Vector, size: Vector):
        self.position = vector
        self.size = size


class Bonus:
    def __init__(self, position: Vector):
        self.position = position
        self.velocity = Vector(0, 4)

    def draw(self):
        screen.draw.filled_circle((self.position.x, self.position.y), 25, "lightgreen")

    def move(self):
        self.position += self.velocity

#
# class Bonus_life:
#     def __init__(self):
#         self.actor = Actor('heart.png', center=(random.randint(100, 600), 0))
#
#     def update(self):
#         global hearts, x_heart
#         self.actor.y = self.actor.y + 5
#         if abs(self.actor.x - paddle.position.x) < 40 and abs(self.actor.y - paddle.position.y) < 10:
#             x_heart = x_heart + 25
#             hearts.append(x_heart)
#             self.actor.y = -500
#             self.actor.x = -20
#         if self.actor.x == HEIGHT:
#             self.actor.y = -500
#             self.actor.x = -20
#         if self.actor.x == -20 and random.randint(0, 10000) == 1:
#             self.actor.x = random.randint(100, 600)
#             self.actor.y = 0
#
#     def draw(self):
#         self.actor.draw()


bonuses = []
paddle = Paddle(Vector(100, 770), Vector(200, 30))
circle = Ball(Vector(500, 500))
obstacles = [Obstacle(x, i * 100) for i in range(1, 3)  # генератор списка
             for x in range(45, WIDTH, 100)]  # список препятствий 45 це координати по x з якої у нас починається перещкоди
#  WIDTH і до ширини , 100 це ширина між шариками
obstacles2 = [Obstacle2(x, i * 100, random.randint(0, 2)) for i in range(3, 5) for x in range(50, WIDTH, 100)]
# bonus_hearts = Bonus_life()

def draw():
    screen.clear()
    screen.fill("peru")
    screen.draw.filled_circle((circle.position.x, circle.position.y), 25, "mediumblue")
    screen.draw.filled_rect((Rect((paddle.position.x, paddle.position.y), (paddle.size.x, paddle.size.y))), "black")
    for heart in hearts:
        heart.draw()
    if not hearts:
        screen.draw.text("GAME OVER!", (200, 400), color='black', fontsize=100)

    for obstacle in obstacles:
        obstacle.draw()
    if not obstacles and not obstacles2:
        screen.draw.text("YOU WON!", (200, 400), color="black", fontsize=100)

    for bonus in bonuses:
        bonus.draw()

    for obstacle2 in obstacles2:
        obstacle2.draw()
    # for bonus_heart in hearts:
    #     bonus_heart.draw()


def update(dt):
    global x_speed
    circle.position.x = circle.position.x + x_speed
    if circle.position.x > (WIDTH - 25) or circle.position.x < 25:
        x_speed = - x_speed

    global y_speed
    circle.position.y = circle.position.y + y_speed
    if circle.position.y <= 770 <= (circle.position.y + 25) and paddle.position.x <= circle.position.x <= (paddle.position.x + paddle.size.x) or circle.position.y < 25:
        y_speed = -y_speed
    if circle.position.y > 800:
        hearts.pop()
        circle.position = Vector(600, 600)
    if not hearts:
        x_speed = 0
        y_speed = 0
        circle.position = Vector(-100, -100)
    for obstacle in obstacles:
        if ((circle.position.x - obstacle.x) ** 2 + (circle.position.y - obstacle.y) ** 2) ** .5 < 25 + obstacle.radius:
            obstacles.remove(obstacle)
            if (circle.x_speed < 0 and circle.position.x <= obstacle.x) or (circle.x_speed > 0 and circle.position.x >= obstacle.x) or (circle.x_speed < 0 and circle.position.x >= obstacle.x) or (circle.x_speed < 0 and circle.position.x <= obstacle.x):
                x_speed = -x_speed
            if (circle.y_speed < 0 and circle.position.y <= obstacle.y) or (circle.y_speed > 0 and circle.position.y >= obstacle.y) or (circle.y_speed < 0 and circle.position.y <= obstacle.y) or (circle.y_speed < 0 and circle.position.y >= obstacle.y):
                y_speed = -y_speed
    if not obstacles:
        x_speed = 0
        y_speed = 0
        circle.position = Vector(-100, -100)
    if random.random() < 0.001:
        position = Vector(random.randint(0, WIDTH), 0)
        bonuses.append(Bonus(position))
    for bonus in bonuses:
        bonus.move()
        bonus_y_on_puddle = (bonus.position.y <= (HEIGHT - 30) <= (bonus.position.y + 25))
        bonus_x_on_puddle = (paddle.position.x <= bonus.position.x <= (paddle.position.x + paddle.size.x))
        if bonus_y_on_puddle and bonus_x_on_puddle:
            paddle.size = Vector(300, 30)
            bonuses.remove(bonus)
            clock.schedule_unique(make_paddle_smaller, 5.0)
    for obstacle2 in obstacles2:
        if obstacle2.colliderect(Rect((circle.position.x - 25, circle.position.y - 25), (50, 50))) and obstacle2.image == "element_blue_rectangle_glossy.png":
            obstacles2.remove(obstacle2)
            y_speed = -y_speed
        if obstacle2.colliderect(Rect((circle.position.x - 25, circle.position.y - 25), (50, 50))) and (obstacle2.image == "element_green_rectangle_glossy.png" or obstacle2.image == "element_green_rectangle_glossy_damaged.png"):
            if obstacle2.hp == 100:
                obstacle2.image = "element_green_rectangle_glossy_damaged.png"
                obstacle2.hp -= 50
            elif obstacle2.hp == 50:
                obstacles2.remove(obstacle2)
            y_speed = -y_speed
        if obstacle2.colliderect(Rect((circle.position.x - 25, circle.position.y - 25), (50, 50))) and (obstacle2.image == "element_red_rectangle_glossy.png" or obstacle2.image == "element_red_rectangle_glossy_damaged.png" or obstacle2.image == "element_red_rectangle_glossy_damaged2.png"):
            if obstacle2.hp == 100:
                obstacle2.image = "element_red_rectangle_glossy_damaged.png"
                obstacle2.hp -= 5
            elif obstacle2.hp == 95:
                obstacle2.image = "element_red_rectangle_glossy_damaged2.png"
                obstacle2.hp -= 5
            elif obstacle2.hp == 90:
                obstacles2.remove(obstacle2)
            y_speed = -y_speed
    # bonus_hearts.update()


def make_paddle_smaller():
    paddle.size.x = 200


def on_mouse_move(pos):
    new_x = pos[0]
    if new_x > WIDTH - paddle.size.x:
        new_x = WIDTH - paddle.size.x
    paddle.position.x = new_x


pgzrun.go()
