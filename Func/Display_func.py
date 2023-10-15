# 화면 효과 함수 모음
from Env_variable import *
import random


def push_display(p):
    if p.land_y > 0:
        p.land_y -= LAND_SHAKE_REDUCE


def shake_display(p):
    if p.shake_time > 0:
        p.shake_x = random.randint(-p.shake_range, p.shake_range)
        p.shake_y = random.randint(-p.shake_range, p.shake_range)
        p.shake_time -= 1
    else:
        p.shake_x = 0
        p.shake_y = 0
