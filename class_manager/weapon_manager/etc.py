from pico2d import *

from game_class.prop import Shell
from game_work import game_manager, game_framework


def l_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONDOWN and e[1].button == SDL_BUTTON_LEFT


def l_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONUP and e[1].button == SDL_BUTTON_LEFT


def q_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_q


def r_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONDOWN and e[1].button == SDL_BUTTON_RIGHT


def r_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONUP and e[1].button == SDL_BUTTON_RIGHT


def change_weapon(weapon):
    if weapon.weapon_type == 0:  # 총을 들고 있을 때 총 -> 근접무기
        weapon.p.look_mouse = False  # 플레이어는 더 이상 마우스를 따라보지 않는다.
        weapon.p.rotate = 0
        weapon.weapon_type = 1
        weapon.flame_display_time = 0
        weapon.zoom = False
        return

    elif weapon.weapon_type == 1:  # 근접무기를 들고 있을 때 근접무기 -> 총
        weapon.p.look_mouse = True
        weapon.weapon_type = 0


def update_delay(weapon):
    pps = game_framework.pps
    if weapon.shoot_delay > 0:
        weapon.shoot_delay -= pps / 3
    if weapon.wield_delay > 0:
        weapon.wield_delay -= pps / 3


def update_sniper_bolt(weapon):
    if weapon.gun == 'AWP':
        if 100 < weapon.shoot_delay < 500 and not weapon.shell_out:  # 탄피를 한 번만 만들도록 한다
            weapon.bolt_action = True
            make_shell(weapon, 30, 20)
            weapon.shell_out = True

        if 0 < weapon.shoot_delay < 100:
            weapon.bolt_action = False
            weapon.shell_out = False


def make_shell(weapon, size_x=15, size_y=15):  # 탄피 생성
    if weapon.p.dir == 0:
        shell = Shell \
            (weapon.p, weapon.mp, weapon.p.x - 20, weapon.p.y - weapon.p.cam_h + 10, weapon.p.dir, size_x, size_y)
    elif weapon.p.dir == 1:
        shell = Shell \
            (weapon.p, weapon.mp, weapon.p.x + 20, weapon.p.y - weapon.p.cam_h + 10, weapon.p.dir, size_x, size_y)
    game_manager.add_object(shell, 4)  # 총을 발사하면 탄피가 나온다
