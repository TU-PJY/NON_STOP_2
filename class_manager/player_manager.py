# 플레이어 관련 함수 모음

from pico2d import *

from config import *
from game_work import game_framework


def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_d


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_d


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a


def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


def calc_pps():
    global pps
    pps = PPS * game_framework.frame_time


def load_player_image(self):
    self.image = load_image(player1_right_image_directory)
    self.image_left = load_image(player1_left_image_directory)


def calculate_player_pos(p):
    p.px = p.x + p.shake_x + p.camera_x  # 무기 풀력 x 좌표로도 사용
    p.py = p.y - p.land_y + p.shake_y + p.size * 50 + p.camera_y
    # 플레이어 출력 좌표

    p.py2 = p.y - p.land_y + p.shake_y + p.camera_y
    # 무기 출력 y 좌표

    p.efx = p.shake_x + p.camera_x
    p.efy = p.shake_y - p.land_y + p.camera_y - (p.y - 250) / 1.5
    # 나머지 객체에 사용되는 좌표


def look_mouse(p):
    if p.look_mouse:
        if p.dir == 1:  # 마우스를 살짝 따라본다.
            p.rotate = math.atan2((p.my - p.y), ((p.mx * 1.7) - p.x))
        elif p.dir == 0:
            p.rotate = math.atan2((p.my - p.y), (p.mx - (p.x * 1.7)))


def draw_player(p):
    if p.dir == 1:
        p.image.clip_composite_draw(0, 0, 128, 128, p.rotate, '', p.px, p.py, 400, 400 + p.size * 100)
    elif p.dir == 0:
        if p.look_mouse:
            p.image_left.clip_composite_draw(0, 0, 128, 128, p.rotate, 'h, v', p.px, p.py, 400, 400 + p.size * 100)
        else:
            p.image_left.clip_composite_draw(0, 0, 128, 128, p.rotate, '', p.px, p.py, 400, 400 + p.size * 100)


def jump(p):
    global pps
    if p.mv_jump:  # 점프 시
        p.y += p.jump_acc * pps / 4

        if p.y <= 250:  # 점프 후 착지하면
            p.y = 250
            p.jump_acc = 0  # 점프 가속도 초기화
            p.mv_jump = False  # 점프가 가능해진다
            p.land_y = LAND_SHAKE  # LAND_SHAKE 만큼 화면이 눌린다
            p.jump_count = 0  # 점프 가능 횟수 초기화

        p.jump_acc -= pps / 90


def walk_animation(p):
    global pps
    p.size_deg += 1 * pps / 50

    if not p.mv_jump:
        p.size = math.sin(p.size_deg) / 7
    else:
        p.size = 0


def update_damage_delay(p):
    global pps
    if p.dmg_delay > 0:
        p.dmg_delay -= pps / 3
