# 조준점 관련 함수 오음
import math
import random

from pico2d import *

from config import *
from game_work import game_framework


def load_target(self):
    self.target_up = load_image(target_up_directory)
    self.target_down = load_image(target_down_directory)
    self.target_right = load_image(target_right_directory)
    self.target_left = load_image(target_left_directory)
    self.target_dot = load_image(target_dot_directory)
    self.not_target = load_image(target_x_directory)
    self.target_melee = load_image(target_melee_directory)


def draw_target(self):
    if self.weapon.weapon_type == 0:
        self.target_up.draw(self.p.mx, self.p.my + self.recoil + self.dis2, 60, 60)
        self.target_down.draw(self.p.mx, self.p.my - self.recoil - self.dis2, 60, 60)
        self.target_right.draw(self.p.mx + self.recoil + self.dis2, self.p.my, 60, 60)
        self.target_left.draw(self.p.mx - self.recoil - self.dis2, self.p.my, 60, 60)
    elif self.weapon.weapon_type == 1:  # 근접 무기는 조준점이 필요 없으므로 타겟을 사용하지 않는다.
        self.not_target.draw(self.p.mx, self.p.my, 120, 120)

    if self.target_dot_display_time > 0:
        self.target_dot.draw(self.tx, self.ty, 30, 30)

    if self.weapon.weapon_type == 1:
        if self.p.dir == 1:
            if self.weapon.melee == 'KNIFE':
                self.target_melee.composite_draw \
                    (0, '', self.p.x + self.p.camera_x + 200, -self.p.land_y + self.p.y + self.p.camera_y,
                     100, 150)

        elif self.p.dir == 0:
            if self.weapon.melee == 'KNIFE':
                self.target_melee.composite_draw \
                    (0, 'h', self.p.x + self.p.camera_x - 200, -self.p.land_y + self.p.y + self.p.camera_y,
                     100, 150)


def update_target(self):
    pps = PPS * game_framework.frame_time
    self.dis = math.sqrt((self.p.mx - WIDTH / 2) ** 2 + (self.p.y - self.p.my) ** 2)

    if self.recoil > 0:
        self.recoil -= pps / 7
    else:
        self.recoil = 0

    if self.dis < 0:  # 분산도가 0 밑으로 내려가지 않도록 한다.
        self.dis = 0

    if self.weapon.gun == 'SCAR_H':
        # empty randrange 방지를 위해 35를 더해야 함
        self.dis2 = self.dis / 20 + 35  # 나누는 숫자가 작을 수록 분산도가 커진다.
        if self.weapon.shoot:
            self.recoil += 20  # 총기마다 반동 수치가 달라 조준점이 벌어지는 정도가 다르다.

    if self.weapon.gun == 'M16':
        self.dis2 = self.dis / 30 + 35
        if self.weapon.shoot:
            self.recoil += 15

    if self.weapon.gun == 'MP44':
        self.dis2 = self.dis / 35 + 35
        if self.weapon.shoot:
            self.recoil += 30

    if self.target_dot_display_time > 0:
        self.target_dot_display_time -= pps / 3


def make_target_point(self):  # 이 함수에서 생성되는 좌표로 적 피격을 판정한다.
    if self.weapon.shoot:
        self.target_dot_display_time = TARGET_DOT_DISPLAY_TIME  # 해당 시간 동안 조준점 내부에 점이 보인다.
        self.tx = random.randint \
            (self.p.mx - int(self.recoil) - int(self.dis2) + 31, self.p.mx + int(self.recoil) + int(self.dis2) - 31)
        self.ty = random.randint \
            (self.p.my - int(self.recoil) - int(self.dis2) + 31, self.p.my + int(self.recoil) + int(self.dis2) - 31)
