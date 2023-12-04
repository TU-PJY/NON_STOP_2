# 플레이어 관련 함수 모음
import random

from pico2d import *

from config import *
from game_class.prop import Playerdead
from game_work import game_framework, game_manager
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


def ctrl_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LCTRL


def load_player_image(self):
    self.image = load_image(player1_right_image_directory)
    self.image_left = load_image(player1_left_image_directory)
    self.ch2_right = load_image(player2_right_image_directory)
    self.ch2_left = load_image(player2_left_image_directory)
    self.ch3_right = load_image(player3_right_image_directory)
    self.ch3_left = load_image(player3_left_image_directory)
    self.ch4_right = load_image(player4_right_image_directory)
    self.ch4_left = load_image(player4_left_image_directory)
    self.ch5_right = load_image(player5_right_image_directory)
    self.ch5_left = load_image(player5_left_image_directory)
    self.ch6_right = load_image(player6_right_image_directory)
    self.ch6_left = load_image(player6_left_image_directory)
    self.ch7_right = load_image(player7_right_image_directory)
    self.ch7_left = load_image(player7_left_image_directory)
    self.ch8_right = load_image(player8_right_image_directory)
    self.ch8_left = load_image(player8_left_image_directory)

    self.here = load_image(ch_selected_directory)

    self.sound = load_wav(walk_directory)
    self.sound.set_volume(128)
    self.land_sound = load_wav(land_directory)
    self.land_sound.set_volume(128)
    self.jump_sound = load_wav(jump_directory)
    self.jump_sound.set_volume(128)

    self.damage_sound = load_wav(damage_directory)
    self.dead_sound = load_wav(dead_sound_directory)
    self.medkit_sound = load_wav(medkit_sound_directory)

    self.random_bgm = random.randint(1, 2)
    match self.random_bgm:
        case 1:
            self.play_bgm = load_music(play_bgm_directory)
        case 2:
            self.play_bgm = load_music(play_bgm2_directory)


def look_mouse(p):
    if p.look_mouse:  # 해당 변수가 true일 때만 플레이어는 마우스를 바라본다
        if p.dir == 1:  # 마우스를 살짝 따라본다.
            p.rotate = math.atan2((p.my - p.y), ((p.mx * 1.7) - p.x))
        elif p.dir == 0:
            p.rotate = math.atan2((p.my - p.y), (p.mx - (p.x * 1.7)))


