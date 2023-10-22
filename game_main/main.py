from pico2d import *
from config import *
from game_class.player import Player
from game_class.map import Land, BackGround, Wall
from game_class.weapon import Weapon
from game_class.target import Target
from class_manager.monster_tool import Manager
from game_work import game_manager


def handle_events():
    global running, p, weapon, target

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

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
