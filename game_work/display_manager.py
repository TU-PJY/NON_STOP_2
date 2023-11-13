# 화면 효과 함수 모음
import random

from game_work import game_framework


def process_effect(p):
    p.wx = p.x + p.shake_x + p.cam_x  # 무기 출력 좌표, weapon x, weapon y
    p.wy = p.y + p.shake_y + p.cam_y - p.push_y + p.size * 50

    p.px = p.wx  # 플레이어 출력 좌표, player x, player y
    p.py = p.wy

    p.ex = p.shake_x + p.cam_x  # 디스플레이 효과만 사용할때 쓰는 값, 무기, 플레이어를 제외한 객체에 사용
    p.ey = p.shake_y + p.cam_y + p.cam_h - p.push_y  # effect x, effect y
    pass


def push_display(p):
    pps = game_framework.pps

    if p.push_y > 0:
        p.push_y -= pps / 2
    if p.push_y <= 0:
        p.push_y = 0
    pass


def shake_display(p):
    pps = game_framework.pps

    if not p.shake_range - pps / 8 < 0:  # empty randrange 방지
        p.shake_x = random.randint(-int(p.shake_range), int(p.shake_range))
        p.shake_y = random.randint(-int(p.shake_range), int(p.shake_range))
        p.shake_range -= pps / 8
        # p.scope_rot = p.shake_x / 200
    else:
        p.shake_x = 0
        p.shake_y = 0
        p.scope_rot = 0
    pass


def update_camera(p):
    p.cam_y = (p.y - p.my) / 3
    p.cam_x = (p.x - p.mx) / 3
    p.cam_h = - (p.y - 250) / 1.5
    pass
