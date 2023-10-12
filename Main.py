from pico2d import *
from Env_variable import *
from Class_Player import Player
from Class_Map import Land, BackGround, Wall


def handle_events():
    global running, mx, my, p

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:  # 점프는 상태 상관없이 가능해야하므로 점프 기능은 이곳에 배치
            p.mv_jump = True
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, HEIGHT - 1 - event.y
            p.dir = 1 if mx > p.x else 0
        else:
            p.handle_event(event)


def init_game():
    global running, game, p, land, bg, wall

    running = True
    game = []

    p = Player()
    land = Land(p)
    wall = Wall(p)
    bg = BackGround(p)

    game.append(bg)
    game.append(p)
    game.append(land)
    game.append(wall)


def update_game():
    for o in game:
        o.update()


def render_game():
    for o in game:
        o.draw()


open_canvas(WIDTH, HEIGHT)
init_game()

while running:
    clear_canvas()
    handle_events()

    if GAME_SCENE == SCENE[2]:  # 인게임
        render_game()
        update_game()

    update_canvas()

close_canvas()
