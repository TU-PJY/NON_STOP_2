from pico2d import *
from Env_variable import *
from Class_Player import Player
import math


class Gun:
    def __init__(self, p):
        self.scar_right = load_image(scar_h_right_directory)
        self.scar_left = load_image(scar_h_left_directory)
        self.p = p
        self.deg = 0
        self.trigger = False
        self.shoot = False
        self.shoot_delay = 0

    def draw(self):
        if GUN_NAME == 'SCAR_H':  # GUN_NAME에 따라 사용하는 총기가 달라진다.
            if self.p.dir == 1:
                self.scar_right.clip_composite_draw(0, 0, 150, 100, self.deg, '', self.p.x, self.p.y - 10 - self.p.land_y, 170, 120)
            elif self.p.dir == 0:
                self.scar_left.clip_composite_draw(0, 0, 150, 100, self.deg, 'h, v', self.p.x, self.p.y - 10 - self.p.land_y, 170, 120)

    def update(self):
        self.deg = math.atan2(self.p.my - self.p.y, self.p.mx - self.p.x)

        if self.trigger:
            if self.shoot_delay == 0:
                if GUN_NAME == 'SCAR_H':
                    self.shoot = True
                    self.shoot_delay = 65

            else:
                self.shoot = False
                self.shoot_delay -= 1

    def handle_event(self, event):
        pass
