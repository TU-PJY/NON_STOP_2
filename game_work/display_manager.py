# 화면 효과 함수 모음
import random

from game_work import game_framework


def process_effect(p):  # 화면 효과 최종 계산
    p.wx = p.x + p.shake_x + p.shake_dx + p.shake_ex + p.cam_x  # 무기 출력 좌표, weapon x, weapon y
    p.wy = p.y + p.shake_y + p.shake_dy + p.shake_ey + p.cam_y - p.push_y + p.size * 50

    p.px = p.wx  # 플레이어 출력 좌표, player x, player y
    p.py = p.wy

    # 디스플레이 효과만 사용할때 쓰는 값, 무기, 플레이어를 제외한 객체 좌표에 사용
    p.ex = p.shake_ex + p.shake_x + p.shake_dx + p.cam_x
    p.ey = p.shake_ey + p.shake_y + p.shake_dy + p.cam_y + p.cam_h - p.push_y
    pass


def push_display(p):  # 플레이어가 바닥에 착지하면 화면이 밑으로 눌린다
    pps = game_framework.pps

    if p.push_y > 0:  # 눌린 화면이 점차 복구
        p.push_y -= pps / 2
    if p.push_y <= 0:
        p.push_y = 0
    pass


def shake_display(p):  # 총기 및 근접무기 사용 시의 화면 흔들림
    pps = game_framework.pps

    if not p.shake_range - pps / 8 < 0:  # empty randrange 방지
        p.shake_x = random.randint(-int(p.shake_range), int(p.shake_range))
        p.shake_y = random.randint(-int(p.shake_range), int(p.shake_range))
        p.shake_range -= pps / 8
    else:
        p.shake_x = 0
        p.shake_y = 0


def dmg_shake(p):  # 플레이어 대미지 받을 시의 화면 흔들림
    pps = game_framework.pps
    if not p.dmg_shake_range / 8 < 0:
        p.shake_dx = random.randint(-int(p.dmg_shake_range), int(p.dmg_shake_range))
        p.shake_dy = random.randint(-int(p.dmg_shake_range), int(p.dmg_shake_range))
        p.dmg_shake_range -= pps / 8
    else:
        p.shake_dx = 0
        p.shake_dy = 0


def explode_shake(p):  # 폭발물 폭발 시의 화면 흔들림
    pps = game_framework.pps
    if not p.ex_shake_range / 8 < 0:
        p.shake_ex = random.randint(-int(p.ex_shake_range), int(p.ex_shake_range))
        p.shake_ey = random.randint(-int(p.ex_shake_range), int(p.ex_shake_range))
        p.ex_shake_range -= pps / 8
    else:
        p.shake_ex = 0
        p.shake_ey = 0


def update_camera(p):  # 마우스 좌표에 따라 카메라를 실시간으로 업데이트
    p.cam_y = (p.y - p.my) / 3
    p.cam_x = (p.x - p.mx) / 3
    p.cam_h = - (p.y - 250) / 1.5
    pass