def draw_player(p):
    # 플레이어가 너무 높게 점프하여 화면 높이보다 더 올라가게 되면 플레이어 위치를 화살표로 표시한다
    if p.y + p.cam_y >= HEIGHT:
        p.here.rotate_draw(math.radians(180), p.x + p.ex, HEIGHT - 120, 80, 80)

    if p.look_mouse:  # 캐릭터에 따라 이미지가 다르게 출력 된다. look mouse = true 일시 플레이어가 마우스를 따라본다
        if p.dir == 1:
            match p.ch:
                case 1:
                    p.image.clip_composite_draw(0, 0, 128, 128, p.rotate, '', p.px, p.py, 400, 400 + p.size * 100)
                case 2:
                    p.ch2_right.clip_composite_draw(0, 0, 128, 128, p.rotate, '', p.px, p.py, 400, 400 + p.size * 100)
                case 3:
                    p.ch3_right.clip_composite_draw(0, 0, 128, 128, p.rotate, '', p.px, p.py, 400, 400 + p.size * 100)
                case 4:
                    p.ch4_right.clip_composite_draw(0, 0, 128, 128, p.rotate, '', p.px, p.py, 400, 400 + p.size * 100)
                case 5:
                    p.ch5_right.clip_composite_draw(0, 0, 128, 128, p.rotate, '', p.px, p.py, 400, 400 + p.size * 100)
                case 6:
                    p.ch6_right.clip_composite_draw(0, 0, 128, 128, p.rotate, '', p.px, p.py, 400, 400 + p.size * 100)
                case 7:
                    p.ch7_right.clip_composite_draw(0, 0, 128, 128, p.rotate, '', p.px, p.py, 400, 400 + p.size * 100)
                case 8:
                    p.ch8_right.clip_composite_draw(0, 0, 128, 128, p.rotate, '', p.px, p.py, 400, 400 + p.size * 100)

        elif p.dir == 0:
            match p.ch:
                case 1:
                    p.image_left.clip_composite_draw \
                        (0, 0, 128, 128, p.rotate, 'h, v', p.px, p.py, 400, 400 + p.size * 100)
                case 2:
                    p.ch2_left.clip_composite_draw \
                        (0, 0, 128, 128, p.rotate, 'h, v', p.px, p.py, 400, 400 + p.size * 100)
                case 3:
                    p.ch3_left.clip_composite_draw \
                        (0, 0, 128, 128, p.rotate, 'h, v', p.px, p.py, 400, 400 + p.size * 100)
                case 4:
                    p.ch4_left.clip_composite_draw \
                        (0, 0, 128, 128, p.rotate, 'h, v', p.px, p.py, 400, 400 + p.size * 100)
                case 5:
                    p.ch5_left.clip_composite_draw \
                        (0, 0, 128, 128, p.rotate, 'h, v', p.px, p.py, 400, 400 + p.size * 100)
                case 6:
                    p.ch6_left.clip_composite_draw \
                        (0, 0, 128, 128, p.rotate, 'h, v', p.px, p.py, 400, 400 + p.size * 100)
                case 7:
                    p.ch7_left.clip_composite_draw \
                        (0, 0, 128, 128, p.rotate, 'h, v', p.px, p.py, 400, 400 + p.size * 100)
                case 8:
                    p.ch8_left.clip_composite_draw \
                        (0, 0, 128, 128, p.rotate, 'h, v', p.px, p.py, 400, 400 + p.size * 100)

    else:
        if p.dir == 1:
            match p.ch:
                case 1:
                    p.image.clip_composite_draw(0, 0, 128, 128, p.rotate, '', p.px, p.py, 400, 400 + p.size * 100)
                case 2:
                    p.ch2_right.clip_composite_draw(0, 0, 128, 128, p.rotate, '', p.px, p.py, 400, 400 + p.size * 100)
                case 3:
                    p.ch3_right.clip_composite_draw(0, 0, 128, 128, p.rotate, '', p.px, p.py, 400, 400 + p.size * 100)
                case 4:
                    p.ch4_right.clip_composite_draw(0, 0, 128, 128, p.rotate, '', p.px, p.py, 400, 400 + p.size * 100)
                case 5:
                    p.ch5_right.clip_composite_draw(0, 0, 128, 128, p.rotate, '', p.px, p.py, 400, 400 + p.size * 100)
                case 6:
                    p.ch6_right.clip_composite_draw(0, 0, 128, 128, p.rotate, '', p.px, p.py, 400, 400 + p.size * 100)
                case 7:
                    p.ch7_right.clip_composite_draw(0, 0, 128, 128, p.rotate, '', p.px, p.py, 400, 400 + p.size * 100)
                case 8:
                    p.ch8_right.clip_composite_draw(0, 0, 128, 128, p.rotate, '', p.px, p.py, 400, 400 + p.size * 100)
        elif p.dir == 0:
            match p.ch:
                case 1:
                    p.image_left.clip_composite_draw \
                        (0, 0, 128, 128, -p.rotate, '', p.px, p.py, 400, 400 + p.size * 100)
                case 2:
                    p.ch2_left.clip_composite_draw \
                        (0, 0, 128, 128, -p.rotate, '', p.px, p.py, 400, 400 + p.size * 100)
                case 3:
                    p.ch3_left.clip_composite_draw \
                        (0, 0, 128, 128, -p.rotate, '', p.px, p.py, 400, 400 + p.size * 100)
                case 4:
                    p.ch4_left.clip_composite_draw \
                        (0, 0, 128, 128, -p.rotate, '', p.px, p.py, 400, 400 + p.size * 100)
                case 5:
                    p.ch5_left.clip_composite_draw \
                        (0, 0, 128, 128, -p.rotate, '', p.px, p.py, 400, 400 + p.size * 100)
                case 6:
                    p.ch6_left.clip_composite_draw \
                        (0, 0, 128, 128, -p.rotate, '', p.px, p.py, 400, 400 + p.size * 100)
                case 7:
                    p.ch7_left.clip_composite_draw \
                        (0, 0, 128, 128, -p.rotate, '', p.px, p.py, 400, 400 + p.size * 100)
                case 8:
                    p.ch8_left.clip_composite_draw \
                        (0, 0, 128, 128, -p.rotate, '', p.px, p.py, 400, 400 + p.size * 100)


