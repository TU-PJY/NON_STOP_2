import random

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
        pps = game_framework.pps
        if game_framework.MODE == 'play':
            if self.p.mv_right:
                self.x -= self.p.speed * pps / 4
            elif self.p.mv_left:
                self.x += self.p.speed * pps / 4

            # 화살이 벽에 박힌다
            if self.simulate:
                self.x += math.cos(self.incline) * 5 * pps / 4
                self.y += math.sin(self.incline) * 5 * pps / 4
                self.y += self.acc * pps / 4
                self.acc -= 0.01 * pps / 4

                if self.dir == 1:
                    if self.deg > -90:
                        self.deg -= 0.002555 * pps / 4
                elif self.dir == 0:
                    if self.deg < 90:
                        self.deg += 0.002555 * pps / 4

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


class Shell:
    def __init__(self, p, mp, x, y, dir, size_x, size_y):
        self.image = load_image(shell_directory)
        self.p = p
        self.mp = mp
        self.x = x
        self.y = y
        self.dir = dir
        self.size_x = size_x
        self.size_y = size_y
        self.acc = 2
        self.speed = random.uniform(1, 2)
        self.deg = 0
        self.simulate = True
        self.remove_timer = 100

    def update(self):
        pps = game_framework.pps
        if game_framework.MODE == 'play':
            if self.p.mv_right:
                self.x -= self.p.speed * pps / 4
            elif self.p.mv_left:
                self.x += self.p.speed * pps / 4

            if self.simulate:
                if self.dir == 1:
                    self.x -= self.speed * pps / 4
                    self.deg += 0.1 * pps / 3

                elif self.dir == 0:
                    self.x += self.speed * pps / 4
                    self.deg -= 0.1 * pps / 3

                self.y += self.acc * pps / 3
                self.acc -= 0.05 * pps / 3

                if self.y < 190:  # 튕길 속도가 나는 한 계속 튄다
                    self.y = 190
                    self.acc = (self.acc / 2) * -1

                    if -1 <= self.acc <= 1:  # 더 이상 튕길 속도가 나지 않으면 시뮬레이션을 정지한다.
                        self.deg = 0
                        self.y = 195
                        self.simulate = False

                if self.x <= self.mp.playerToWallLeft + 10:  # 벽에 튕기면 반대로 튄다
                    self.dir = 0

                if self.x >= self.mp.playerToWallRight - 10:
                    self.dir = 1

            else:
                self.remove_timer -= pps / 3
                if self.remove_timer <= 0:
                    game_manager.remove_object(self)

    def draw(self):
        x = self.x + self.p.ex
        y = self.y + self.p.ey
        self.image.rotate_draw(self.deg, x, y, self.size_x, self.size_y)

    def handle_evnet(self):
        pass


class Feedback:
    def __init__(self, x, y):
        self.image = load_image(hit_feeeback_directory)
        self.x = x
        self.y = y
        self.op = 300

    def draw(self):
        self.image.opacify(self.op)
        self.image.draw(self.x, self.y, 40, 40)

    def update(self):
        pps = game_framework.pps

        if self.op > 0:
            self.op -= 4 * pps / 3
        else:
            game_manager.remove_object(self)

    def handle_event(self):
        pass


class Bullet:
    def __init__(self, weapon, p, mp, x, y, incline, name):
        self.weapon = weapon
        self.p, self.mp = p, mp
        self.x, self.y = x, y
        self.incline = incline
        self.name = name

    def update(self):
        pps = game_framework.pps

        if game_framework.MODE == 'play':
            if self.x < self.mp.playerToWallLeft or self.x > self.mp.playerToWallRight:
                self.weapon.pen_enable = False  # 벽에 닿으면 관통 비활성화 후 객체 삭제
                game_manager.remove_object(self)

            if self.y < 120 + self.p.cam_h or self.y > 750 + self.p.y + self.p.cam_h:  # 바닥이나 너무 높이 올라가도 삭제
                self.weapon.pen_enable = False
                game_manager.remove_object(self)

            self.x += math.cos(self.incline) * 40 * pps / 4
            self.y += math.sin(self.incline) * 40 * pps / 4

            if self.p.mv_right:
                self.x -= self.p.speed * pps / 4
            elif self.p.mv_left:
                self.x += self.p.speed * pps / 4

    def draw(self):
        pass
        # draw_rectangle(*self.get_bb())

    def handle_event(self):
        pass

    def get_bb(self):
        return self.x + self.p.ex - 70, self.y + self.p.ey - 30, self.x + self.p.ex + 70, self.y + self.p.ey + 30

    def handle_collision(self, group, other):
        pass
