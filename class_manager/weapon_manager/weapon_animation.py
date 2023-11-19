from class_manager.weapon_manager.etc import make_shell
from game_work import game_framework


# 윈체스터 휘두르기 장전 모션
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


# 근접무기 출력 위치 조정
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


# 근접무기 휘두르기 모션
def swing(weapon):
    pps = game_framework.pps

    if weapon.melee == 'BAT':
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

    elif weapon.melee == 'KATANA':
        if weapon.swing_down:
            weapon.melee_deg -= pps / 10
            weapon.p.rotate -= pps / 50
            if weapon.melee_deg <= -2.2:
                weapon.swing_down = False
                weapon.swing_up = True

        elif weapon.swing_up:
            weapon.melee_deg += pps / 100
            weapon.p.rotate += pps / 500
            if weapon.melee_deg >= 0:
                weapon.swing_up = False
                weapon.swing = False

    elif weapon.melee == 'AXE':
        if weapon.swing_down:
            weapon.melee_deg -= pps / 30
            weapon.p.rotate -= pps / 100
            if weapon.melee_deg <= 117.5:
                weapon.swing_down = False
                weapon.swing_up = True

        elif weapon.swing_up:
            weapon.melee_deg += pps / 300
            weapon.p.rotate += pps / 1000
            if weapon.melee_deg >= 120:
                weapon.swing_up = False
                weapon.swing = False
