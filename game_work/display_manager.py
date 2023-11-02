# 화면 효과 함수 모음
from config import *
import random

from game_work import game_framework


def push_display(p):
    speed = PLAYER_PPS * game_framework.frame_time
    if p.land_y > 0:
        p.land_y -= speed / 2


def shake_display(p):
    if p.shake_time > 0:
        p.shake_x = random.randint(-p.shake_range, p.shake_range)
        p.shake_y = random.randint(-p.shake_range, p.shake_range)
        p.shake_time -= 1
    else:
        p.shake_x = 0
        p.shake_y = 0


def update_camera(p):
    p.camera_y = (p.y - p.my) / 3
    p.camera_x = (p.x - p.mx) / 3
