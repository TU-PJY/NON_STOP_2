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


def draw_gun(gun):
    if gun.weapon_type == 0:
        gun.deg = math.atan2(gun.p.my - gun.p.y, gun.p.mx - gun.p.x)

        if gun.name == 'SCAR_H':  # GUN_NAME에 따라 사용하는 총기가 달라진다.
            if gun.p.dir == 1:
                gun.scar_right.clip_composite_draw(0, 0, 150, 100, gun.deg, '', gun.p.x + gun.p.shake_x,
                                                   gun.p.y - 10 - gun.p.land_y + gun.p.shake_y, 170, 120)
            elif gun.p.dir == 0:
                gun.scar_left.clip_composite_draw(0, 0, 150, 100, gun.deg, 'h, v', gun.p.x + gun.p.shake_x,
                                                  gun.p.y - 10 - gun.p.land_y + gun.p.shake_y, 170, 120)


def draw_flame(gun):
    if gun.flame_display_time > 0 and gun.weapon_type == 0:
        gun.flame_display_time -= 1
        if gun.p.dir == 1:
            gun.flame_right.clip_composite_draw(0, 0, 100, 100, gun.deg, '',
                                                gun.p.x + math.cos(gun.deg) * 150 + gun.p.shake_x,
                                                gun.p.y + math.sin(gun.deg) * 150 - gun.p.land_y + gun.p.shake_y,
                                                100, 100)
        elif gun.p.dir == 0:
            gun.flame_left.clip_composite_draw(0, 0, 100, 100, gun.deg, 'h, v',
                                               gun.p.x + math.cos(gun.deg) * 150 + gun.p.shake_x,
                                               gun.p.y + math.sin(gun.deg) * 150 - gun.p.land_y + gun.p.shake_y,
                                               100, 100)


def draw_melee(gun):
    if gun.weapon_type == 1:
        if gun.melee_x == 0:
            gun.melee_deg = 170

        if gun.melee == 'KNIFE':
            if gun.p.dir == 1:
                gun.knife_right.clip_composite_draw(0, 0, 150, 100, gun.melee_deg, '', gun.p.x + 50 + gun.melee_x +
                                                    gun.p.shake_x, gun.p.y - 10 - gun.p.land_y + gun.p.shake_y, 100, 50)
            elif gun.p.dir == 0:
                gun.knife_right.clip_composite_draw(0, 0, 150, 100, -gun.melee_deg, 'h', gun.p.x - 50 - gun.melee_x +
                                                    gun.p.shake_x, gun.p.y - 10 - gun.p.land_y + gun.p.shake_y, 100, 50)


def shoot_gun(gun):
    if gun.trigger and gun.weapon_type == 0:
        if gun.shoot_delay == 0:  # 딜레이는 총마다 다르며, 딜레이 수치가 낮을수록 연사 속도가 빠르다. 0이 될 때마다 발사된다.
            gun.shoot = True  # True일시 해당 값을 Target 클래스로 전달하여 Target 클래스의 recoil을 증가시킨다.
            gun.p.shoot_shake = True
            if gun.name == 'SCAR_H':
                gun.flame_display_time = FLAME_DISPLAY_TIME
                gun.shoot_delay = 60
                gun.p.shake_timer = 30
                gun.p.shake_range = 10
        else:
            gun.shoot = False


def wield_melee(gun):
    if gun.use and gun.weapon_type == 1:
        if gun.wield_delay == 0:
            gun.wield = True
            gun.p.shoot_shake = True

            if gun.melee == 'KNIFE':
                gun.melee_x = 100
                gun.melee_deg = 0
                gun.wield_delay = 200
                gun.p.shake_timer = 30
                gun.p.shake_range = 10
        else:
            gun.weild = False


def update_melee_position(gun):
    if gun.melee_x > 0:
        gun.melee_x -= 2


def update_delay(gun):
    if gun.shoot_delay > 0:
        gun.shoot_delay -= 1
    if gun.wield_delay > 0:
        gun.wield_delay -= 1
