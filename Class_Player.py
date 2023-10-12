from pico2d import *
from Config import *
from Class_Object import *
import math


def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_d


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_d


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a


def look(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEMOTION


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
        pass

    @staticmethod
    def draw(p):
        if p.dir == 1:
            p.image.clip_composite_draw(0, 0, 128, 128, math.pi * p.rotate_left / 360, '', p.x, p.y, 400, 400)
        elif p.dir == 0:
            p.image.clip_composite_draw(0, 0, 128, 128, -math.pi * p.rotate_left / 360, 'h', p.x, p.y, 400, 400)


class Idle:
    @staticmethod
    def enter(p, e):
        pass

    @staticmethod
    def exit(p, e):
        pass

    @staticmethod
    def do(p):
        pass

    @staticmethod
    def draw(p):
        if p.dir == 1:
            p.image.clip_composite_draw(0, 0, 128, 128, math.pi * p.rotate_left / 360, '', p.x, p.y, 400, 400)
        elif p.dir == 0:
            p.image.clip_composite_draw(0, 0, 128, 128, -math.pi * p.rotate_left / 360, 'h', p.x, p.y, 400, 400)


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
        self.mv_right, self.mv_left, self.mv_jump = False, False, False
        self.jump_acc = JUMP_ACC
        self.rotate_right = 0
        self.rotate_left = 0
        self.dir = 1
        self.dist = 0  # 플레이어의 이동거리를 측정하는 변수
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()
        if self.mv_jump:
            self.rotate_right += 0.2
            self.rotate_left -= 0.2
            self.y += self.jump_acc
            self.jump_acc -= JUMP_ACC_SPEED
            if self.jump_acc == -(JUMP_ACC + JUMP_ACC_SPEED):  # 점프 후 착지하면
                self.mv_jump = False
                self.jump_acc = JUMP_ACC
                self.rotate_right, self.rotate_left = 0, 0

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
