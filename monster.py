# from func.monster_manager import *
from pico2d import *
from Env_variable import *


class Monster:
    def __init__(self, p, weapon, target, x, y, speed, hp, type):
        self.type1 = load_image(type1_directory)
        self.p = p
        self.weapon = weapon
        self.target = target
        self.type = type
        self.x, self.y = x, y
        self.speed = speed
        self.dir = 0
        self.hp = hp

        self.is_attack = False
        self.is_hit = False

    def draw(self):
        if self.type == 1:
            if self.dir == 0:
                self.type1.clip_composite_draw(0, 0, 64, 64, 0, '', self.x + self.p.efx, self.y + self.p.efy, 250, 250)
            elif self.dir == 1:
                self.type1.clip_composite_draw(0, 0, 64, 64, 0, 'h', self.x + self.p.efx, self.y + self.p.efy, 250, 250)

    def update(self):
        self.dir = 1 if self.p.x > self.x else 0

        if self.dir == 0:
            self.x -= self.speed
        elif self.dir == 1:
            self.x += self.speed

        if self.p.mv_right:
            self.x -= self.p.speed
        elif self.p.mv_left:
            self.x += self.p.speed

    def handle_events(self):
        pass
