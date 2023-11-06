# 화면 효과 함수 모음
import random

from config import *
from game_work import game_framework


def push_display(p):
    pps = PPS * game_framework.frame_time
    if p.land_y > 0:
        p.land_y -= pps / 2
    if p.land_y <= 0:
        p.land_y = 0


def shake_display(p):
    pps = PPS * game_framework.frame_time
    if not p.shake_range - pps / 8 < 0:  # empty randrange 방지
        p.shake_x = random.randint(-int(p.shake_range), int(p.shake_range))
        p.shake_y = random.randint(-int(p.shake_range), int(p.shake_range))
        p.shake_range -= pps / 8
    else:
        p.shake_x = 0
        p.shake_y = 0


def update_camera(p):
    p.camera_y = (p.y - p.my) / 3
    p.camera_x = (p.x - p.mx) / 3
