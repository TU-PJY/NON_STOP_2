from pico2d import *
from config import *
from game_work import game_manager
import math


class Prob:
    def __init__(self, p, mp, x, y, incline, dir):
        self.x = x
        self.y = y
        self.incline = incline
        self.p = p
        self.mp = mp
        self.dir = dir
        self.acc = 0
        self.deg = self.incline
        self.remove_timer = 300

        if self.dir == 0:
            self.arrow_left = load_image(arrow_left_directory)
        elif self.dir == 1:
            self.arrow_right = load_image(arrow_right_directory)

    def update(self):
        if self.p.mv_right:
            self.x -= self.p.speed
        elif self.p.mv_left:
            self.x += self.p.speed

        # 화살이 벽에 박힌다
        if not (self.x >= self.mp.playerToWallRight - 10 or self.x <= self.mp.playerToWallLeft + 10 or
                self.y <= 190):
            self.x += math.cos(self.incline) * 8
            self.y += math.sin(self.incline) * 8
            self.y += self.acc
            self.acc -= 0.01

            if self.dir == 1:
                if self.deg > -90:
                    self.deg -= 0.0015
            elif self.dir == 0:
                if self.deg < 90:
                    self.deg += 0.0015

        else:
            if self.y <= 190:
                self.y = 190
            self.remove_timer -= 1
            if self.remove_timer == 0:
                game_manager.remove_object(self)

    def draw(self):
        if self.dir == 0:
            self.arrow_left.clip_composite_draw \
                (0, 0, 128, 128, self.deg, 'h', self.x + self.p.efx, self.y + self.p.efy, 400, 400)
        elif self.dir == 1:
            self.arrow_right.clip_composite_draw \
                (0, 0, 128, 128, self.deg, '', self.x + self.p.efx, self.y + self.p.efy, 400, 400)

    def handle_event(self):
        pass
