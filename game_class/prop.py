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

        draw_rectangle(*self.get_bb())

    def handle_event(self):
        pass

    def get_bb(self):
        x = self.x + math.cos(self.deg) * 50 + self.p.ex
        y = self.y + math.sin(self.deg) * 50 + self.p.ey
        return x - 10, y - 10, x + 10, y + 10

    def handle_collision(self, group, other):
        if group == 'player:arrow':
            if self.p.dmg_delay <= 0:
                self.p.dmg_shake_range = 30
                self.p.dmg_delay = 200
                pd = PlayerDamage()
                game_manager.add_object(pd, 7)
            game_manager.remove_object(self)




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
        self.op = 1

    def draw(self):
        self.image.opacify(self.op)
        self.image.draw(self.x, self.y, 40, 40)

    def update(self):
        pps = game_framework.pps

        if self.op < 99:
            self.op += int(2 * pps / 3)
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
        self.move_delay = 30

    def update(self):
        pps = game_framework.pps

        if game_framework.MODE == 'play':
            if self.x < self.mp.playerToWallLeft or self.x > self.mp.playerToWallRight or \
                    self.y < 120 + self.p.cam_h or self.y > self.p.y + 800:
                self.weapon.pen_enable = False
                game_manager.remove_object(self)

            # 객체 생성하자마자 움직이면 최초로 쏜 몬스터와 충돌하지 않을수도 있으므로 약간의 딜레이 후 움직인다.
            if self.move_delay > 0:
                self.move_delay -= pps / 4
            else:
                self.x += math.cos(self.incline) * 30 * pps / 4
                self.y += math.sin(self.incline) * 30 * pps / 4

            if self.p.mv_right:
                self.x -= self.p.speed * pps / 4
            elif self.p.mv_left:
                self.x += self.p.speed * pps / 4

    def draw(self):
        pass
        draw_rectangle(*self.get_bb())

    def handle_event(self):
        pass

    def get_bb(self):
        return self.x + self.p.ex, self.y + self.p.ey, self.x + self.p.ex, self.y + self.p.ey

    def handle_collision(self, group, other):
        pass


class KatanaSlice:
    def __init__(self, p, weapon):
        self.p, self.weapon = p, weapon
        self.x, self.y = 0, 0
        self.dir = 0
        self.player_deg = 0
        self.melee_deg = 0
        self.op = 1
        self.op_reduce = False

        self.dir = self.p.dir

        self.back = load_image(pause_bg_directory)
        self.katana_slice = load_image(katana_slice_directory)
        self.player1_slice_right = load_image(player1_slice_right_directory)
        self.player1_slice_left = load_image(player1_slice_left_directory)
        self.effect = load_image(slice_effect_directory)

        self.start_x = self.p.px
        self.stary_y = self.p.py

    def draw(self):
        self.back.opacify(self.op + 50)
        self.katana_slice.opacify(self.op)
        self.effect.opacify(self.op)

        self.back.draw(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)

        if self.dir == 1:
            self.effect.clip_composite_draw(0, 0, 1500, 280, 0, '', self.p.px - 900, self.p.py, 1500, 280)
        else:
            self.effect.clip_composite_draw(0, 0, 1500, 280, 0, 'h', self.p.px + 900, self.p.py, 1500, 280)

        if self.p.dir == 1:
            self.player1_slice_right.opacify(self.op)
            (self.player1_slice_right.rotate_draw(self.p.rotate, self.p.px, self.p.py, 400, 400))
            if self.weapon.skill_enable:
                self.katana_slice.clip_composite_draw \
                    (0, 0, 60, 410, -self.weapon.melee_deg, 'h', self.p.px - 40, self.p.py - 30, 50, 360)
            else:
                self.katana_slice.clip_composite_draw \
                    (0, 0, 60, 410, self.weapon.melee_deg, '', self.p.px + 40, self.p.py - 30, 50, 360) \

        elif self.p.dir == 0:
            self.player1_slice_left.opacify(self.op)
            self.player1_slice_left.rotate_draw(-self.p.rotate, self.p.px, self.p.py, 400, 400)
            if self.weapon.skill_enable:
                self.katana_slice.clip_composite_draw \
                    (0, 0, 60, 410, self.weapon.melee_deg, '', self.p.px + 40, self.p.py - 30, 50, 360)
            else:
                self.katana_slice.clip_composite_draw \
                    (0, 0, 60, 410, -self.weapon.melee_deg, 'h', self.p.px - 40, self.p.py - 30, 50, 360)

    def update(self):
        pps = game_framework.pps

        if not self.weapon.skill_enable:
            self.op_reduce = True

        if self.op_reduce:
            self.op += int(4 * pps / 3)
            if self.op >= 99:
                game_manager.remove_object(self)

    def handle_event(self):
        pass


class PlayerDamage:
    def __init__(self):
        self.op = 1
        self.image = load_image(player_damage_directory)

    def draw(self):
        self.image.opacify(self.op)
        self.image.draw(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
        pass

    def update(self):
        pps = game_framework.pps
        if self.op < 250:
            self.op += int(pps / 2)
        else:
            game_manager.remove_object(self)

        pass

    def handle_event(self):
        pass
