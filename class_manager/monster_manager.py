from pico2d import *
from config import *
import math


def load_monster(self):
    self.type1 = load_image(type1_directory)
    self.type2 = load_image(type2_directory)
    self.type3 = load_image(type3_directory)


def draw_monster(m):
    if m.type == 1:
        if m.dir == 0:
            m.type1.clip_composite_draw \
                (m.frame * 64, 0, 64, 64, 0, '', m.x + m.p.efx, m.y + m.p.efy + m.size / 3, 300, 300 + m.size)
        elif m.dir == 1:
            m.type1.clip_composite_draw \
                (m.frame * 64, 0, 64, 64, 0, 'h', m.x + m.p.efx, m.y + m.p.efy + m.size / 3, 300, 300 + m.size)
        draw_rectangle \
            (m.x - 50 + m.p.efx, m.y + 50 + m.p.efy, m.x + 50 + m.p.efx, m.y - 70 + m.p.efy)

    if m.type == 2:
        if m.dir == 0:
            m.type2.clip_composite_draw \
                (m.frame * 128, 0, 128, 128, 0, '', m.x + m.p.efx, m.y + m.p.efy, 300, 300 + m.size)
        elif m.dir == 1:
            m.type2.clip_composite_draw \
                (m.frame * 128, 0, 128, 128, 0, 'h', m.x + m.p.efx, m.y + m.p.efy, 300, 300 + m.size)
        draw_rectangle \
            (m.x - 40 + m.p.efx, m.y + 40 + m.p.efy, m.x + 40 + m.p.efx, m.y - 40 + m.p.efy)

    if m.type == 3:
        if m.dir == 0:
            m.type3.clip_composite_draw \
                (m.frame * 128, 0, 128, 128, 0, '', m.x + m.p.efx, m.y + m.p.efy + m.size2 / 3 + m.size / 5,
                 300, 300 + m.size2 + m.size)
        elif m.dir == 1:
            m.type3.clip_composite_draw \
                (m.frame * 128, 0, 128, 128, 0, 'h', m.x + m.p.efx, m.y + m.p.efy + m.size2 / 3 + m.size / 5,
                 300, 300 + m.size2 + m.size)
        draw_rectangle \
            (m.x - 60 + m.p.efx, m.y + 60 + m.p.efy, m.x + 60 + m.p.efx, m.y - 60 + m.p.efy)


def move_monster(m):
    m.dir = 1 if m.p.x > m.x else 0
    if not m.is_attack and m.attack_motion_time == 0:
        if not m.p.x - 5 <= m.x <= m.p.x + 5:
            if m.dir == 0:
                m.x -= m.speed
            elif m.dir == 1:
                m.x += m.speed

        if m.type == 2 and m.y < 650:  # 650보다 낮게 있으면 자기 자리로 복귀한다
            m.y += 1

        if m.type == 3:
            if not m.is_jump and m.jump_delay == 0:  # 점프하면서 이동
                m.jump_acc = JUMP_ACC
                m.is_jump = True

            if m.is_jump:
                m.y += m.jump_acc * 2

                if m.acc_delay == 0:
                    m.jump_acc -= 1
                    m.acc_delay = ACC_DELAY
                else:
                    m.acc_delay -= 1

                if m.y <= 230 and m.jump_acc < 0:  # 땅에 착지할 경우
                    m.y = 230
                    m.is_jump = False
                    m.acc_delay = 0
                    m.jump_delay = 250  # 점프 타이밍이 존재

            if m.jump_delay > 0:
                m.jump_delay -= 1


def monster_animation(m):
    if not m.is_attack and m.attack_motion_time == 0 and not m.type == 3:
        if m.fdelay == 0:
            m.frame = (m.frame + 1) % 2
            m.fdelay = 70
        else:
            m.fdelay -= 1

    if m.type == 3:
        if m.size_up:
            m.size_deg += 0.005
            if m.size_deg >= 0.4:
                m.size_deg, m.size_up = 0.4, False

        elif not m.size_up:
            m.size_deg -= 0.005
            if m.size_deg <= 0:
                m.size_deg, m.size_up = 0, True

        if not m.is_jump:
            m.size2 = math.sin(m.size_deg) * 100

        if m.is_jump:  # 점프 시 프레임이 다름
            m.frame = 1
            m.size2 = 0
        else:
            m.frame = 0


def process_attack(m):
    if m.type == 1:
        m.is_attack = True if math.sqrt((m.x - m.p.x) ** 2 + (m.p.y - m.y + (m.p.y - 250) / 1.5) ** 2) <= 100 else False
        if m.is_attack:
            if m.atk_delay == 0:
                m.attack_motion_time = 50
                m.atk_delay = 150
                m.size = 100

            if m.attack_motion_time > 0:
                m.frame = 2
            else:
                m.frame = 1

    if m.type == 2:
        if math.sqrt((m.p.x - m.x) ** 2 + (m.p.y - m.y + (m.p.y - 250) / 1.5) ** 2) <= 100 and not m.is_dash:  # 공중 접촉
            if m.atk_delay == 0:
                m.size = 150
                m.atk_delay = 150

        if m.p.p_to_wall_left + 100 < m.x < m.p.p_to_wall_right - 100:  # 스폰 지점에서 바로 대쉬하지 않도록
            if m.dash_delay == 0:
                if math.sqrt((m.x - m.p.x) ** 2 + (m.y - m.p.y) ** 2) <= 800 and not m.is_attack and m.atk_delay == 0:
                    m.incline = math.atan2(m.p.y - m.y, m.p.x - m.x)
                    m.temp_x, m.temp_y = m.p.x, m.p.y
                    m.is_dash = True
                    m.is_attack = True
                    m.f_delay = 0

        if m.is_dash:  # True일 시 대쉬 공격
            m.frame = 3
            m.x += 6 * math.cos(m.incline)
            m.y += 6 * math.sin(m.incline)

            if math.sqrt((m.p.x - m.x) ** 2 + (m.p.y - m.y + (m.p.y - 250) / 1.5) ** 2) <= 100:  # 대쉬 접촉
                m.size = 150

            if m.temp_x - 10 <= m.x <= m.temp_x + 10 and m.temp_y - 10 <= m.y <= m.temp_y + 10:
                m.dash_delay = 600
                m.is_dash = False
                m.is_attack = False

    if m.type == 3:
        if math.sqrt((m.p.x - m.x) ** 2 + (m.p.y - m.y + (m.p.y - 250) / 1.5) ** 2) <= 110:
            if m.atk_delay == 0:
                m.size = 200
                m.atk_delay = 150


def update_delay(m):
    if m.attack_motion_time > 0:
        m.attack_motion_time -= 1
    if m.atk_delay > 0:
        m.atk_delay -= 1
    if m.dash_delay > 0:
        m.dash_delay -= 1


def update_monster_size(m):
    if m.size > 0:
        m.size -= 2


def update_monster_pos(m):
    if m.p.mv_right:
        m.x -= m.p.speed
        m.temp_x -= m.p.speed
    elif m.p.mv_left:
        m.x += m.p.speed
        m.temp_x += m.p.speed
