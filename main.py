import pgzrun
from new_vector import Vector
from pgzero.actor import Actor

WIDTH = 800
HEIGHT = 800
x_speed = -7
y_speed = -7
hearts = [Actor("heart", center=(30, 50)), Actor("heart", center=(80, 50)), Actor("heart", center=(130, 50))]


class Obstacle(Actor):
    def __init__(self, x, y, **kwargs): # инициализирует параметры преграды
        super().__init__("obstacle.png", **kwargs) # задает изображение преграды
        self.x = x # задает х координату преграды
        self.y = y # задает у координату преграды
        self.radius = self.width / 2 # задает радиус преграды

class Ball:
    def __init__(self, vector: Vector):
        self.position = vector
        self.x_speed = -7 # задает скорость движения мяча по х координате
        self.y_speed = -7
    def stop(self): # останавливает движение мяча
        self.x_speed = 0 # останавливает движение по х координате
        self.y_speed = 0

class Puddle:
    def __init__(self, vector: Vector, size: Vector):
        self.position = vector
        self.size = size


puddle1 = Puddle(Vector(100, 770), Vector(200, 30))
circle = Ball(Vector(400, 400))
# our_obstacles = [Actor("obstacle", center=(400, 400))]
obstacles = [Obstacle(x, i * 100) for i in range(1, 4)
             for x in range(50, WIDTH, 100)]  # список препятствий
NUMBER_OF_OBSTACLES = len(obstacles)


def draw():
    screen.clear()
    screen.fill("peru")
    screen.draw.filled_circle((circle.position.x, circle.position.y), 25, "mediumblue")
    screen.draw.filled_rect((Rect((puddle1.position.x, puddle1.position.y), (puddle1.size.x, puddle1.size.y))), "black")
    for heart in hearts:
        heart.draw()
    if not hearts:
        screen.draw.text("GAME OVER!", (200, 400), color='black', fontsize=100)
    for obstacle in obstacles:
        obstacle.draw()
    if not obstacles:
        screen.draw.text("YOU WON!", (200, 400), color="black", fontsize=100)


def update(dt):
    global x_speed
    circle.position.x = circle.position.x + x_speed
    if circle.position.x > (WIDTH - 25) or circle.position.x < 25:
        x_speed = - x_speed
    global y_speed
    circle.position.y = circle.position.y + y_speed
    if circle.position.y <= 770 <= (circle.position.y + 25) and puddle1.position.x <= circle.position.x <= (puddle1.position.x + 200) or circle.position.y < 25:
        y_speed = -y_speed
    if circle.position.y > 800:
        hearts.pop()
        circle.position = Vector(100, 100)
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

def on_mouse_move(pos):
    new_x = pos[0]
    if new_x > WIDTH - puddle1.size.x:
        new_x = WIDTH - puddle1.size.x
    puddle1.position.x = new_x


pgzrun.go()
