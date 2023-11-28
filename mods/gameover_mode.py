from pico2d import *

from config import HEIGHT
from game_work import game_framework, game_manager
from gameover_class.prop import Playerdead, Reward


def handle_events():
    global p, weapon

    events = get_events()
    global reward
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()

        elif event.type == SDL_MOUSEMOTION:
            reward.mx, reward.my = event.x, HEIGHT - 1 - event.y

        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            reward.click = True  # true일 시 상점창이 반응한다


def init():
    global playerdead, reward
    show_cursor()
    playerdead = Playerdead()
    reward = Reward()

    game_manager.add_object(playerdead, 7)
    game_manager.add_object(reward, 6)


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