from pico2d import *

WIDTH, HEIGHT = 1200, 800

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def set_game():
    global running
    running = True

set_game()
open_canvas(WIDTH, HEIGHT)

while running:
    handle_events()
    delay(0.01)

close_canvas()
