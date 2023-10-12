from pico2d import load_image
from Config import *


class Land:
    global WIDTH

    def __init__(self, p):
        self.image = load_image(land_image_directory)
        self.x, self.y = WIDTH / 2, -50
        self.p = p

    def draw(self):
        self.image.draw(self.x, self.y, 4096, 512)

    def update(self):
        if self.p.mv_right:
            self.x -= 2
            if self.x + 2048 <= WIDTH / 2:
                self.p.mv_right = False
                self.x += 2

        elif self.p.mv_left:
            self.x += 2
            if self.x - 2048 >= WIDTH / 2:
                self.p.mv_left = False
                self.x -= 2

    def handle_event(self, event):
        pass


class BackGround:
    global WIDTH, HEIGHT

    def __init__(self, p, wall):
        self.image = load_image(bg_image_directory)
        self.x, self.y = WIDTH / 2, HEIGHT / 2 - 25
        self.p = p
        self.wall = wall

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if self.p.mv_right:
            self.x -= 0.5
        elif self.p.mv_left:
            self.x += 0.5

        print(self.wall.x2 - 640)
    def handle_event(self, event):
        pass


class Wall:
    global HEIGHT, WIDTH

    def __init__(self, p):
        self.image = load_image(wall_image_directory)
        self.p = p
        self.x2 = WIDTH / 2 + 2048 + 640
        self.x1 = WIDTH / 2 - 2048 - 640
        self.y = HEIGHT / 2

    def draw(self):
        self.image.draw(self.x1, self.y, 1280, 1920)
        self.image.draw(self.x2, self.y, 1280, 1920)

    def update(self):
        if self.p.mv_right:
            self.x1 -= 2
            self.x2 -= 2
            if self.x2 - 640 <= WIDTH / 2:
                self.x1 += 2
                self.x2 += 2
        elif self.p.mv_left:
            self.x1 += 2
            self.x2 += 2
            if self.x1 + 640 >= WIDTH / 2:
                self.x1 -= 2
                self.x2 -= 2

    def handle_event(self, event):
        pass