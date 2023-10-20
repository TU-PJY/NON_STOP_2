# 무기 관련 함수 모음
from pico2d import *
from Env_variable import *
import math


def l_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONDOWN and e[1].button == SDL_BUTTON_LEFT


def l_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONUP and e[1].button == SDL_BUTTON_LEFT


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

        if weapon.name == 'SCAR_H':  # GUN_NAME에 따라 사용하는 총기가 달라진다.
            if weapon.p.dir == 1:
                weapon.scar_right.clip_composite_draw(0, 0, 150, 100, weapon.deg, '', weapon.p.px + 20, weapon.p.py2,
                                                      170, 120)
            elif weapon.p.dir == 0:
                weapon.scar_left.clip_composite_draw(0, 0, 150, 100, weapon.deg, 'h, v', weapon.p.px - 20, weapon.p.py2,
                                                     170, 120)


def draw_flame(weapon):
    if weapon.flame_display_time > 0 and weapon.weapon_type == 0:
        weapon.flame_display_time -= 1
        if weapon.p.dir == 1:
            weapon.flame_right.clip_composite_draw(0, 0, 100, 100, weapon.deg, '',
                                                   weapon.p.px + 20 + math.cos(weapon.deg) * 150,
                                                   weapon.p.py2 + math.sin(weapon.deg) * 150, 100, 100)
        elif weapon.p.dir == 0:
            weapon.flame_left.clip_composite_draw(0, 0, 100, 100, weapon.deg, 'h, v',
                                                  weapon.p.px - 20 + math.cos(weapon.deg) * 150,
                                                  weapon.p.py2 + math.sin(weapon.deg) * 150, 100, 100)


def draw_melee(weapon):
    if weapon.weapon_type == 1:
        if weapon.melee_x == 0:
            weapon.melee_deg = 170

        if weapon.melee == 'KNIFE':
            if weapon.p.dir == 1:
                weapon.knife_right.clip_composite_draw(0, 0, 150, 100, weapon.melee_deg, '',
                                                       weapon.p.px + 50 + weapon.melee_x,
                                                       weapon.p.py2 - 10, 100, 50)

            elif weapon.p.dir == 0:
                weapon.knife_right.clip_composite_draw(0, 0, 150, 100, -weapon.melee_deg, 'h',
                                                       weapon.p.px - 50 - weapon.melee_x,
                                                       weapon.p.py2 - 10, 100, 50)


def shoot_gun(weapon):
    if weapon.trigger and weapon.weapon_type == 0:
        if weapon.shoot_delay == 0:  # 딜레이는 총마다 다르며, 딜레이 수치가 낮을수록 연사 속도가 빠르다. 0이 될 때마다 발사된다.
            weapon.shoot = True  # True일시 해당 값을 Target 클래스로 전달하여 Target 클래스의 recoil을 증가시킨다.
            if weapon.name == 'SCAR_H':
                weapon.flame_display_time = FLAME_DISPLAY_TIME
                weapon.shoot_delay = 30
                weapon.p.shake_time = 20
                weapon.p.shake_range = 10
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


def melee_hit_manager(weapon, i):
    global mx  # monster x
    mx = weapon.m.list[i][0]
    if weapon.wield:  # 사용자 경험을 위해 50픽셀정도 더 길게 인식하도록 한다.
        if weapon.melee == 'KNIFE':  # 무기마다 사거리가 다르므로 따로 범위를 지정해야 한다.
            if weapon.p.dir == 1:
                if (weapon.p.x + weapon.p.efx <= mx + 50 + weapon.p.efx <=
                        weapon.p.x + weapon.melee_x + 200 + weapon.p.efx):
                    weapon.m.list[i][8] = True
                    return  # 중복 인식 방지를 위해 히트가 인식되면 바로 함수를 빠져나가도록 한다.

            elif weapon.p.dir == 0:
                if (weapon.p.x - weapon.melee_x - 200 + weapon.p.efx <= mx - 50 + weapon.p.efx <=
                        weapon.p.x + weapon.p.efx):
                    weapon.m.list[i][8] = True
                    return

        weapon.m.hit_type = 1


def damage_manager(weapon, i):  # 몬스터 대미지 처리
    global hit
    hit = weapon.m.list[i][8]

    if hit:  # 총에 맞으면
        if weapon.m.hit_type == 0:
            if weapon.name == 'SCAR_H':  # 총기마다 다른 대미지가 들어간다.
                weapon.m.list[i][3] -= 45

        elif weapon.m.hit_type == 1:
            if weapon.melee == 'KNIFE':
                weapon.m.list[i][3] -= 50

        weapon.m.list[i][8] = False  # 총에 맞은 상태를 초기화 한다.
