from class_manager.weapon_manager.etc import make_shell
from game_work import game_framework


def spin_win(weapon):
    pps = game_framework.pps
    if weapon.shoot_delay < 200:
        if not weapon.shell_out:  # 장전하는 순간 탄피를 1회만 생성한다.
            make_shell(weapon, 20, 20)
            weapon.shell_out = True

        if weapon.spin < 6:
            weapon.spin += pps / 30
            if weapon.spin >= 6:
                weapon.spin = 0
                weapon.is_spin = False
                weapon.shell_out = False


def update_melee_position(weapon):
    pps = game_framework.pps
    if weapon.melee == 'RAPIER':
        if weapon.skill_enable:
            if weapon.melee_x > 0:
                weapon.melee_x -= pps * 4
            else:
                weapon.melee_x = 0
        else:
            if weapon.melee_x > 0:
                weapon.melee_x -= pps * 2
            else:
                weapon.melee_x = 0

    else:
        if weapon.melee_x > 0:
            weapon.melee_x -= pps / 2
        else:
            weapon.melee_x = 0


def update_rapier_player(weapon):
    if weapon.melee == 'RAPIER':
        if weapon.use or weapon.skill_enable:
            weapon.p.rotate = 119
        else:
            weapon.p.rotate = 0


def swing(weapon):
    pps = game_framework.pps

    if weapon.swing_down:
        weapon.melee_deg -= pps / 20
        weapon.p.rotate -= pps / 60
        if weapon.melee_deg <= 117.5:
            weapon.swing_down = False
            weapon.swing_up = True

    elif weapon.swing_up:
        weapon.melee_deg += pps / 200
        weapon.p.rotate += pps / 600
        if weapon.melee_deg >= 120:
            weapon.swing_up = False
            weapon.swing = False

