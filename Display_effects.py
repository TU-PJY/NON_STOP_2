# 화면 효과 함수 모음
from Env_variable import LAND_SHAKE_REDUCE
import random


def push_display(p):
    if p.land_shake:  # 땅 흔들림 활성화 시 화면 전체가 흔들린다.
        if p.land_y > 0:
            p.land_y -= LAND_SHAKE_REDUCE
        else:
            p.land_shake = False


def shake_display(p):
    if p.shoot_shake:
        if p.shake_timer > 0:
            p.shake_x = random.randint(-p.shake_range, p.shake_range)
            p.shake_y = random.randint(-p.shake_range, p.shake_range)
            p.shake_timer -= 1
        else:
            p.shake_x = 0
            p.shake_y = 0
            p.shoot_shake = False
