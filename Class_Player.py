from pico2d import *
from Env_variable import *
from Class_Map import *
import math


# 실시간으로 총이 마우스 좌표를 향해야 하므로 Class_Player가 마우스 좌표를 받아 Class_Gun으로 전달한다.
# 플레이어 이동 시 맵 자체가 움직이는 방식이기 때문에 컨트롤러의 키 누름 여부와 현재 플레이어 좌표를 Class_Map으로 전달한다.


def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_d


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_d


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a


def draw_player(p):
    if p.dir == 1:
        p.image.clip_composite_draw(0, 0, 128, 128, p.rotate, '', p.x, p.y - p.land_y, 400, 400)
    elif p.dir == 0:
        p.image_left.clip_composite_draw(0, 0, 128, 128, p.rotate, 'h, v', p.x, p.y - p.land_y, 400, 400)


def look_mouse(p):
    if p.dir == 1:  # 마우스를 살짝 따라본다.
        p.rotate = math.atan2((p.my - p.y), ((p.mx * 1.7) - p.x))
    elif p.dir == 0:
        p.rotate = math.atan2((p.my - p.y), (p.mx - (p.x * 1.7)))


def jump_and_land(p):
    if p.mv_jump:  # 점프 시
        p.y += p.jump_acc

        if p.acc_delay < ACC_DELAY:  # 빠른 딜레이로 인해 가속도 변화에 딜레이를 줘야 제대로 된 점프 애니메이션이 나온다.
            p.acc_delay += 1
        else:
            p.jump_acc -= 1
            p.acc_delay = 0

        if p.jump_acc == -(JUMP_ACC + 1):  # 점프 후 착지하면
            p.land_shake = True  # 땅에 착지 시 화면 흔들림이 활성화 된다
            p.mv_jump = False  # 점프가 가능해진다
            p.land_y = LAND_SHAKE  # LAND_SHAKE 만큼 화면이 눌린다
            p.jump_acc = JUMP_ACC  # 점프 가속도 초기화
            p.acc_delay = 0  # 점프 가속도 변화 딜레이 초기화

    if p.land_shake:  # 땅 흔들림 활성화 시 화면 전체가 흔들린다.
        if p.land_y > 0:
            p.land_y -= LAND_SHAKE_REDUCE
        else:
            p.land_shake = False


class Move:
    @staticmethod
    def enter(p, e):
        if right_down(e) or left_up(e):
            p.mv_right = True
        elif right_up(e) or left_down(e):
            p.mv_left = True

    @staticmethod
    def exit(p, e):
        p.mv_right = False
        p.mv_left = False

    @staticmethod
    def do(p):
        p.dir = 1 if p.mx > p.x else 0
        jump_and_land(p)
        look_mouse(p)

    @staticmethod
    def draw(p):
        draw_player(p)


class Idle:
    @staticmethod
    def enter(p, e):
        pass

    @staticmethod
    def exit(p, e):
        pass

    @staticmethod
    def do(p):
        p.dir = 1 if p.mx > p.x else 0
        jump_and_land(p)
        look_mouse(p)

    @staticmethod
    def draw(p):
        draw_player(p)


class StateMachine:
    def __init__(self, p):
        self.p = p
        self.cur_state = Idle
        self.table = {
            Idle: {right_down: Move, left_down: Move, left_up: Move, right_up: Move},
            Move: {right_down: Idle, left_down: Idle, left_up: Idle, right_up: Idle},
        }

    def start(self):
        self.cur_state.enter(self.p, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.p)

    def handle_event(self, e):  # state event handling
        for check_event, next_state in self.table[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.p, e)
                self.cur_state = next_state
                self.cur_state.enter(self.p, e)
                return True
        return False

    def draw(self):
        self.cur_state.draw(self.p)


class Player:
    def __init__(self):
        self.image = load_image(commando_image_directory)
        self.image_left = load_image(commando_left_image_directory)

        self.x, self.y, self.dir = WIDTH / 2, 250, 1
        self.mv_right, self.mv_left, self.mv_jump, self.land_shake = False, False, False, False  # 플레이어 이동, 점프
        
        self.speed = 2  # 플레이어 이동 속도 (사실상 맵 움직이는 속도)
        self.mx, self.my = 0, 0  # 마우스 좌표

        self.jump_acc = JUMP_ACC
        self.acc_delay = 0
        self.land_y = 0  # 이 수치만큼 화면의 모든 이미지들이 아래로 눌린다.

        self.state_machine = StateMachine(self)
        self.state_machine.start()

        self.rotate = 0  # 플레이어가 마우스 좌표를 살짝 따라 본다

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
