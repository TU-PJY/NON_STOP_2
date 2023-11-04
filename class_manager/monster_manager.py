import math

from pico2d import *

from config import *
from game_class.prop import Arrow
from game_work import game_manager, game_framework


def load_monster(self):
    if self.type == 1:
        self.type1 = load_image(type1_directory)
    elif self.type == 2:
        self.type2 = load_image(type2_directory)
    elif self.type == 3:
        self.type3 = load_image(type3_directory)
    elif self.type == 4:
        self.type4 = load_image(type4_directory)


def draw_monster(m):
    if m.type == 1:
        if m.dir == 0:
            m.type1.clip_composite_draw \
                (int(m.frame) * 64, 0, 64, 64, 0, '', m.x + m.p.efx, m.y + m.p.efy + m.size / 3, 280, 280 + m.size)
        elif m.dir == 1:
            m.type1.clip_composite_draw \
                (int(m.frame) * 64, 0, 64, 64, 0, 'h', m.x + m.p.efx, m.y + m.p.efy + m.size / 3, 280, 280 + m.size)
        draw_rectangle \
            (m.x - 50 + m.p.efx, m.y + 50 + m.p.efy, m.x + 50 + m.p.efx, m.y - 70 + m.p.efy)

    if m.type == 2:
        if m.dir == 0:
            m.type2.clip_composite_draw \
                (int(m.frame) * 128, 0, 128, 128, 0, '', m.x + m.p.efx, m.y + m.p.efy, 400, 400 + m.size)
        elif m.dir == 1:
            m.type2.clip_composite_draw \
                (int(m.frame) * 128, 0, 128, 128, 0, 'h', m.x + m.p.efx, m.y + m.p.efy, 400, 400 + m.size)
        draw_rectangle \
            (m.x - 65 + m.p.efx, m.y + 65 + m.p.efy, m.x + 65 + m.p.efx, m.y - 65 + m.p.efy)

    if m.type == 3:
        if m.dir == 0:
            m.type3.clip_composite_draw \
                (int(m.frame) * 128, 0, 128, 128, 0, '', m.x + m.p.efx, m.y + m.p.efy + m.size2 / 3 + m.size / 5,
                 300, 300 + m.size2 + m.size)
        elif m.dir == 1:
            m.type3.clip_composite_draw \
                (int(m.frame) * 128, 0, 128, 128, 0, 'h', m.x + m.p.efx, m.y + m.p.efy + m.size2 / 3 + m.size / 5,
                 300, 300 + m.size2 + m.size)
        draw_rectangle \
            (m.x - 60 + m.p.efx, m.y + 60 + m.p.efy, m.x + 60 + m.p.efx, m.y - 60 + m.p.efy)

    if m.type == 4:
        if m.dir == 0:
            m.type4.clip_composite_draw \
                (int(m.frame) * 128, 0, 128, 128, 0, '', m.x + m.p.efx, m.y + m.p.efy, 450, 450)
        elif m.dir == 1:
            m.type4.clip_composite_draw \
                (int(m.frame) * 128, 0, 128, 128, 0, 'h', m.x + m.p.efx, m.y + m.p.efy, 450, 450)
        draw_rectangle \
            (m.x - 55 + m.p.efx, m.y + 55 + m.p.efy, m.x + 55 + m.p.efx, m.y - 55 + m.p.efy)


def update_monster_size(m):
    pps = PPS * game_framework.frame_time
    if m.size > 0:
        m.size -= 2 * pps / 3


def move_monster(m):
    pps = PPS * game_framework.frame_time

    m.dir = 1 if m.p.x > m.x else 0

    if not m.is_attack and m.attack_motion_time <= 0:
        if not m.p.x - 5 <= m.x <= m.p.x + 5:
            if m.dir == 0:
                m.x -= m.speed * pps / 4
            elif m.dir == 1:
                m.x += m.speed * pps / 4

        if m.type == 2 and m.y < 670:  # 670보다 낮게 있으면 자기 자리로 복귀한다
            m.y += pps / 4
            if m.y >= 670:
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
                    m.acc_delay = 0
                    m.jump_delay = 350  # 점프 타이밍이 존재

                m.jump_acc -= pps / 90

            if m.jump_delay > 0:
                m.jump_delay -= pps / 3


def monster_animation(m):
    pps = PPS * game_framework.frame_time
    # all type animation except type 3
    if not m.is_attack and m.attack_motion_time <= 0 and not m.type == 3:  # type3은 프레임 업데이트를 하지 않음
        m.frame = (m.frame + APT * FPA * game_framework.frame_time) % 2

    # type 3 animation
    if m.type == 3:
        if m.size_up:
            m.size_deg += 0.005 * pps / 5
            if m.size_deg >= 0.4:
                m.size_deg, m.size_up = 0.4, False

        elif not m.size_up:
            m.size_deg -= 0.005 * pps / 5
            if m.size_deg <= 0:
                m.size_deg, m.size_up = 0, True

        if not m.is_jump:
            m.size2 = math.sin(m.size_deg) * 100
            m.frame = 0

        if m.is_jump:  # 점프 시 프레임이 다름
            m.frame = 1
            m.size2 = 0


