from pico2d import *
from Env_variable import *
from player import Player
from map import Land, BackGround, Wall
from weapon import Weapon
from target import Target
from monater_manager import Manager
import game_manager


def handle_events():
    global running, p, weapon, target

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            p.mv_jump = True

        elif event.type == SDL_KEYDOWN and event.key == SDLK_q:  # 무기 교체
            if weapon.weapon_type == 0:
                p.look_mouse = False  # 플레이어는 더 이상 마우스를 따라보지 않는다.
                p.rotate = 0
                weapon.weapon_type = 1
                weapon.flame_display_time = 0
                return
            else:
                p.look_mouse = True
                weapon.weapon_type = 0

        elif event.type == SDL_MOUSEMOTION:
            p.mx, p.my = event.x, HEIGHT - 1 - event.y

        else:
            p.handle_event(event)
            weapon.handle_event(event)


def init_game():
    global running, game, p, land, bg, wall, weapon, target, m, gp

    running = True
    game = []

    p = Player()
    land = Land(p)
    wall = Wall(p)
    bg = BackGround(p)
    weapon = Weapon(p)
    target = Target(p, weapon)
    man = Manager(p, weapon, target)

    game_manager.add_object(man, 0)
    game_manager.add_object(bg, 1)
    game_manager.add_object(p, 3)
    game_manager.add_object(weapon, 4)
    game_manager.add_object(land, 5)
    game_manager.add_object(wall, 6)
    game_manager.add_object(target, 7)


def update_game():
    game_manager.update()


def render_game():
    game_manager.render()


open_canvas(WIDTH, HEIGHT)
init_game()
hide_cursor()
hide_lattice()

while running:
    clear_canvas()
    handle_events()

    if GAME_SCENE == SCENE[2]:  # 인게임
        render_game()
        update_game()

    update_canvas()

    delay(0.001)

close_canvas()
