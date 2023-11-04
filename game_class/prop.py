from pico2d import *

from config import *
from game_work import game_manager, game_framework


class Arrow:
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
        if game_framework.MODE == 'play':
            pps = PPS * game_framework.frame_time
            if self.p.mv_right:
                self.x -= self.p.speed * pps / 4
            elif self.p.mv_left:
                self.x += self.p.speed * pps / 4

            # 화살이 벽에 박힌다
            if not (self.x >= self.mp.playerToWallRight - 10 or self.x <= self.mp.playerToWallLeft + 10 or
                    self.y <= 190):
                self.x += math.cos(self.incline) * 8 * pps / 4
                self.y += math.sin(self.incline) * 8 * pps / 4
                self.y += self.acc * pps / 5
                self.acc -= 0.01 * pps / 5

                if self.dir == 1:
                    if self.deg > -90:
                        self.deg -= 0.0015 * pps / 5
                elif self.dir == 0:
                    if self.deg < 90:
                        self.deg += 0.0015 * pps / 5

                if self.y >= 2000:  # 너무 높이 올라가면 삭제
                    game_manager.remove_object(self)

            else:
                if self.y <= 190:
                    self.y = 190
                self.remove_timer -= pps / 3
                if self.remove_timer <= 0:
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


class BloodGun:
    def __init__(self, x, y, bdir, p):
        self.p = p
        self.image = load_image(blood_gun_directory)
        self.x = x
        self.y = y
        self.dir = bdir
        self.frame = 0

    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw\
                (int(self.frame) * 42, 0, 42, 42, 0, 'h', self.x + self.p.efx - 75, self.y + self.p.efy, 150, 150)
        elif self.dir == 0:
            self.image.clip_composite_draw\
                (int(self.frame) * 42, 0, 42, 42, 0, '', self.x + self.p.efx + 75, self.y + self.p.efy, 150, 150)

    def update(self):
        pps = PPS * game_framework.frame_time

        if self.p.mv_right:
            self.x -= self.p.speed * pps / 4
        elif self.p.mv_left:
            self.x += self.p.speed * pps / 4

        self.frame = (self.frame + pps / 50) % 8
        if self.frame >= 7:
            game_manager.remove_object(self)

    def handle_event(self):
        pass


class BloodMelee:
    def __init__(self, x, y, bdir, p):
        self.p = p
        self.image = load_image(blood_melee_directory)
        self.x = x
        self.y = y
        self.dir = bdir
        self.frame = 0

    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw\
                (int(self.frame) * 37, 0, 37, 37, 0, 'h', self.x + self.p.efx, self.y + self.p.efy + 50, 130, 130)
        elif self.dir == 0:
            self.image.clip_composite_draw\
                (int(self.frame) * 37, 0, 37, 37, 0, '', self.x + self.p.efx, self.y + self.p.efy + 50, 130, 130)

    def update(self):
        pps = PPS * game_framework.frame_time

        if self.p.mv_right:
            self.x -= self.p.speed * pps / 4
        elif self.p.mv_left:
            self.x += self.p.speed * pps / 4

        self.frame = (self.frame + pps / 50) % 10
        if self.frame >= 9:
            game_manager.remove_object(self)

    def handle_event(self):
        pass
