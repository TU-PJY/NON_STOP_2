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
        self.simulate = True  # True일 동안 움직임

        if self.dir == 0:
            self.arrow_left = load_image(arrow_left_directory)
        elif self.dir == 1:
            self.arrow_right = load_image(arrow_right_directory)

    def update(self):
        pps = PPS * game_framework.frame_time
        if game_framework.MODE == 'play':
            if self.p.mv_right:
                self.x -= self.p.speed * pps / 4
            elif self.p.mv_left:
                self.x += self.p.speed * pps / 4

            # 화살이 벽에 박힌다
            if self.simulate:
                self.x += math.cos(self.incline) * 6 * pps / 4
                self.y += math.sin(self.incline) * 6 * pps / 4
                self.y += self.acc * pps / 4
                self.acc -= 0.01 * pps / 4

                if self.dir == 1:
                    self.deg -= 0.002 * pps / 4
                elif self.dir == 0:
                    self.deg += 0.002 * pps / 4

                # 화살이 벽에 박히면
                if self.x >= self.mp.playerToWallRight - 10 or self.x <= self.mp.playerToWallLeft + 10 or self.y <= 190:
                    self.simulate = False  # 움직임을 멈춘다

                if self.y >= 2000:  # 너무 높이 올라가면 삭제
                    game_manager.remove_object(self)

            else:
                if self.y <= 190:
                    self.y = 190
                self.remove_timer -= pps / 3
                if self.remove_timer <= 0:
                    game_manager.remove_object(self)

    def draw(self):
        x = self.x + self.p.ex
        y = self.y + self.p.ey
        if self.dir == 0:
            self.arrow_left.clip_composite_draw \
                (0, 0, 128, 128, self.deg, 'h', x, y, 400, 400)
        elif self.dir == 1:
            self.arrow_right.clip_composite_draw \
                (0, 0, 128, 128, self.deg, '', x, y, 400, 400)

    def handle_event(self):
        pass
