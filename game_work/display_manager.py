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
    if p.shake_time > 0:
        p.shake_x = random.randint(-p.shake_range, p.shake_range)
        p.shake_y = random.randint(-p.shake_range, p.shake_range)
        p.shake_time -= pps / 3
    else:
        p.shake_x = 0
        p.shake_y = 0


def update_camera(p):
    p.camera_y = (p.y - p.my) / 3
    p.camera_x = (p.x - p.mx) / 3
