from pico2d import *
from Config import *
import math


class Commando:
    global WIDTH, HEIGHT, JUMP_ACC, JUMP_ACC_SPEED

    def __init__(self):
        self.image = load_image(commando_image_directory)
        self.x, self.y, self.Dir = WIDTH / 2, 250, 1
        self.mv_right, self.mv_left, self.mv_jump = False, False, False
        self.jump_acc = JUMP_ACC
        self.rotate_right = 0
        self.rotate_left = 0
        self.distance = 0

    def draw(self):
        if self.Dir == 1:
            self.image.rotate_draw(math.pi * self.rotate_right / 360, self.x, self.y, 400, 400)
        elif self.Dir == 0:
            self.image.clip_composite_draw(0, 0, 128, 128, math.pi * self.rotate_left / 360, 'h', self.x, self.y, 400, 400)

    def move(self):  # 좌우 이동
        if self.mv_right and self.x <= WIDTH:
            self.x += 2
        if self.mv_left and self.x >= 0:
            self.x -= 2

    def mem_distance(self):  # 이동 거리를 측정 하여 배경 스크롤 여부를 결정
        if self.mv_right and self.distance <= 2048:
            self.distance += 2
        if self.mv_left and self.distance >= -2048:
            self.distance -= 2

    def jump(self):  # 점프
        if self.mv_jump:
            self.rotate_right += 0.3
            self.rotate_left -= 0.3
            self.y += self.jump_acc
            self.jump_acc -= JUMP_ACC_SPEED
            if self.jump_acc == -(JUMP_ACC + JUMP_ACC_SPEED):  # 점프 후 착지하면
                self.mv_jump = False
                self.jump_acc = JUMP_ACC
                self.rotate_right, self.rotate_left = 0, 0


class Land:
    global WIDTH

    def __init__(self):
        self.image = load_image(land_image_directory)
        self.x, self.y = WIDTH / 2, -50

    def draw(self):
        self.image.draw(self.x, self.y)

    def scroll_right(self, op):
        if op:
            self.x -= 2

    def scroll_left(self, op):
        if op:
            self.x += 2


class BackGround:
    global WIDTH, HEIGHT

    def __init__(self):
        self.image = load_image(bg_image_directory)
        self.x, self.y = WIDTH / 2, HEIGHT / 2 - 25

    def draw(self):
        self.image.draw(self.x, self.y)

    def scroll_right(self, op):
        if op:
            self.x -= 0.5

    def scroll_left(self, op):
        if op:
            self.x += 0.5
