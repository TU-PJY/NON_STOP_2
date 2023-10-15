from pico2d import *
from Env_variable import *
from Player import Player
from Map import Land, BackGround, Wall
from Weapon import Weapon
from Target import Target


def handle_events():
    global running, p, weapon, target

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:  # 점프는 상태 상관없이 가능해야하므로 점프 기능은 이곳에 배치
            p.mv_jump = True

        elif event.type == SDL_MOUSEMOTION:
            p.mx, p.my = event.x, HEIGHT - 1 - event.y

        elif event.type == SDL_KEYDOWN and event.key == SDLK_q:  # 무기 교체
            if weapon.weapon_type == 0:
                p.look_mouse = False
                p.rotate = 0

                weapon.weapon_type = 1
                weapon.flame_display_time = 0
                return

            elif weapon.weapon_type == 1:
                p.look_mouse = True
                weapon.weapon_type = 0

        else:
            p.handle_event(event)
            weapon.handle_event(event)


def init_game():
    global running, game, p, land, bg, wall, weapon, target

    running = True
    game = []

    p = Player()
    land = Land(p)
    wall = Wall(p)
    bg = BackGround(p)
    weapon = Weapon(p)
    target = Target(p, weapon)

    game.append(bg)
    game.append(p)
    game.append(weapon)
    game.append(land)
    game.append(wall)
    game.append(target)


def update_game():
    for o in game:
        o.update()


def render_game():
    for o in game:
        o.draw()


open_canvas(WIDTH, HEIGHT)
init_game()
hide_cursor()
hide_lattice()


while running:
    clear_canvas()
    handle_events()

    if GAME_SCENE == SCENE[2]:  # 인게임
        render_game()
        update_game()

    update_canvas()

close_canvas()
