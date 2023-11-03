from pico2d import *
from config import *
from game_class.player import Player
from game_class.map import Map, BackGround, Wall
from game_class.weapon import Weapon
from game_class.target import Target
from game_class.monster_tool import Tool
from game_work import game_manager, game_framework
from mods import shop_mode


def handle_events():
    global p, weapon

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_TAB:  # to_shop_mode
            game_framework.MODE = 'shop'
            game_framework.push_mode(shop_mode)
            show_cursor()
        elif event.type == SDL_MOUSEMOTION:
            p.mx, p.my = event.x, HEIGHT - 1 - event.y
        else:
            p.handle_event(event)
            weapon.handle_event(event)


def init():
    global game, p, mp, bg, wall, weapon, target, tool

    game = []

    p = Player()
    wall = Wall(p)
    bg = BackGround(p)
    mp = Map(p, wall, bg)
    weapon = Weapon(p)
    target = Target(p, weapon)
    tool = Tool(p, weapon, target, mp)

    game_manager.add_object(tool, 0)  # monster tool은 맨 아래 레이어에서 구동된다.
    game_manager.add_object(bg, 1)
    game_manager.add_object(p, 3)
    game_manager.add_object(weapon, 4)
    game_manager.add_object(mp, 5)
    game_manager.add_object(wall, 6)
    game_manager.add_object(target, 7)


def update():
    game_manager.update()


def draw():
    clear_canvas()
    game_manager.render()
    update_canvas()


def finish():
    game_manager.clear()
    pass


def pause():
    pass


def resume():
    pass