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
    if weapon.melee_x > 0:
        weapon.melee_x -= pps
    else:
        weapon.melee_x = 0
