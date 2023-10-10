from pico2d import *
from Config import *
from Classes import Commando, Land, BackGround


def handle_events():
    global running, mx, my, commando
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, HEIGHT - 1 - event.y
            commando.Dir = 1 if mx > commando.x else 0

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_d:
                commando.mv_right = True
            elif event.key == SDLK_a:
                commando.mv_left = True
            elif event.key == SDLK_SPACE and commando.mv_jump == False:
                commando.mv_jump = True

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_d: commando.mv_right = False
            if event.key == SDLK_a: commando.mv_left = False


def init_game():
    global running, commando, land, bg
    running = True
    commando = Commando()
    land = Land()
    bg = BackGround()


def update_game():
    commando.move()


def render():
    bg.draw()
    commando.draw()
    land.draw()




open_canvas(WIDTH, HEIGHT)
init_game()

while running:
    clear_canvas()
    handle_events()
    render()
    update_game()
    update_canvas()

close_canvas()
