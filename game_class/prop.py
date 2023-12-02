import random

from pico2d import *

from config import *
from game_work import game_manager, game_framework
from mods import play_mode, gameover_mode


class Arrow:
    sound = None

    def __init__(self, p, mp, x, y, incline, dir):
        self.x = x
        self.y = y
        self.incline = incline
        self.p = p
        self.mp = mp
        self.dir = dir
        self.acc = 0
        self.remove_timer = 300
        self.simulate = True  # True일 동안 움직임

        if self.dir == 0:
            self.arrow_left = load_image(arrow_left_directory)
        elif self.dir == 1:
            self.arrow_right = load_image(arrow_right_directory)

        if not Arrow.sound:
            Arrow.sound = load_wav(arrow_wall_directory)

    def update(self):
        pps = game_framework.pps
        speed = game_framework.pps * self.p.speed
        if game_framework.MODE == 'play':
            if self.p.mv_right:
                self.x -= speed
            elif self.p.mv_left:
                self.x += speed

            # 화살이 벽에 박힌다
            if self.simulate:
                self.x += math.cos(self.incline) * 4 * pps / 4
                self.y += math.sin(self.incline) * 4 * pps / 4

                if self.dir == 1:  # 중력에 의해 점차 앞으로 기울어진다.
                    if self.incline > -1.5:
                        self.incline += self.acc * pps / 3
                        self.acc -= 0.0000055 * pps / 3

                elif self.dir == 0:
                    if self.incline < 4.6:
                        self.incline -= self.acc * pps / 3
                        self.acc -= 0.0000055 * pps / 3

                # 화살이 벽에 박히면
                if self.x >= self.mp.playerToWallRight - 10 or self.x <= self.mp.playerToWallLeft + 10 or self.y <= 190:
                    Arrow.sound.play()
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
                (0, 0, 128, 128, self.incline, 'h', x, y, 400, 400)
        elif self.dir == 1:
            self.arrow_right.clip_composite_draw \
                (0, 0, 128, 128, self.incline, '', x, y, 400, 400)

        draw_rectangle(*self.get_bb())

    def handle_event(self):
        pass

    def get_bb(self):
        x = self.x + math.cos(self.incline) * 50 + self.p.ex
        y = self.y + math.sin(self.incline) * 50 + self.p.ey
        return x - 10, y - 10, x + 10, y + 10

    def handle_collision(self, group, other):
        if group == 'player:arrow':
            if self.simulate:  # 움직이는 화살만 인식하도록 설정
                if self.p.dmg_delay <= 0:
                    self.p.damage_sound.play()
                    self.p.cur_hp -= 15
                    self.p.dmg_shake_range = 30
                    self.p.dmg_delay = 200
                    pd = PlayerDamage()
                    game_manager.add_object(pd, 7)
            game_manager.remove_object(self)


