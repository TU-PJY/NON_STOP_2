# from func.monster_manager import *
from pico2d import *
from Env_variable import *


class Monster:
    def __init__(self, p, weapon, target, x, y, speed, hp, frame, fdelay, type):
        self.type1 = load_image(type1_directory)
        self.p = p
        self.weapon = weapon
        self.target = target
        self.type = type
        self.x, self.y = x, y
        self.hp = hp
        self.speed = speed
        self.frame = frame
        self.fdelay = fdelay
        self.atk_delay = 0

        self.dir = 0
        self.attack_motion_time = 0  # 해당 시간동안 공격 스파리아트를 보여준다.

        self.is_attack = False
        self.is_hit = False

    def draw(self):
        if self.type == 1:
            if self.dir == 0:
                self.type1.clip_composite_draw((self.frame * 64), 0, 64, 64, 0, '', self.x + self.p.efx, self.y + self.p.efy, 250, 250)
            elif self.dir == 1:
                self.type1.clip_composite_draw((self.frame * 64), 0, 64, 64, 0, 'h', self.x + self.p.efx, self.y + self.p.efy, 250, 250)
            draw_rectangle(self.x - 50 + self.p.efx, self.y + 50 + self.p.efy, self.x + 50 + self.p.efx, self.y - 70 + self.p.efy)

    def update(self):
        self.dir = 1 if self.p.x > self.x else 0
        if self.type == 1:
            if self.p.x - 90 <= self.x <= self.p.x + 90 and self.p.y - 200 <= self.y - 20 <= self.p.y + 200:
                self.is_attack = True
            else:
                self.is_attack = False

        if not self.is_attack and self.attack_motion_time == 0:
            if self.dir == 0:
                self.x -= self.speed
            elif self.dir == 1:
                self.x += self.speed

        if self.p.mv_right:
            self.x -= self.p.speed
        elif self.p.mv_left:
            self.x += self.p.speed

        if not self.is_attack and self.attack_motion_time == 0:
            if self.fdelay == 0:
                self.frame = (self.frame + 1) % 2
                self.fdelay = 70
            else:
                self.fdelay -= 1

        elif self.is_attack:
            if self.atk_delay == 0:
                self.attack_motion_time = 50
                self.atk_delay = 150

            if self.attack_motion_time > 0:
                self.frame = 2
            else:
                self.frame = 1

        if self.attack_motion_time > 0:
            self.attack_motion_time -= 1

        if self.atk_delay > 0:
            self.atk_delay -= 1

    def handle_events(self):
        pass
