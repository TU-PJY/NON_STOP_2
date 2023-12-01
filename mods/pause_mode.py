from pico2d import *
from config import *
from game_work import game_framework, game_manager
from mods import play_mode
from pop_ui_class.pause_ui import Back, Button, Cursor, Back2


def handle_events():
    global exit_enable, cursor, button
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYUP and event.key == SDLK_ESCAPE:
            exit_enable = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            if exit_enable:
                bg = Back2()
                game_manager.add_object(bg, 7)
                game_framework.MODE = 'play'
                game_framework.pop_mode()

        elif event.type == SDL_MOUSEMOTION:
            cursor.mx, cursor.my = event.x, HEIGHT - 1 - event.y

        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            button.click = True

        else:
            play_mode.p.handle_event(event)  # 이동키를 누른 상태로 모드 전환 시 동작 오류 방지
            play_mode.weapon.handle_event(event)  # 마우스 버튼을 누른 채로 모드 전환 시 동작 오류 방지


def init():
    global exit_enable, back, button, cursor
    exit_enable = False

    back = Back()
    cursor = Cursor()
    button = Button(cursor)

    game_manager.add_object(back, 7)
    game_manager.add_object(button, 7)
    game_manager.add_object(cursor, 7)
    pass


def update():
    game_manager.update()


def draw():
    clear_canvas()
    game_manager.render()
    update_canvas()


def finish():
    game_manager.remove_object(back)
    game_manager.remove_object(button)
    game_manager.remove_object(cursor)
    pass


def pause():
    pass


def resume():
    pass
