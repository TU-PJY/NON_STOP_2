from pico2d import *

from config import HEIGHT
from game_work import game_manager, game_framework
from home_class.home_ui_class import Button, Background, Playerimage, Monsterimage, Cursor


def handle_events():
    global cursor
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()

        elif event.type == SDL_MOUSEMOTION:
            cursor.mx, cursor.my = event.x, HEIGHT - 1 - event.y

        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            button.click = True


def init():
    global button, cursor

    cursor = Cursor()
    button = Button(cursor)
    bg = Background(cursor)
    pimage = Playerimage(cursor)
    mimage = Monsterimage(cursor)
    game_manager.add_object(bg, 6)
    game_manager.add_object(pimage, 7)
    game_manager.add_object(mimage, 7)
    game_manager.add_object(button, 7)
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
