# 조준점 관련 함수 오음
from pico2d import *
from config import *
import math
import random


def load_target(self):
    self.target_up = load_image(target_up_directory)
    self.target_down = load_image(target_down_directory)
    self.target_right = load_image(target_right_directory)
    self.target_left = load_image(target_left_directory)
    self.target_dot = load_image(target_dot_directory)


def draw_target(target):
    target.target_up.draw(target.p.mx, target.p.my + target.recoil + target.dis2, 60, 60)
    target.target_down.draw(target.p.mx, target.p.my - target.recoil - target.dis2, 60, 60)
    target.target_right.draw(target.p.mx + target.recoil + target.dis2, target.p.my, 60, 60)
    target.target_left.draw(target.p.mx - target.recoil - target.dis2, target.p.my, 60, 60)

    if target.target_dot_display_time > 0:
        target.target_dot.draw(target.tx, target.ty, 30, 30)


def update_target(target):
    target.dis = math.sqrt((target.p.mx - WIDTH / 2) ** 2 + (target.p.y - target.p.my) ** 2)

    if target.recoil > 0:
        if target.reduce_delay == 0:
            target.recoil -= 1
            target.reduce_delay = RECOIL_REDUCE
        else:
            target.reduce_delay -= 1

    if target.dis < 0:
        target.dis = 0

    if target.weapon.gun == 'SCAR_H':
        target.dis2 = 35 + target.dis / 20
        if target.weapon.shoot:
            target.recoil += 18

    if target.target_dot_display_time > 0:
        target.target_dot_display_time -= 1


def make_target_point(target):  # 이 함수에서 생성되는 좌표로 적 피격을 판정한다.
    if target.weapon.shoot:
        global x, y, type
        target.target_dot_display_time = TARGET_DOT_DISPLAY_TIME
        target.tx = random.randint\
            (target.p.mx - target.recoil - int(target.dis2) + 31, target.p.mx + target.recoil + int(target.dis2) - 31)
        target.ty = random.randint\
            (target.p.my - target.recoil - int(target.dis2) + 31, target.p.my + target.recoil + int(target.dis2) - 31)
