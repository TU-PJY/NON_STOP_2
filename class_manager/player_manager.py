# 플레이어 관련 함수 모음

from pico2d import *

from config import *
from game_work import game_framework
from mods import play_mode


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


def load_player_image(self):
    self.image = load_image(player1_right_image_directory)
    self.image_left = load_image(player1_left_image_directory)


def look_mouse(p):
    if p.look_mouse:
        if p.dir == 1:  # 마우스를 살짝 따라본다.
            p.rotate = math.atan2((p.my - p.y), ((p.mx * 1.7) - p.x))
        elif p.dir == 0:
            p.rotate = math.atan2((p.my - p.y), (p.mx - (p.x * 1.7)))


def draw_player(p):
    if p.look_mouse:
        if p.dir == 1:
            p.image.clip_composite_draw(0, 0, 128, 128, p.rotate, '', p.px, p.py, 400, 400 + p.size * 100)
        elif p.dir == 0:
            p.image_left.clip_composite_draw(0, 0, 128, 128, p.rotate, 'h, v', p.px, p.py, 400, 400 + p.size * 100)
    else:
        if p.dir == 1:
            p.image.clip_composite_draw(0, 0, 128, 128, p.rotate, '', p.px, p.py, 400, 400 + p.size * 100)
        elif p.dir == 0:
            p.image_left.clip_composite_draw(0, 0, 128, 128, -p.rotate, '', p.px, p.py, 400, 400 + p.size * 100)


def jump(p):
    pps = game_framework.pps
    if p.mv_jump and play_mode.weapon.melee == 'AXE' and play_mode.weapon.skill_enable:
        p.y += p.jump_acc * pps / 4

        if p.y <= 250:  # 점프 후 착지하면
            p.y = 250
            p.jump_acc = 0  # 점프 가속도 초기화
            p.push_y = 150  # LAND_SHAKE 만큼 화면이 눌린다
            p.jump_delay = 0
            p.shake_range = 80
            play_mode.weapon.hit_ground = True

        if 0 < p.jump_acc:
            p.jump_acc -= pps / 50

        elif p.jump_acc <= 0:
            if p.jump_delay < 30:
                p.jump_acc = 0
                p.jump_delay += pps / 4
            elif p.jump_delay > 30:
                p.jump_acc -= pps / 5

    else:
        if p.mv_jump:  # 점프 시
            p.y += p.jump_acc * pps / 4

            if p.y <= 250:  # 점프 후 착지하면
                p.y = 250
                p.jump_acc = 0  # 점프 가속도 초기화
                p.mv_jump = False  # 점프가 가능해진다
                p.push_y = LAND_SHAKE  # LAND_SHAKE 만큼 화면이 눌린다
                p.jump_count = 0  # 점프 가능 횟수 초기화

            p.jump_acc -= pps / 90


def walk_animation(p):
    pps = game_framework.pps
    p.size_deg += 1 * pps / 50

    if not p.mv_jump:
        p.size = math.sin(p.size_deg) / 5
    else:
        p.size = 0


def update_damage_delay(p):
    pps = game_framework.pps
    if p.dmg_delay > 0:
        p.dmg_delay -= pps / 3
