import random

from game_work import game_framework


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
        else:
            weapon.wield = False


def melee_skill(weapon):
    global x
    if weapon.melee == 'RAPIER':
        if weapon.wield_delay <= 0:
            weapon.rapier_y = random.randint(-10, 10)
            weapon.rapid_x = random.randint(-30, 30)
            weapon.melee_deg = 0
            weapon.melee_x = 150
            weapon.p.shake_range = 20
            weapon.wield_delay = 25
            weapon.wield = True

        else:
            weapon.wield = False


def update_melee_skill(weapon):
    pps = game_framework.pps
    if weapon.skill_time > 0:
        weapon.skill_time -= pps / 3
    else:
        weapon.skill_enable = False
        weapon.wield = False
