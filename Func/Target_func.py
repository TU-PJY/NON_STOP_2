# 조준점 관련 함수 오음
from pico2d import *
from Env_variable import *
import math


def load_target(self):
    self.target_up = load_image(target_up_directory)
    self.target_down = load_image(target_down_directory)
    self.target_right = load_image(target_right_directory)
    self.target_left = load_image(target_left_directory)


def draw_target(target):
    target.target_up.draw(target.p.mx, target.p.my + target.recoil + target.dis, 60, 60)
    target.target_down.draw(target.p.mx, target.p.my - target.recoil - target.dis, 60, 60)
    target.target_right.draw(target.p.mx + target.recoil + target.dis, target.p.my, 60, 60)
    target.target_left.draw(target.p.mx - target.recoil - target.dis, target.p.my, 60, 60)


def cal_dis(target):
    if target.weapon.name == 'SCAR_H':  # 분산도 계산 파트, 나누는 숫자가 작을수록 분산도가 크다.
        target.dis = 35 + math.sqrt((target.p.mx - WIDTH / 2) ** 2 + (target.p.y - target.p.my) ** 2) / 20
    if target.dis < 0:
        target.dis = 0


def update_recoil(target):
    if target.weapon.shoot:  # 총 추가시 여기에 추가
        if target.weapon.name == 'SCAR_H':
            target.recoil += 20

    if target.recoil > 0:
        if target.reduce_delay == 0:
            target.recoil -= 1
            target.reduce_delay = RECOIL_REDUCE
        else:
            target.reduce_delay -= 1
