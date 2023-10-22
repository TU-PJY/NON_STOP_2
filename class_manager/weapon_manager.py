# 무기 관련 함수 모음
from pico2d import *
from game_main.config import *
import math


def l_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONDOWN and e[1].button == SDL_BUTTON_LEFT


def l_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONUP and e[1].button == SDL_BUTTON_LEFT


def q_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_q


def load_gun_image(self):
    self.flame_right = load_image(flame_right_directory)
    self.flame_left = load_image(flame_left_directory)

    self.scar_right = load_image(scar_h_right_directory)
    self.scar_left = load_image(scar_h_left_directory)


def load_melee_image(self):
    self.knife_right = load_image(knife_right_directory)
    self.knife_left = load_image(knife_left_directory)


def draw_gun(weapon):
    if weapon.weapon_type == 0:
        weapon.deg = math.atan2(weapon.p.my - weapon.p.y, weapon.p.mx - weapon.p.x)

        if weapon.gun == 'SCAR_H':  # GUN_NAME에 따라 사용하는 총기가 달라진다.
            if weapon.p.dir == 1:
                weapon.scar_right.clip_composite_draw\
                    (0, 0, 150, 100, weapon.deg, '', weapon.p.px + 20, weapon.p.py2, 170, 120)

            elif weapon.p.dir == 0:
                weapon.scar_left.clip_composite_draw\
                    (0, 0, 150, 100, weapon.deg, 'h, v', weapon.p.px - 20, weapon.p.py2, 170, 120)


def draw_flame(weapon):
    if weapon.flame_display_time > 0 and weapon.weapon_type == 0:
        weapon.flame_display_time -= 1
        if weapon.p.dir == 1:
            weapon.flame_right.clip_composite_draw\
                (0, 0, 100, 100, weapon.deg, '', weapon.p.px + 20 + math.cos(weapon.deg) * 150,
                    weapon.p.py2 + math.sin(weapon.deg) * 150, 100, 100)

        elif weapon.p.dir == 0:
            weapon.flame_left.clip_composite_draw\
                (0, 0, 100, 100, weapon.deg, 'h, v', weapon.p.px - 20 + math.cos(weapon.deg) * 150,
                    weapon.p.py2 + math.sin(weapon.deg) * 150, 100, 100)


def draw_melee(weapon):
    if weapon.weapon_type == 1:
        if weapon.melee_x == 0:
            weapon.melee_deg = 170

        if weapon.melee == 'KNIFE':
            if weapon.p.dir == 1:
                weapon.knife_right.clip_composite_draw\
                    (0, 0, 150, 100, weapon.melee_deg, '', weapon.p.px + 50 + weapon.melee_x,
                        weapon.p.py2 - 10, 100, 50)

            elif weapon.p.dir == 0:
                weapon.knife_right.clip_composite_draw\
                    (0, 0, 150, 100, -weapon.melee_deg, 'h', weapon.p.px - 50 - weapon.melee_x,
                        weapon.p.py2 - 10, 100, 50)


def change_weapon(weapon):
    if weapon.weapon_type == 0:  # 총을 들고 있을 때 총 -> 근접무기
        weapon.p.look_mouse = False  # 플레이어는 더 이상 마우스를 따라보지 않는다.
        weapon.p.rotate = 0
        weapon.weapon_type = 1
        weapon.flame_display_time = 0
        return

    elif weapon.weapon_type == 1:  # 근접무기를 들고 있을 때 근접무기 -> 총
        weapon.p.look_mouse = True
        weapon.weapon_type = 0


def shoot_gun(weapon):
    if weapon.trigger and weapon.weapon_type == 0:
        if weapon.shoot_delay == 0:  # 딜레이는 총마다 다르며, 딜레이 수치가 낮을수록 연사 속도가 빠르다. 0이 될 때마다 발사된다.
            weapon.shoot = True  # True일시 해당 값을 Target 클래스로 전달하여 Target 클래스의 recoil을 증가시킨다.
            if weapon.gun == 'SCAR_H':
                weapon.flame_display_time = FLAME_DISPLAY_TIME
                weapon.shoot_delay = 30
                weapon.p.shake_time = 20
                weapon.p.shake_range = 15
        else:
            weapon.shoot = False


def wield_melee(weapon):
    if weapon.use and weapon.weapon_type == 1:
        if weapon.wield_delay == 0:
            weapon.wield = True
            if weapon.melee == 'KNIFE':
                weapon.melee_x = 100
                weapon.melee_deg = 0
                weapon.wield_delay = 80
                weapon.p.shake_time = 15
                weapon.p.shake_range = 10
        else:
            weapon.wield = False


def update_melee_position(weapon):
    if weapon.melee_x > 0:
        weapon.melee_x -= 2


def update_delay(weapon):
    if weapon.shoot_delay > 0:
        weapon.shoot_delay -= 1
    if weapon.wield_delay > 0:
        weapon.wield_delay -= 1
