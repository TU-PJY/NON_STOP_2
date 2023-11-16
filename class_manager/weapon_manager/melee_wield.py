import random

from game_class.prop import KatanaSlice
from game_work import game_framework, game_manager


def wield_melee(weapon):
    if weapon.use and weapon.weapon_type == 1:
        if weapon.wield_delay <= 0:
            weapon.wield = True
            if weapon.melee == 'KNIFE':
                weapon.melee_x = 100
                weapon.melee_deg = 0
                weapon.wield_delay = 80
                weapon.p.shake_range = 15

            elif weapon.melee == 'BAT':
                weapon.melee_x = 100
                weapon.p.shake_range = 20
                weapon.wield_delay = 250
                weapon.swing_down = True
                weapon.swing = True

            elif weapon.melee == 'RAPIER':
                weapon.rapier_y = random.randint(-10, 10)
                weapon.melee_deg = 0
                weapon.melee_x = 150
                weapon.p.shake_range = 20
                weapon.wield_delay = 45

            elif weapon.melee == 'KATANA':
                weapon.melee_x = 100
                weapon.p.shake_range = 20
                weapon.wield_delay = 140
                weapon.swing_down = True
                weapon.swing = True
        else:
            weapon.wield = False


def set_skill(weapon):
    if weapon.melee == 'RAPIER':
        weapon.p.rotate = 0
        weapon.skill_time = 300
        weapon.skill_enable = True

    elif weapon.melee == 'KATANA' and (weapon.p.mv_right or weapon.p.mv_left):
        if (weapon.p.mv_right and weapon.p.dir == 1) or (weapon.p.mv_left and weapon.p.dir == 0):
            weapon.swing = False
            weapon.swing_down = False
            weapon.swing_up = False
            weapon.p.rotate = 0

            weapon.skill_time = 100
            weapon.p.temp_speed = weapon.p.speed
            weapon.p.speed = 30

            ks = KatanaSlice(weapon.p, weapon)
            game_manager.add_object(ks, 7)

            weapon.skill_enable = True


def melee_skill(weapon):
    if weapon.melee == 'RAPIER':
        if weapon.wield_delay <= 0:
            weapon.rapier_y = random.randint(-10, 10)
            weapon.rapid_x = random.randint(-30, 30)

            weapon.melee_deg = 0
            weapon.melee_x = 150
            weapon.p.shake_range = 20
            weapon.wield_delay = 18

            weapon.wield = True

        else:
            weapon.wield = False

    elif weapon.melee == 'KATANA':
        weapon.p.shake_range = 35
        weapon.p.rotate = 118.8


def update_rapier_player(weapon):
    if weapon.melee == 'RAPIER':
        if weapon.use or weapon.skill_enable:
            weapon.p.rotate = 119
        else:
            weapon.p.rotate = 0


def update_melee_skill(weapon):
    pps = game_framework.pps
    if weapon.skill_time > 0:
        weapon.skill_time -= pps / 3
    else:
        if weapon.melee == 'KATANA':
            weapon.p.speed = weapon.p.temp_speed
            weapon.p.rotate = 0
        weapon.skill_enable = False
        weapon.wield = False


def init_melee(weapon):
    if weapon.melee == 'KATANA' and weapon.skill_enable:
        weapon.p.speed = weapon.p.temp_speed
    weapon.skill_enable = False

    weapon.swing_down = False
    weapon.swing_up = False
    weapon.swing = False
    weapon.melee_deg = 0
