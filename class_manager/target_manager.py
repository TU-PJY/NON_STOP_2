# 조준점 관련 함수 오음
import random

from pico2d import *

from config import *
from game_work import game_framework

def calc_pps():
    global pps 
    pps = PPS * game_framework.frame_time


def load_target(t):
    t.target_up = load_image(target_up_directory)
    t.target_down = load_image(target_down_directory)
    t.target_right = load_image(target_right_directory)
    t.target_left = load_image(target_left_directory)
    t.target_dot = load_image(target_dot_directory)
    t.not_target = load_image(target_x_directory)
    t.target_melee = load_image(target_melee_directory)


def draw_target(t):
    if t.weapon.weapon_type == 0:
        t.target_up.draw(t.p.mx, t.p.my + t.recoil + t.dis2, 60, 60)
        t.target_down.draw(t.p.mx, t.p.my - t.recoil - t.dis2, 60, 60)
        t.target_right.draw(t.p.mx + t.recoil + t.dis2, t.p.my, 60, 60)
        t.target_left.draw(t.p.mx - t.recoil - t.dis2, t.p.my, 60, 60)

    elif t.weapon.weapon_type == 1:
        t.not_target.draw(t.p.mx, t.p.my, 120, 120)
        t.tmy = t.p.y + t.p.camera_y - t.p.land_y

        if t.weapon.melee == 'KNIFE':
            if t.p.dir == 1:
                t.tmx = t.p.camera_x + t.p.x + 170
                t.target_melee.composite_draw(0, '', t.tmx, t.tmy, 100, 150)
            elif t.p.dir == 0:
                t.tmx = t.p.camera_x + t.p.x - 170
                t.target_melee.composite_draw(0, 'h', t.tmx, t.tmy, 100, 150)

    # if t.target_dot_display_time > 0:
    #     t.target_dot.draw(t.tx, t.ty, 30, 30)


def update_target(t):
    global pps 
    t.dis = math.sqrt((t.p.mx - WIDTH / 2) ** 2 + (t.p.y - t.p.my) ** 2)

    if t.recoil > 0:
        t.recoil -= pps / 7
    else:
        t.recoil = 0

    if t.dis < 0:  # 분산도가 0 밑으로 내려가지 않도록 한다.
        t.dis = 0

    if t.weapon.gun == 'SCAR_H':
        # empty randrange 방지를 위해 35를 더해야 함
        t.dis2 = t.dis / 20 + 35  # 나누는 숫자가 작을 수록 분산도가 커진다.
        if t.weapon.shoot:
            t.recoil += 20  # 총기마다 반동 수치가 달라 조준점이 벌어지는 정도가 다르다.

    elif t.weapon.gun == 'M16':
        t.dis2 = t.dis / 30 + 35
        if t.weapon.shoot:
            t.recoil += 15

    elif t.weapon.gun == 'MP44':
        t.dis2 = t.dis / 35 + 35
        if t.weapon.shoot:
            t.recoil += 30

    elif t.weapon.gun == 'AUG':
        t.dis2 = t.dis / 45 + 35
        if t.weapon.shoot:
            t.recoil += 16

    elif t.weapon.gun == 'GROZA':
        t.dis2 = t.dis / 40 + 35
        if t.weapon.shoot:
            t.recoil += 13

    elif t.weapon.gun == 'AKS74':
        t.dis2 = t.dis / 30 + 35
        if t.weapon.shoot:
            t.recoil += 13

    elif t.weapon.gun == 'UMP':
        t.dis2 = t.dis / 25 + 35
        if t.weapon.shoot:
            t.recoil += 17

    elif t.weapon.gun == 'VECTOR':
        t.dis2 = t.dis / 12 + 35
        if t.weapon.shoot:
            t.recoil += 8

    elif t.weapon.gun == 'THOMPSON':
        t.dis2 = t.dis / 20 + 35
        if t.weapon.shoot:
            t.recoil += 17

    elif t.weapon.gun == 'P90':
        t.dis2 = t.dis / 20 + 35
        if t.weapon.shoot:
            t.recoil += 13

    if t.target_dot_display_time > 0:
        t.target_dot_display_time -= pps / 3


def make_target_point(t):  # 이 함수에서 생성되는 좌표로 적 피격을 판정한다.
    if t.weapon.shoot:
        t.target_dot_display_time = TARGET_DOT_DISPLAY_TIME  # 해당 시간 동안 조준점 내부에 점이 보인다.
        t.tx = random.randint \
            (t.p.mx - int(t.recoil) - int(t.dis2) + 31, t.p.mx + int(t.recoil) + int(t.dis2) - 31)
        t.ty = random.randint \
            (t.p.my - int(t.recoil) - int(t.dis2) + 31, t.p.my + int(t.recoil) + int(t.dis2) - 31)
