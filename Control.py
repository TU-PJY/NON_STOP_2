from pico2d import *
from Classes import Commando
from NON_STOP import running
from Config import *

def handle_events():
    global running
    global mx, my
    global commando
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, HEIGHT - 1 - event.y
            if mx > commando.x:
                commando.Dir = 1
            elif mx < commando.x:
                commando.Dir = 0    

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
            if event.key == SDLK_d:
                commando.mv_right = False 
            if event.key == SDLK_a:
                commando.mv_left = False 