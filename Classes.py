from pico2d import *
from Config import *


class Commando:
    global WIDTH, HEIGHT, JUMP_ACC, JUMP_ACC_SPEED

    def __init__(self):
        self.image = load_image('commando.png')
        self.x, self.y, self.Dir = WIDTH / 2, 250, 1
        self.mv_right, self.mv_left, self.mv_jump = False, False, False
        self.jump_acc = JUMP_ACC

    def draw(self):
        if self.Dir == 1:
            self.image.clip_draw(0, 0, 100, 100, self.x, self.y, 100, 100)
        elif self.Dir == 0:
            self.image.clip_composite_draw(0, 0, 100, 100, 0, 'h', self.x, self.y, 100, 100)

    def move(self):  # 좌우 이동
        if self.mv_right == True: self.x += 2
        if self.mv_left == True: self.x -= 2
        if self.mv_jump == True:  # 점프 후 착지하면
            self.y += self.jump_acc
            self.jump_acc -= JUMP_ACC_SPEED
            if self.jump_acc == -(JUMP_ACC + JUMP_ACC_SPEED):  # 점프 후 착지하면
                self.mv_jump = False
                self.jump_acc = JUMP_ACC
