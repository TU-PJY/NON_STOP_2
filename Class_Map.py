from pico2d import load_image
from Env_variable import *


class BackGround:  # 배경
    global WIDTH, HEIGHT

    def __init__(self, p):
        self.image = load_image(bg_image_directory)
        self.x, self.y = WIDTH / 2, HEIGHT / 2 - 25
        self.p = p

    def draw(self):
        self.image.draw(self.x, self.y - self.p.land_y)

    def update(self):
        if self.p.mv_right:
            self.x -= MOVE_SPEED / 4

        elif self.p.mv_left:
            self.x += MOVE_SPEED / 4

    def handle_event(self, event):
        pass


class Land:  # 땅
    global WIDTH

    def __init__(self, p):
        self.image = load_image(land_image_directory)
        self.x, self.y = WIDTH / 2, -50
        self.p = p

    def draw(self):
        self.image.draw(self.x, self.y - self.p.land_y, 4096, 512)

    def update(self):
        if self.p.mv_right:
            self.x -= MOVE_SPEED
            if self.x + 2048 <= WIDTH / 2:
                self.p.mv_right = False
                self.x += MOVE_SPEED

        elif self.p.mv_left:
            self.x += MOVE_SPEED
            if self.x - 2048 >= WIDTH / 2:
                self.p.mv_left = False
                self.x -= MOVE_SPEED

    def handle_event(self, event):
        pass


class Wall:  # 벽
    global HEIGHT, WIDTH

    def __init__(self, p):
        self.image = load_image(wall_image_directory)
        self.p = p
        self.x2 = WIDTH / 2 + 2048 + 640
        self.x1 = WIDTH / 2 - 2048 - 640
        self.y = HEIGHT / 2

    def draw(self):
        self.image.draw(self.x1, self.y - self.p.land_y, 1280, 1920)
        self.image.draw(self.x2, self.y - self.p.land_y, 1280, 1920)

    def update(self):
        if self.p.mv_right:
            self.x1 -= MOVE_SPEED
            self.x2 -= MOVE_SPEED

        elif self.p.mv_left:
            self.x1 += MOVE_SPEED
            self.x2 += MOVE_SPEED

    def handle_event(self, event):
        pass
