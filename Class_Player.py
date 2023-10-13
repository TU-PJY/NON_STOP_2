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
        pass

    @staticmethod
    def draw(p):
        if p.dir == 1:
            p.image.clip_composite_draw(0, 0, 128, 128, math.pi * p.rotate_left / 360, '', p.x, p.y - p.land_y, 400, 400)
        elif p.dir == 0:
            p.image.clip_composite_draw(0, 0, 128, 128, -math.pi * p.rotate_left / 360, 'h', p.x, p.y - p.land_y, 400, 400)


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
        pass

    @staticmethod
    def draw(p):
        if p.dir == 1:
            p.image.clip_composite_draw(0, 0, 128, 128, math.pi * p.rotate_left / 360, '', p.x, p.y - p.land_y, 400, 400)
        elif p.dir == 0:
            p.image.clip_composite_draw(0, 0, 128, 128, -math.pi * p.rotate_left / 360, 'h', p.x, p.y - p.land_y, 400, 400)


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
    global WIDTH, HEIGHT, JUMP_ACC, JUMP_ACC_SPEED
    def __init__(self):
        self.image = load_image(commando_image_directory)

        self.x, self.y, self.dir = WIDTH / 2, 250, 1
        self.mv_right, self.mv_left, self.mv_jump, self.land_shake = False, False, False, False  # 플레이어 이동, 점프
        
        self.speed = 2  # 플레이어 이동 속도 (사실상 맵 움직이는 속도)
        self.mx, self.my = 0, 0  # 마우스 좌표
        
        self.jump_acc = JUMP_ACC
        self.land_y = 0

        self.rotate_right, self.rotate_left = 0, 0
        self.state_machine = StateMachine(self)
        self.state_machine.start()


    def update(self):
        self.state_machine.update()

        if self.mv_jump:  # 점프 시 
            self.rotate_right += 0.2
            self.rotate_left -= 0.2
            self.y += self.jump_acc
            self.jump_acc -= JUMP_ACC_SPEED
            if self.jump_acc == -(JUMP_ACC + JUMP_ACC_SPEED):  # 점프 후 착지하면
                self.land_shake = True  # 땅에 착지 시 화면 흔들림이 활성화 된다 
                self.land_y = LAND_SHAKE

                self.mv_jump = False
                self.jump_acc = JUMP_ACC
                self.rotate_right, self.rotate_left = 0, 0

        if self.land_shake:    # 땅 흔들림 활성화시 화면 전체가 흔들린다. 
            if self.land_y > 0:
                self.land_y -= LAND_SHAKE_REDUCE
            else:
                self.land_shake = False


    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