class Shell:
    sound = None

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

        if not Shell.sound:
            Shell.sound = load_wav(shell_hit_directory)

    def update(self):
        pps = game_framework.pps
        speed = game_framework.pps * self.p.speed
        if game_framework.MODE == 'play':
            if self.p.mv_right:
                self.x -= speed
            elif self.p.mv_left:
                self.x += speed

            if self.simulate:  # true 일 때만 움직인다
                if self.dir == 1:
                    self.x -= self.speed * pps / 4
                    self.deg += 0.1 * pps / 2

                elif self.dir == 0:
                    self.x += self.speed * pps / 4
                    self.deg -= 0.1 * pps / 2

                self.y += self.acc * pps / 4
                self.acc -= 0.05 * pps / 4  # 바닥에 튕길때마다 가속값이 감소

                if self.y < 190:  # 튕길 속도가 나는 한 계속 튄다
                    self.y = 190
                    self.acc = (self.acc / 2) * -1
                    Shell.sound.play()

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
    def __init__(self, x, y, size):
        self.image = load_image(hit_feeeback_directory)
        self.x = x
        self.y = y
        self.op = 1
        self.size = size

    def draw(self):
        self.image.opacify(self.op)
        if self.size == 2:
            self.image.draw(self.x, self.y, 60, 60)
        elif self.size == 1:
            self.image.draw(self.x, self.y, 40, 40)

    def update(self):
        pps = game_framework.pps

        if game_framework.MODE == 'play':
            if self.op > 0:  # 피드백이 점차 투명해진다
                self.op -= pps / 400
            if self.op <= 0:
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
        self.move_delay = 10

    def update(self):
        pps = game_framework.pps
        speed = game_framework.pps * self.p.speed

        if game_framework.MODE == 'play':
            if self.x < self.mp.playerToWallLeft or self.x > self.mp.playerToWallRight or \
                    self.y < 120 + self.p.cam_h or self.y > self.p.y + 800:
                self.weapon.pen_enable = False  # 벽에 부딫히거나 너무 높이 올라가면 객체 삭제
                game_manager.remove_object(self)

            # 생성하자마자 움직이면 최초로 쏜 몬스터와 충돌하지 않을수도 있으므로 약간의 딜레이 후 움직인다.
            if self.move_delay > 0:
                self.move_delay -= pps / 4
            else:
                self.x += math.cos(self.incline) * 30 * pps / 4  # 총을 쏜 각도대로 움직인다
                self.y += math.sin(self.incline) * 30 * pps / 4

            if self.p.mv_right:
                self.x -= speed
            elif self.p.mv_left:
                self.x += speed

    def draw(self):
        pass
        draw_rectangle(*self.get_bb())

    def handle_event(self):
        pass

    def get_bb(self):
        return self.x + self.p.ex - 30, self.y + self.p.ey - 30, self.x + self.p.ex + 30, self.y + self.p.ey + 30

    def handle_collision(self, group, other):
        pass


class KatanaSlice:
    def __init__(self, p, weapon):
        self.p, self.weapon = p, weapon
        self.x, self.y = 0, 0
        self.dir = 0
        self.player_deg = 0
        self.melee_deg = 0
        self.op = 0.8
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
        self.back.opacify(self.op)
        self.katana_slice.opacify(self.op)
        self.effect.opacify(self.op)

        self.back.draw(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)

        # 스킬 이펙트 출력
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
                    (0, 0, 60, 410, self.weapon.melee_deg, '', self.p.px + 40, self.p.py - 30, 50, 360)

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

        if game_framework.MODE == 'play':
            if not self.weapon.skill_enable:
                self.op_reduce = True

            if self.op_reduce:  # 스킬 사용이 끝나면 효과가 점차 투명해진다
                self.op -= pps / 400
                if self.op <= 0:  # 완전히 투명해지면 객체 삭제
                    game_manager.remove_object(self)

    def handle_event(self):
        pass


