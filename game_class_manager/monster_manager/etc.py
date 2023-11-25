import math

from config import *
from game_work import game_framework


def monster_animation(m):
    pps = game_framework.pps
    if not m.is_attack and m.attack_motion_time <= 0 and not m.type == 3:  # type3은 프레임 업데이트를 하지 않음
        m.frame = (m.frame + APT * FPA * game_framework.frame_time) % 2

    # type 3 animation
    if m.type == 3:
        m.size_deg += 1 * pps / 80
        if not m.is_jump:
            m.size2 = math.sin(m.size_deg) / 6  # 위 아래로 rubber animation 출력
            m.frame = 0
        if m.is_jump:  # 점프 시 프레임이 다름
            m.frame = 1
            m.size2 = 0


def update_delay(m):  # 몬스터 관련 딜레이 업데이트
    pps = game_framework.pps
    if m.attack_motion_time > 0:
        m.attack_motion_time -= pps / 3
    if m.atk_delay > 0:
        m.atk_delay -= pps / 3
    if m.type == 2 and m.dash_delay > 0:
        m.dash_delay -= pps / 3
    if m.type == 4 and m.shoot_delay > 0:
        m.shoot_delay -= pps / 3
    if m.type == 3 and m.jump_delay > 0:
        m.jump_delay -= pps / 3


def update_monster_size(m):  # 몬스터 공격 피드백 관리
    pps = game_framework.pps
    if m.size > 0:
        m.size -= 2 * pps / 3


def update_monster_opacify(m):  # 몬스터 대미지 피드백 관리
    pps = game_framework.pps
    if m.op > 0:
        m.op -= int(4 * pps / 3)
        if m.op < 0:
            m.op = 0


def update_monster_pos(m):  # 화면 상의 몬스터 위치 업데이트
    speed = game_framework.pps * m.p.speed
    if m.p.mv_right:
        m.x -= speed
        if m.type == 2:
            m.temp_x -= speed

    elif m.p.mv_left:
        m.x += speed
        if m.type == 2:
            m.temp_x += speed
