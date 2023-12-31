from pico2d import *

from config import HEIGHT
from game_work import game_framework, game_manager
from gameover_class.gameover_ui_class import Playerdead, Reward, Cursor


def handle_events():
    global cursor

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            pass

        elif event.type == SDL_MOUSEMOTION:
            cursor.mx, cursor.my = event.x, HEIGHT - 1 - event.y

        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            reward.click = True


def init():
    global playerdead, reward, cursor

    cursor = Cursor()
    playerdead = Playerdead()

    with open('data//rounds_data.json', 'rb') as f:
        data = json.load(f)
        for d in data:
            reward = Reward(cursor)
            reward.__dict__.update(d)

    game_manager.add_object(playerdead, 7)
    game_manager.add_object(reward, 6)
    game_manager.add_object(cursor, 7)


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