class PlayerDamage:
    def __init__(self, heal=False):
        self.op = 1
        self.heal = heal
        if not self.heal:
            self.image = load_image(player_damage_directory)
        elif self.heal:
            self.image = load_image(player_heal_directory)

    def draw(self):
        self.image.opacify(self.op)
        self.image.draw(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
        pass

    def update(self):
        pps = game_framework.pps
        if game_framework.MODE == 'play':
            self.op -= pps / 800
            if self.op <= 0:
                game_manager.remove_object(self)

    def handle_event(self):
        pass


class Coin:
    pickup = None

    def __init__(self, p, mp, x, y, dir, sp=2):
        self.image = load_image(coin_icon_directory)
        self.p = p
        self.mp = mp
        self.x = x
        self.y = y
        self.dir = dir
        self.acc = 3
        self.sp = sp
        self.size_down = True
        self.size_x = 70
        self.up = False
        self.fall = True
        self.op = 1

        if self.sp > 2:
            self.acc = 5

        if not Coin.pickup:
            Coin.pickup = load_wav(pickup_directory)

    def draw(self):
        self.image.opacify(self.op)
        self.image.draw(self.x + self.p.ex, self.y + self.p.ey, self.size_x, 70)
        draw_rectangle(*self.get_bb())

    def update(self):
        pps = game_framework.pps
        speed = game_framework.pps * self.p.speed
        if game_framework.MODE == 'play':
            if self.p.mv_right:
                self.x -= speed
            elif self.p.mv_left:
                self.x += speed

            if self.fall:  # true 일 시 코인이 떨어진다
                self.y += self.acc
                self.acc -= pps / 90

                if self.dir == 1:  # 몬스터가 드랍한 직후 지정 방향으로 살짝 움직인다.
                    self.x -= self.sp * pps / 4
                    if self.x <= self.mp.playerToWallLeft + 20:
                        self.dir = 0

                elif self.dir == 0:
                    self.x += self.sp * pps / 4
                    if self.x >= self.mp.playerToWallRight + 20:
                        self.dir = 1

                if self.y <= 230 and self.acc <= 0:  # 바닥에 떨어지면
                    self.y = 230
                    self.fall = False

            if self.size_down:  # 코인이 좌우로 회전한다
                self.size_x -= pps / 5
                if self.size_x <= 0:
                    self.size_x = 0
                    self.size_down = False
            else:
                self.size_x += pps / 5
                if self.size_x >= 70:
                    self.size_x = 70
                    self.size_down = True

            if self.up:  # 플레이어가 코인을 얻으면 투명해지면서 사라지는 효과를 출력
                self.y += pps
                self.op -= pps / 800
                if self.op <= 0:
                    game_manager.remove_object(self)

    def handle_event(self):
        pass

    def handle_collision(self, group, other):
        if group == 'player:coin':
            if not self.up:  # 획득하지 않은 코인에 대해서만 코인 획득 피드백 재생
                Coin.pickup.play()
                self.p.coin += 20 + play_mode.tool.rounds * 10  # 라운드가 올라갈 수록 코인을 더 많이 획득한다
                self.up = True
                self.p.get_coin = True

    def get_bb(self):
        x = self.x + self.p.ex
        y = self.y + self.p.ey
        return x - 30, y - 30, x + 30, y + 30


class Explode:
    def __init__(self, p, weapon, x, y):
        self.image = load_image(explode_directory)
        self.x = x
        self.y = y + 50
        self.p = p
        self.frame = 0
        self.weapon = weapon

    def draw(self):
        x = self.x + self.p.ex
        y = self.y + self.p.ey
        size = self.weapon.gren_level * 200  # 수류탄 레벨이 올라갈수록 폭발도 커진다
        self.image.clip_composite_draw(100 * int(self.frame), 0, 100, 695, 0, '', x, y, 200 + size, 200 + size)

    def update(self):
        pps = game_framework.pps
        speed = game_framework.pps * self.p.speed
        if game_framework.MODE == 'play':
            self.frame = (self.frame + pps / 40) % 7
            if int(self.frame) == 6:  # 폭발 애니메이션이 다 출력되면 객체 삭제
                game_manager.remove_object(self)

            if self.p.mv_right:
                self.x -= speed
            elif self.p.mv_left:
                self.x += speed

    def handle_event(self):
        pass

    def get_bb(self):
        bound = self.weapon.gren_level * 200
        x = self.x + self.p.ex
        y = self.y + self.p.ey
        if int(self.frame) == 0:  # 폭발 순간에만 히트박스 제공
            return x - bound, y - bound, x + bound, y + bound
        else:
            return -9999, -9999, -9999, -9999

    def handle_collision(self, group, other):
        pass


class Grenade:
    sound = None
    hit_sound = None

    def __init__(self, p, mp, weapon, x, y, dir):
        self.image = load_image(grenade_directory)
        self.x, self.y, self.dir = x, y, dir
        self.p, self.mp = p, mp
        self.weapon = weapon
        self.timer = 1200
        self.acc = 4
        self.speed = 4
        self.simulate = True
        self.deg = 0

        if not Grenade.sound:
            Grenade.sound = load_wav(explode_sound_directory)
            Grenade.hit_sound = load_wav(gren_hit_directory)

        if self.p.mv_right and self.dir == 1:  # 움직이는 방향으로 향하여 던지면 더 빨리 날아간다
            self.speed = 9
        elif self.p.mv_left and self.dir == 0:
            self.speed = 9

    def draw(self):
        x = self.x + self.p.ex
        y = self.y + self.p.ey
        self.image.rotate_draw(self.deg, x, y, 40, 40)
        pass

    def update(self):
        pps = game_framework.pps
        speed = game_framework.pps * self.p.speed
        if game_framework.MODE == 'play':
            if self.simulate:  # true 일 때만 움직임
                if self.dir == 1:
                    self.deg -= 5 * pps / 4
                    self.x += self.speed * pps / 4
                    if self.x >= self.mp.playerToWallRight:
                        self.speed -= 2
                        self.dir = 0

                elif self.dir == 0:
                    self.deg += 5 * pps / 4
                    self.x -= self.speed * pps / 4
                    if self.x <= self.mp.playerToWallLeft:
                        self.speed -= 2
                        self.dir = 1

                self.y += self.acc * pps / 4
                self.acc -= pps / 90

                if self.y <= 200:
                    Grenade.hit_sound.play()
                    self.speed -= 1
                    self.y = 200
                    self.acc = self.acc / 2 * -1
                    if self.acc < 0.5:
                        self.simulate = False

            if self.p.mv_right:
                self.x -= speed
            elif self.p.mv_left:
                self.x += speed

            self.timer -= pps / 3

        if self.timer <= 0:  # 타이머가 0이되면 폭발한다.
            Grenade.sound.play()
            self.weapon.gren_x = self.x  # 몬스터가 날아가는 방향을 지정하기 위해 weapon 클래스로 자기 위치를 전달한다
            ex = Explode(self.p, self.weapon, self.x, self.y)
            self.p.ex_shake_range = 100  # 화면이 흔들린다
            game_manager.add_object(ex, 5)  # 폭발 애니메이션 추가
            game_manager.add_collision_pair('grenade:monster', ex, None)
            game_manager.remove_object(self)

    def handle_event(self):
        pass


class Splash:
    def __init__(self, p, x, y):
        self.p = p
        self.x = x
        self.y = y
        self.frame = 0
        self.image = load_image(splash_directory)

    def draw(self):
        self.image.clip_draw(int(self.frame) * 165, 0, 165, 148, self.x + self.p.ex, self.y + self.p.ey, 400, 400)

    def update(self):
        pps = game_framework.pps
        speed = game_framework.pps * self.p.speed

        if game_framework.MODE == 'play':
            if self.p.mv_right:
                self.x -= speed
            if self.p.mv_left:
                self.x += speed

            self.frame = (self.frame + pps / 50) % 9

            if int(self.frame) == 8:
                game_manager.remove_object(self)

    def handle_event(self):
        pass


class Dead:
    sound = None

    def __init__(self, p, mp, x, y, dir, type, animation=0):
        self.p, self.mp = p, mp
        self.x, self.y, self.dir = x, y, dir
        self.type = type
        self.ani = animation  # 이 변수에 따라 시체가 날아가거나 쓰러진다
        self.deg = 0
        self.simulate = True  # 이 변수가 false가 되면 투명화를 가동한다
        self.op = 1  # 투명도
        self.remove_timer = 300
        self.speed = 6

        self.size_reduce = 0  # type2 데드 모션 출력 용 변수

        if self.type == 1:
            self.image = load_image(goblin_dead_directory)
            self.acc = 1.5  # 걸어오다가 앞으로 넘어져 죽는 모션을 위한 변수

        elif self.type == 4:
            self.image = load_image(apple_dead_directory)
            self.acc = 0.5  # 걸어오다가 앞으로 넘어져 죽는 모션을 위한 변수

        if self.ani == 1:
            self.acc = 3

        elif self.ani == 2:
            self.acc = 4

        elif self.ani == 3:
            self.acc = random.uniform(5, 9)

        elif self.ani == 4:
            self.acc = random.uniform(6, 7)

        if self.type == 2:
            self.ani = -1
            self.image = load_image(ghost_dead_directory)

        if not Dead.sound:
            Dead.sound = load_wav(flesh_directory)

    def draw(self):
        deg = math.radians(self.deg)
        self.image.opacify(self.op)

        if self.type == 1:  # 믄스터마다 이미지 크기가 달라 따로 지정
            if self.dir == 1:
                self.image.composite_draw(deg, 'h', self.x + self.p.ex, self.y + self.p.ey - 50, 280, 280)
            elif self.dir == 0:
                self.image.composite_draw(deg, '', self.x + self.p.ex, self.y + self.p.ey - 50, 280, 280)

        elif self.type == 2:
            if self.dir == 1:
                self.image.composite_draw(deg, 'h', self.x + self.p.ex, self.y + self.p.ey,
                                          400 - self.size_reduce, 400 - self.size_reduce)
            elif self.dir == 0:
                self.image.composite_draw(deg, '', self.x + self.p.ex, self.y + self.p.ey,
                                          400 - self.size_reduce, 400 - self.size_reduce)
        elif self.type == 4:
            if self.dir == 1:
                self.image.composite_draw(deg, 'h', self.x + self.p.ex, self.y + self.p.ey - 30, 450, 450)
            elif self.dir == 0:
                self.image.composite_draw(deg, '', self.x + self.p.ex, self.y + self.p.ey - 30, 450, 450)

    def update(self):
        pps = game_framework.pps
        speed = game_framework.pps * self.p.speed

        if game_framework.MODE == 'play':
            if self.p.mv_right:
                self.x -= speed
            elif self.p.mv_left:
                self.x += speed

            if self.simulate:
                # animation -1
                if self.ani == -1:
                    if self.dir == 1:
                        self.deg += pps / 2
                    elif self.dir == 0:
                        self.deg -= pps / 2

                    if self.op < 250:
                        self.op += int(pps / 2)
                    if self.op > 250:
                        self.op = 250

                    self.size_reduce += pps / 3

                    if self.size_reduce >= 400:
                        game_manager.remove_object(self)

                # animation 0
                if self.ani == 0:  # 앞으로 넘어져 죽는 모션, 기본 모션
                    if self.dir == 1:
                        self.x += self.acc * pps / 4

                    elif self.dir == 0:
                        self.x -= self.acc * pps / 4

                    self.acc -= pps / 400

                    if self.x <= self.mp.playerToWallLeft or self.x >= self.mp.playerToWallRight:
                        self.acc = 0

                    if self.acc < 0:  # 앞으로 넘어지면서 점차 속도가 줄어든다.
                        self.acc = 0
                        self.simulate = False

                # aniamtion 1
                elif self.ani == 1:  # 고화력 총기에 튕겨저 나가 죽는 모션, rifle 이상부터 재생
                    if self.dir == 1:
                        self.deg = 180
                        self.x -= self.acc * pps / 4
                    elif self.dir == 0:
                        self.deg = -180
                        self.x += self.acc * pps / 4

                    self.acc -= pps / 400

                    if self.x <= self.mp.playerToWallLeft or self.x >= self.mp.playerToWallRight:
                        self.acc = 0

                    if self.acc < 0:
                        self.acc = 0
                        self.simulate = False

                # animation 2
                elif self.ani == 2:  # 고화력 총기에 튕겨저 나가 죽는 모션, rifle 이상부터 재생
                    if self.dir == 1:
                        self.deg += self.acc * pps / 4
                        self.x -= self.acc * pps / 4
                    elif self.dir == 0:
                        self.deg -= self.acc * pps / 4
                        self.x += self.acc * pps / 4

                    self.acc -= pps / 400

                    if self.x <= self.mp.playerToWallLeft or self.x >= self.mp.playerToWallRight:
                        self.acc = 0

                    if self.acc < 0:
                        self.acc = 0
                        self.simulate = False

                # animation 3
                elif self.ani == 3:  # 폭발에 튕겨나가는 모션
                    if self.dir == 1:
                        self.x -= self.speed * pps / 4
                        self.deg += pps / 4
                        if self.x <= self.mp.playerToWallLeft:
                            self.speed -= random.uniform(1.5, 3)
                            self.dir = 0

                    elif self.dir == 0:
                        self.x += self.speed * pps / 4
                        self.deg -= pps / 4
                        if self.x >= self.mp.playerToWallRight:
                            self.speed -= random.uniform(1.5, 3)
                            self.dir = 1

                    self.y += self.acc * pps / 4
                    self.acc -= pps / 90

                    if self.y < 250 and self.type == 1:
                        Dead.sound.play()
                        self.y = 260
                        self.acc = self.acc * (-1) / 1.5
                        if self.acc < 1:
                            self.simulate = False

                    if self.y < 230 and self.type == 4:
                        Dead.sound.play()
                        self.y = 240
                        self.acc = self.acc * (-1) / 1.5
                        if self.acc < 1:
                            self.simulate = False

                # animation 4
                elif self.ani == 4:  # 카타나 또는 도끼 스킬에 죽는 모션
                    if self.dir == 1:
                        self.deg += pps / 4

                    elif self.dir == 0:
                        self.deg -= pps / 4

                    self.acc -= pps / 90
                    self.y += self.acc * pps / 4

                    if self.y < 250 and self.type == 1:
                        Dead.sound.play()
                        self.y = 260
                        self.acc = self.acc * (-1) / 1.5
                        if self.acc < 1:
                            self.simulate = False

                    if self.y < 230 and self.type == 4:
                        Dead.sound.play()
                        self.y = 240
                        self.acc = self.acc * (-1) / 1.5
                        if self.acc < 1:
                            self.simulate = False

            elif not self.simulate:
                self.remove_timer -= pps / 3
                if self.remove_timer <= 0:
                    self.op += int(pps / 2)  # 시뮬레이션이 끝나면 투명해지면서 사라진다
                    if self.op > 250:
                        game_manager.remove_object(self)

    def handle_event(self):
        pass


class Playerdead:  # 이 클래스를 거쳐 모드를 변경하게 된다
    def __init__(self):
        self.image = load_image(dead_bg_directory)
        self.sign = load_image(you_dead_directory)
        self.front = load_image(front_directory)
        self.font = load_font(font_directory, 100)
        self.size = 0

        self.x1 = 0
        self.x2 = WIDTH
        self.acc = 0
        self.delay = 0

        self.front_size = 0

    def draw(self):
        self.image.draw(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
        self.sign.draw(WIDTH / 2, HEIGHT / 2 - 200, 800 + self.size, 200 + self.size / 3)

        self.front.draw(self.x1 + self.front_size / 2, HEIGHT / 2, self.front_size, HEIGHT)
        self.front.draw(self.x2 - self.front_size / 2, HEIGHT / 2, self.front_size, HEIGHT)

        self.font.draw(self.x1 + self.front_size - 450, HEIGHT / 2, 'GAME', (172, 162, 132))
        self.font.draw(self.x2 - self.front_size + 20, HEIGHT / 2, 'OVER', (172, 162, 132))

    def update(self):
        pps = game_framework.pps
        self.size += pps / 5
        self.delay += pps / 3

        if self.delay >= 600:
            self.front_size += self.acc * pps / 4
            self.acc += pps / 200
            if self.front_size > WIDTH / 2:
                self.acc = self.acc / 4 * -1
                self.front_size = WIDTH / 2

        if self.delay >= 1500:
            game_framework.change_mode(gameover_mode)

    def handle_event(self):
        pass


class Start:
    def __init__(self):
        self.y1 = HEIGHT
        self.y2 = 0
        self.up = load_image(front_directory)
        self.down = load_image(front_directory)
        self.font = load_font(font_directory, 80)
        self.acc = 0

    def draw(self):
        self.up.draw(WIDTH / 2, self.y1, WIDTH, HEIGHT)
        self.down.draw(WIDTH / 2, self.y2, WIDTH, HEIGHT)

    def update(self):
        pps = game_framework.pps
        self.y1 += self.acc * pps / 4
        self.y2 -= self.acc * pps / 4

        self.acc += pps / 100

        if self.y1 > HEIGHT + HEIGHT / 2:
            game_manager.remove_object(self)