def process_attack(m):
    pps = PPS * game_framework.frame_time
    # type 1 attack
    if m.type == 1:
        m.is_attack = True if math.sqrt((m.x - m.p.x) ** 2 + (m.p.y - m.y + (m.p.y - 250) / 1.5) ** 2) <= 100 else False
        if m.is_attack:
            if m.atk_delay <= 0:
                m.attack_motion_time = 50
                m.atk_delay = 200
                m.size = 100

            if m.attack_motion_time > 0:
                m.frame = 2
            else:
                m.frame = 1

    # type 2 attack
    if m.type == 2:
        if math.sqrt((m.p.x - m.x) ** 2 + (m.p.y - m.y + (m.p.y - 250) / 1.5) ** 2) <= 110 and not m.is_dash:  # 접촉
            if m.atk_delay <= 0:
                m.size = 200
                m.atk_delay = 200

        if m.mp.playerToWallLeft + 100 < m.x < m.mp.playerToWallRight - 100:  # 스폰 지점에서 바로 대쉬하지 않도록
            if m.dash_delay <= 0:
                if math.sqrt((m.x - m.p.x) ** 2 + (m.y - m.p.y) ** 2) <= 800 and not m.is_attack and m.atk_delay <= 0:
                    m.incline = math.atan2(m.p.y - m.y + ((m.p.y - 250) / 1.5), m.p.x - m.x)
                    m.temp_x, m.temp_y = m.p.x, m.p.y + ((m.p.y - 250) / 1.5)
                    m.is_dash = True
                    m.is_attack = True

        if m.is_dash:  # True일 시 대쉬 공격
            m.frame = 3
            m.x += 6 * math.cos(m.incline) * pps / 4
            m.y += 6 * math.sin(m.incline) * pps / 4

            if math.sqrt((m.p.x - m.x) ** 2 + (m.p.y - m.y + (m.p.y - 250) / 1.5) ** 2) <= 100:  # 대쉬 접촉
                m.size = 200

            if m.temp_x - 10 <= m.x <= m.temp_x + 10 and m.temp_y - 10 <= m.y <= m.temp_y + 10:
                m.dash_delay = 650
                m.is_dash = False
                m.is_attack = False

    # type 3 attack
    if m.type == 3:
        if math.sqrt((m.p.x - m.x) ** 2 + (m.p.y - m.y + (m.p.y - 250) / 1.5) ** 2) <= 110:
            if m.atk_delay <= 0:
                m.size = 200
                m.atk_delay = 200

    # type 4 attack
    if m.type == 4:
        if m.mp.playerToWallLeft + 100 <= m.x <= m.mp.playerToWallRight - 100:
            if math.sqrt((m.p.x - m.x) ** 2 + (m.p.y - m.y + (m.p.y - 250) / 1.5) ** 2) <= 700:
                m.is_attack = True
            else:
                m.is_attack = False
                m.shoot_delay = 150

            if m.is_attack:
                m.incline = math.atan2(m.p.y - m.y, m.p.x - m.x)
                m.frame = 2
                if m.shoot_delay <= 0:
                    ar = Arrow(m.p, m.mp, m.x, m.y, m.incline, m.dir)  # 일정 간격으로 화살을 발사한다
                    game_manager.add_object(ar, 2)
                    m.shoot_delay = 400


def damage_monster(m):
    if m.weapon.shoot:
        m.dispx = m.x + m.p.efx
        m.dispy = m.y + m.p.efy

        if m.type == 1:  # 몬스터가 총에 맞았는지 판정한다.
            m.hit = True if m.dispx - 50 <= m.target.tx <= m.dispx + 50 and \
                            m.dispy - 70 <= m.target.ty <= m.dispy + 50 else False
        if m.type == 2:
            m.hit = True if m.dispx - 65 <= m.target.tx <= m.dispx + 65 and \
                            m.dispy - 65 <= m.target.ty <= m.dispy + 65 else False
        if m.type == 3:
            m.hit = True if m.dispx - 60 <= m.target.tx <= m.dispx + 60 and \
                            m.dispy - 60 <= m.target.ty <= m.dispy + 60 else False
        if m.type == 4:
            m.hit = True if m.dispx - 55 <= m.target.tx <= m.dispx + 55 and \
                            m.dispy - 55 <= m.target.ty <= m.dispy + 55 else False

        if m.hit:  # 맞은걸로 판정되면 대미지를 가한다.
            if m.weapon.gun == 'SCAR_H':
                m.hp -= 30
            elif m.weapon.gun == 'M16':
                m.hp -= 25
            elif m.weapon.gun == 'MP44':
                m.hp -= 45

            m.hit = False

    if m.hp <= 0:  # hp가 0이 될 경우 죽는다.
        game_manager.remove_object(m)


def update_delay(m):
    pps = PPS * game_framework.frame_time
    if m.attack_motion_time > 0:
        m.attack_motion_time -= pps / 3
    if m.atk_delay > 0:
        m.atk_delay -= pps / 3
    if m.dash_delay > 0:
        m.dash_delay -= pps / 3
    if m.shoot_delay > 0:
        m.shoot_delay -= pps / 3


def update_monster_pos(m):
    pps = PPS * game_framework.frame_time
    if m.p.mv_right:
        m.x -= m.p.speed * pps / 4
        m.temp_x -= m.p.speed * pps / 4
    elif m.p.mv_left:
        m.x += m.p.speed * pps / 4
        m.temp_x += m.p.speed * pps / 4
