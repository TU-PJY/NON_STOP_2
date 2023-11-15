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
