# 플레이어 관련 함수 모음
from pico2d import *
from Env_variable import *
import math


def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_d


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_d


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a


def load_player_image(self):
    self.image = load_image(commando_image_directory)
    self.image_left = load_image(commando_left_image_directory)


def calculate_player_pos(p):
    p.px = p.x + p.shake_x + p.camera_x
    p.py = p.y - p.land_y + p.shake_y + p.size * 50 + p.camera_y

    p.py2 = p.y - p.land_y + p.shake_y + p.camera_y
    # 사이즈 변형 포함되지 않은 y 위치. 무기 좌표로 사용.

    p.efx = p.shake_x + p.camera_x
    p.efy = p.shake_y - p.land_y + p.camera_y
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
    if p.mv_jump:  # 점프 시
        p.y += p.jump_acc

        if p.y <= 250:  # 점프 후 착지하면
            p.y = 250
            p.jump_acc = JUMP_ACC  # 점프 가속도 초기화
            p.acc_delay = 0  # 점프 가속도 변화 딜레이 초기화
            p.mv_jump = False  # 점프가 가능해진다
            p.land_y = LAND_SHAKE  # LAND_SHAKE 만큼 화면이 눌린다

        if p.acc_delay < ACC_DELAY:  # 빠른 딜레이로 인해 가속도 변화에 딜레이를 줘야 제대로 된 점프 애니메이션이 나온다.
            p.acc_delay += 1
        else:
            p.jump_acc -= 1
            p.acc_delay = 0


def walk_animation(p):
    if p.size_up:
        p.size_deg += 0.01

        if p.size_deg >= 0.3:
            p.size_deg = 0.3
            p.size_up = False

    elif not p.size_up:
        p.size_deg -= 0.01
        if p.size_deg <= 0:
            p.size_deg = 0
            p.size_up = True
    p.size = math.sin(p.size_deg)
