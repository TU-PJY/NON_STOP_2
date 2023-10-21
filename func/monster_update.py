from pico2d import *
from Env_variable import *
import math


def load_monster(self):
    self.type1 = load_image(type1_directory)


def draw_monster(m):
    if m.type == 1:
        if m.dir == 0:
            m.type1.clip_composite_draw\
                (m.frame * 64, 0, 64, 64, 0, '', m.x + m.p.efx, m.y + m.p.efy, 250, 250)
        elif m.dir == 1:
            m.type1.clip_composite_draw\
                (m.frame * 64, 0, 64, 64, 0, 'h', m.x + m.p.efx,m.y + m.p.efy, 250, 250)

        draw_rectangle\
            (m.x - 50 + m.p.efx, m.y + 50 + m.p.efy, m.x + 50 + m.p.efx, m.y - 70 + m.p.efy)



def move_monster(m):
    m.dir = 1 if m.p.x > m.x else 0
    if not m.is_attack and m.attack_motion_time == 0:
        if m.dir == 0:
            m.x -= m.speed
        elif m.dir == 1:
            m.x += m.speed


def update_frame(m):
    if not m.is_attack and m.attack_motion_time == 0:
        if m.fdelay == 0:
            m.frame = (m.frame + 1) % 2
            m.fdelay = 70
        else:
            m.fdelay -= 1


def process_attack(m):
    if m.type == 1:
        if math.sqrt((m.x - m.p.x) ** 2 + (m.y - m.p.y) ** 2) <= 100:
            m.is_attack = True
        else:
            m.is_attack = False

        if m.is_attack:
            if m.atk_delay == 0:
                m.attack_motion_time = 50
                m.atk_delay = 150

            if m.attack_motion_time > 0:
                m.frame = 2
            else:
                m.frame = 1


def update_delay(m):
    if m.attack_motion_time > 0:
        m.attack_motion_time -= 1
    if m.atk_delay > 0:
        m.atk_delay -= 1


def update_monster_pos(m):
    if m.p.mv_right:
        m.x -= m.p.speed
    elif m.p.mv_left:
        m.x += m.p.speed
