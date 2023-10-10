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
            elif event.key == SDLK_SPACE:
                commando.mv_jump = True

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_d:
                commando.mv_right = False
            if event.key == SDLK_a:
                commando.mv_left = False


def init_game():
    global running, commando, land, bg
    running = True
    commando = Commando()
    land = Land()
    bg = BackGround()


def move_commando():
    commando.jump()  # 점프
    commando.mem_distance()  # 이동 거리를 측정하여 배경 스크롤 여부를 결정한다
    if -2048 + WIDTH / 2 <= commando.distance <= 2048 - WIDTH / 2:
        land.scroll(commando.mv_right, commando.mv_left)
        bg.scroll(commando.mv_right, commando.mv_left)
    elif -2048 + WIDTH / 2 >= commando.distance or commando.distance >= 2048 - WIDTH / 2:
        commando.move()


def update_game():
    move_commando()


def render():
    bg.draw()
    commando.draw()
    land.draw()


open_canvas(WIDTH, HEIGHT)
init_game()

while running:
    clear_canvas()
    handle_events()

    if GAME_SCENE == SCENE[2]:  # 인게임
        render()
        update_game()

    update_canvas()

close_canvas()
