from config import *
from game_work import game_framework


def move_monster(m):
    pps = game_framework.pps
    m.dir = 1 if m.p.x > m.x else 0

    if not m.knockback:  # 넉백 시간 동안에는 움직이지 못한다.
        if not m.is_attack and m.attack_motion_time <= 0:
            if not m.p.x - 5 <= m.x <= m.p.x + 5:  # 몬스터 제자리 와리가리 방지
                if m.dir == 0:
                    m.x -= m.speed * pps / 4
                elif m.dir == 1:
                    m.x += m.speed * pps / 4

    if m.knockback:
        match m.knockback_dir:
            case 1:
                back = -1
            case 0:
                back = 1

        m.x += m.back_acc * back
        m.back_acc -= pps / 20

        if m.x < m.mp.playerToWallLeft or m.x > m.mp.playerToWallRight:  # 벽 뒤로 밀리지 않게 한다
            m.x += m.back_acc * -back

        if m.back_acc <= 0:
            m.knockback = False

    if m.type == 2 and not m.is_dash:
        if m.y < 670:  # 670보다 낮게 있으면 자기 자리로 복귀한다
            m.y += 2 * pps / 4
            if m.y >= 670:
                m.y = 670
        elif m.y > 670:  # 670보다 높게 있으면 자기 자리로 복귀한다
            m.y -= 2 * pps / 4
            if m.y <= 670:
                m.y = 670

    if m.type == 3:
        if not m.is_jump and m.jump_delay <= 0:  # 점프하면서 이동
            m.jump_acc = JUMP_ACC
            m.is_jump = True

        if m.is_jump:
            m.y += m.jump_acc * pps / 2.5

            if m.y <= 230 and m.jump_acc < 0:  # 땅에 착지할 경우
                m.y = 230
                m.is_jump = False
                m.jump_delay = 330  # 점프 타이밍이 존재

            m.jump_acc -= pps / 90
