import math

from game_class.prop import Arrow
from game_work import game_framework, game_manager


# cam_h는 플레이어와 상대적 위치 차이를 발생시키기 때문에 몬스터 y위치에 cam_h를 포함해줘야함
def process_attack(m):
    from game_class.monster import Monster

    pps = game_framework.pps
    # type 1 attack
    if m.type == 1:
        if m.is_attack:
            if m.attack_motion_time > 0:
                m.frame = 2
            else:
                m.frame = 1
                m.is_attack = False

    # type 2 attack
    if m.type == 2:
        if m.mp.playerToWallLeft - 23 < m.x < m.mp.playerToWallRight + 23:  # 스폰 지점에서 바로 대쉬하지 않도록
            if m.dash_delay <= 0 and not m.is_attack and m.atk_delay <= 0:
                if math.sqrt((m.x - m.p.x) ** 2 + ((m.y + m.p.cam_h) - m.p.y) ** 2) <= 600:
                    m.incline = math.atan2(m.p.y - (m.y + m.p.cam_h), m.p.x - m.x)
                    m.temp_x, m.temp_y = m.p.x, m.p.y - m.p.cam_h
                    m.is_dash = True
                    m.is_attack = True

        if m.is_dash:  # True일 시 대쉬 공격
            m.frame = 3
            m.x += 5 * math.cos(m.incline) * pps / 4
            m.y += 5 * math.sin(m.incline) * pps / 4

            if m.temp_x - 40 <= m.x <= m.temp_x + 40 and m.temp_y - 40 <= m.y <= m.temp_y + 40:
                m.dash_delay = 700
                m.is_dash = False
                m.is_attack = False

    # type 3 attack
    if m.type == 3:
        pass

    # type 4 attack
    if m.type == 4:
        if m.mp.playerToWallLeft + 25 <= m.x <= m.mp.playerToWallRight - 25:
            if math.sqrt((m.p.x - m.x) ** 2 + (m.p.y - (m.y + m.p.cam_h)) ** 2) <= 750:
                m.is_attack = True
            else:
                m.is_attack = False
                m.shoot_delay = 150

            if m.is_attack:
                m.incline = math.atan2(m.p.y + 70 - (m.y + m.p.cam_h), m.p.x - m.x)  # 머리쪽으로 살짝 높혀서 쏜다
                m.frame = 2
                if m.shoot_delay <= 0:
                    Monster.bow.play()
                    ar = Arrow(m.p, m.mp, m.x, m.y, m.incline, m.dir)  # 일정 간격으로 화살을 발사한다
                    game_manager.add_collision_pair('player:arrow', None, ar)
                    game_manager.add_object(ar, 2)
                    m.shoot_delay = 550