def jump(p):
    pps = game_framework.pps
    # AXE 스킬을 사용할 경우
    if p.mv_jump and play_mode.weapon.melee == 'AXE' and play_mode.weapon.skill_enable:
        p.y += p.jump_acc * pps / 4

        if p.y <= 250:  # 점프 후 착지하면
            p.y = 250
            p.jump_acc = 0  # 점프 가속도 초기화
            p.push_y = 150  # LAND_SHAKE 만큼 화면이 눌린다
            p.jump_delay = 0
            p.shake_range = 80
            play_mode.weapon.axe_hit.play()
            play_mode.weapon.hit_ground = True

        if 0 < p.jump_acc:
            p.jump_acc -= pps / 50

        elif p.jump_acc <= 0:
            if p.jump_delay < 100:
                p.jump_acc = 0
                p.jump_delay += pps / 4
            elif p.jump_delay > 100:
                p.jump_acc -= pps / 5

    # 일반 점프
    else:
        if p.mv_jump:  # 점프 시
            p.y += p.jump_acc * pps / 4

            if p.y <= 250:  # 점프 후 착지하면
                p.y = 250
                p.jump_acc = 0  # 점프 가속도 초기화
                p.mv_jump = False  # 점프가 가능해진다
                p.push_y = LAND_SHAKE  # LAND_SHAKE 만큼 화면이 눌린다
                p.jump_count = 0  # 점프 가능 횟수 초기화
                p.land_sound.play()

            p.jump_acc -= pps / 90


def walk_animation(p):  # 플레이어 rubber animation 출력
    pps = game_framework.pps
    p.size_deg += 1 * pps / 50

    if not p.mv_jump:
        p.size = math.sin(p.size_deg) / 5
    else:
        p.size = 0


def update_damage_delay(p):  # 플레이어 대미지 딜레이 업데이트
    pps = game_framework.pps
    if p.dmg_delay > 0:
        p.dmg_delay -= pps / 3


def set_medkit_delay(p):
    p.usable_medkit = False
    p.medkit_delay = get_time()


def update_medkit_delay(p):
    if not p.usable_medkit:
        p.medkit_delay_time = get_time() - p.medkit_delay
        if p.medkit_delay_time > 9:
            p.usable_medkit = True


def regen_hp(p):  # 일정 시간마다 체력을 스스로 회복한다
    pps = game_framework.pps
    if p.cur_hp < p.hp:
        p.regen_timer += pps / 3
        if p.regen_timer >= p.regen_delay:
            p.cur_hp += 5
            if p.cur_hp > p.hp:
                p.regen_timer = 0
                p.cur_hp = p.hp
            p.regen_timer = 0


def check_hp(p):  # 플레이어 체력이 0이 되면 게임 오버 모드로 전환한다
    if p.cur_hp <= 0:
        p.dead_sound.play()
        play_mode.weapon.update_deg = False  # 더 이상 총기 이미지 각도 업데이트를 하지 않는다
        p.play_bgm.stop()
        game_framework.START = False
        playerdead = Playerdead()
        game_manager.add_object(playerdead, 7)
        game_framework.MODE = 'GAMEOVER'


def play_player_sound(p):  # 일정 주기로 걷는 소리를 출력한다
    pps = game_framework.pps
    if (p.mv_right or p.mv_left) and not p.mv_jump:  # 땅에 닿지 않으면 출력하지 않는다
        p.sound_delay -= pps / 4
        if p.sound_delay <= 0:
            p.sound.play()
            p.sound_delay = 70
