from Class_Player import Player
from pico2d import *
from Env_variable import *
import math


class Target:
    def __init__(self, p):
        self.p = p
        self.dis = 0
        self.recoil = 0
        self.target_up = load_image(target_up_directory)
        self.target_down = load_image(target_down_directory)
        self.target_right = load_image(target_right_directory)
        self.target_left = load_image(target_left_directory)

    def draw(self):
        self.target_up.draw(self.p.mx, self.p.my + self.recoil + self.dis, 60, 60)
        self.target_down.draw(self.p.mx, self.p.my - self.recoil - self.dis, 60, 60)
        self.target_right.draw(self.p.mx + self.recoil + self.dis, self.p.my, 60, 60)
        self.target_left.draw(self.p.mx - self.recoil - self.dis, self.p.my, 60, 60)

    def update(self):
        if self.dis < 0:
            self.dis = 0
        if GUN_NAME == 'SCAR_H':  # 분산도 계산 파트, 나누는 숫자가 작을수록 분산도가 크다.
            self.dis = 35 + math.sqrt((self.p.mx - WIDTH / 2)**2 + (self.p.y - self.p.my)**2) / 15

    def handle_event(self, event):
        pass
