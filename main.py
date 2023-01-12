import pgzrun
from new_vector import Vector
from pgzero.actor import Actor

WIDTH = 800
HEIGHT = 800
b = 8
a = 5
hearts = [Actor("heart", center=(30, 50)), Actor("heart", center=(80, 50)), Actor("heart", center=(130, 50))]
size_heart = len(hearts)


class Ball:
    def __init__(self, vector: Vector):
        self.position = vector


class Puddle:
    def __init__(self, vector: Vector, size: Vector):
        self.position = vector
        self.size = size


puddle1 = Puddle(Vector(100, 770), Vector(200, 30))

circle = Ball(Vector(100, 25))


def draw():
    global size_heart
    screen.clear()
    screen.fill("peru")
    screen.draw.filled_circle((circle.position.x, circle.position.y), 25, "darkred")
    screen.draw.filled_rect((Rect((puddle1.position.x, puddle1.position.y), (puddle1.size.x, puddle1.size.y))), "black")
    for heart in hearts:
        heart.draw()
    if circle.position.y > 800:
        size_heart -= 1


def update(dt):

    # # b рух кульки по вертикалі
    global size_heart
    global a
    circle.position.x = circle.position.x + a
    if circle.position.x > (WIDTH - 25) or circle.position.x < 25:
        a = - a
    global b
    circle.position.y = circle.position.y + b
    if circle.position.y <= 770 <= (circle.position.y + 25) and puddle1.position.x <= circle.position.x <= (puddle1.position.x + 200) or circle.position.y < 25:
        b = -b
    if circle.position.y > 800:
        hearts.pop()
        circle.position = Vector(100, 100)

    #     size_heart -= 1

# по горизонталі x pos[0]
# по вертикалі y pos[1]


def on_mouse_move(pos):
    new_x = pos[0]
    if new_x > WIDTH - puddle1.size.x:
        new_x = WIDTH - puddle1.size.x
    puddle1.position.x = new_x
    print(puddle1.position)


pgzrun.go()
