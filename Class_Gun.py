from pico2d import *
from Env_variable import *
from Class_Player import Player
import math


class Gun:
    def __init__(self, p):
        self.scar_right = load_image(scar_h_right_directory)
        self.scar_left = load_image(scar_h_left_directory)
        self.p = p
        self.deg_right, self.deg_left = 0, 0

    def draw(self):
        if GUN_NAME == 'SCAR_H':  # GUN_NAME에 따라 사용하는 총기가 달라진다.
            if self.p.dir == 1:
                self.scar_right.rotate_draw(self.deg_right, self.p.x, self.p.y - self.p.land_y, 170, 120)
            elif self.p.dir == 0:
                self.scar_left.rotate_draw(self.deg_left, self.p.x, self.p.y - self.p.land_y, 170, 120)

    def update(self):
        self.deg_right = math.atan2(self.p.my - self.p.y, self.p.mx - self.p.x)
        self.deg_left = math.atan2(self.p.my - self.p.y, self.p.mx - self.p.x)

    def handle_event(self, event):
        pass
