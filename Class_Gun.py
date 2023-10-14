from pico2d import *
from Env_variable import *
import math


# Player location -> Gun class


def l_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONDOWN and e[1].button == SDL_BUTTON_LEFT


def l_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONUP and e[1].button == SDL_BUTTON_LEFT


def load_gun_image(self):
    self.flame_right = load_image(flame_right_directory)
    self.flame_left = load_image(flame_left_directory)

    self.scar_right = load_image(scar_h_right_directory)
    self.scar_left = load_image(scar_h_left_directory)


def draw_gun(gun):
    gun.deg = math.atan2(gun.p.my - gun.p.y, gun.p.mx - gun.p.x)

    if GUN_NAME == 'SCAR_H':  # GUN_NAME에 따라 사용하는 총기가 달라진다.
        if gun.p.dir == 1:
            gun.scar_right.clip_composite_draw(0, 0, 150, 100, gun.deg, '', gun.p.x + gun.p.shake_x,
                                               gun.p.y - 10 - gun.p.land_y + gun.p.shake_y, 170, 120)
        elif gun.p.dir == 0:
            gun.scar_left.clip_composite_draw(0, 0, 150, 100, gun.deg, 'h, v', gun.p.x + gun.p.shake_x,
                                              gun.p.y - 10 - gun.p.land_y + gun.p.shake_y, 170, 120)


def draw_flame(gun):
    if gun.flame_display_time > 0:
        gun.flame_display_time -= 1
        if gun.p.dir == 1:
            gun.flame_right.clip_composite_draw(0, 0, 100, 100, gun.deg, '',
                                                gun.p.x + math.cos(gun.deg) * 150 + gun.p.shake_x,
                                                gun.p.y + math.sin(gun.deg) * 150 - gun.p.land_y + gun.p.shake_y, 100,
                                                100)
        elif gun.p.dir == 0:
            gun.flame_left.clip_composite_draw(0, 0, 100, 100, gun.deg, 'h, v',
                                               gun.p.x + math.cos(gun.deg) * 150 + gun.p.shake_x,
                                               gun.p.y + math.sin(gun.deg) * 150 - gun.p.land_y + gun.p.shake_y, 100,
                                               100)


def set_display_shake(gun):
    gun.p.shake_timer = 30
    gun.p.shake_range = 10
    gun.p.shoot_shake = True


def shoot_gun(gun):
    if gun.trigger:
        if gun.shoot_delay == 0:  # 딜레이는 총마다 다르며, 딜레이 수치가 낮을수록 연사 속도가 빠르다. 0이 될 때마다 발사된다.
            if GUN_NAME == 'SCAR_H':
                gun.shoot = True  # True일시 해당 값을 Target 클래스로 전달하여 Target 클래스의 recoil을 증가시킨다.
                gun.flame_display_time = FLAME_DISPLAY_TIME
                gun.shoot_delay = 60
                set_display_shake(gun)
        else:
            gun.shoot = False
            gun.shoot_delay -= 1


class Shoot:
    @staticmethod
    def enter(gun, e):
        if l_down(e):
            gun.trigger = True

    @staticmethod
    def exit(gun, e):
        gun.trigger = False
        gun.shoot = False
        gun.shoot_delay = 0

    @staticmethod
    def do(gun):
        shoot_gun(gun)

    @staticmethod
    def draw(gun):
        draw_gun(gun)
        draw_flame(gun)


class Idle:
    @staticmethod
    def enter(gun, e):
        pass

    @staticmethod
    def exit(gun, e):
        pass

    @staticmethod
    def do(gun):
        pass

    @staticmethod
    def draw(gun):
        draw_gun(gun)
        draw_flame(gun)


class StateMachineGun:
    def __init__(self, gun):
        self.gun = gun
        self.cur_state = Idle
        self.table = {
            Idle: {l_down: Shoot},
            Shoot: {l_up: Idle}
        }

    def start(self):
        self.cur_state.enter(self.gun, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.gun)

    def handle_event(self, e):  # state event handling
        for check_event, next_state in self.table[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.gun, e)
                self.cur_state = next_state
                self.cur_state.enter(self.gun, e)
                return True
        return False

    def draw(self):
        self.cur_state.draw(self.gun)


class Gun:
    def __init__(self, p):
        load_gun_image(self)
        self.p = p

        self.deg = 0  # 총 이미지 각도

        self.trigger = False
        self.shoot = False
        self.shoot_delay = 0

        self.flame_display_time = 0

        self.state_machine = StateMachineGun(self)
        self.state_machine.start()

    def draw(self):
        self.state_machine.draw()

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))
