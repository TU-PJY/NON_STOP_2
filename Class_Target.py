from pico2d import *
from Env_variable import *
import math


# MOUSEBUTTON -> Gun class -> Target class


def draw_target(target):
    target.target_up.draw(target.p.mx, target.p.my + target.recoil + target.dis, 60, 60)
    target.target_down.draw(target.p.mx, target.p.my - target.recoil - target.dis, 60, 60)
    target.target_right.draw(target.p.mx + target.recoil + target.dis, target.p.my, 60, 60)
    target.target_left.draw(target.p.mx - target.recoil - target.dis, target.p.my, 60, 60)


def cal_dis(target):
    if GUN_NAME == 'SCAR_H':  # 분산도 계산 파트, 나누는 숫자가 작을수록 분산도가 크다.
        target.dis = 35 + math.sqrt((target.p.mx - WIDTH / 2) ** 2 + (target.p.y - target.p.my) ** 2) / 20
    if target.dis < 0:
        target.dis = 0


def update_recoil(target):
    if target.gun.shoot:  # 총 추가시 여기에 추가
        if GUN_NAME == 'SCAR_H':
            target.recoil += 20

    if target.recoil > 0:
        if target.reduce_delay == 0:
            target.recoil -= 1
            target.reduce_delay = RECOIL_REDUCE
        else:
            target.reduce_delay -= 1


class Update:
    @staticmethod
    def enter(target, e):
        pass

    @staticmethod
    def exit(target, e):
        pass

    @staticmethod
    def do(target):
        cal_dis(target)
        update_recoil(target)

    @staticmethod
    def draw(target):
        draw_target(target)


class StateMachineTarget:
    def __init__(self, target):
        self.target = target
        self.cur_state = Update
        self.table = {
            Update: {},
        }

    def start(self):
        self.cur_state.enter(self.target, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.target)

    def handle_event(self, e):  # state event handling
        for check_event, next_state in self.table[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.target, e)
                self.cur_state = next_state
                self.cur_state.enter(self.target, e)
                return True
        return False

    def draw(self):
        self.cur_state.draw(self.target)


class Target:
    def __init__(self, p, gun):
        self.target_up = load_image(target_up_directory)
        self.target_down = load_image(target_down_directory)
        self.target_right = load_image(target_right_directory)
        self.target_left = load_image(target_left_directory)

        self.p = p
        self.gun = gun
        self.dis, self.recoil = 0, 0
        self.reduce_delay = 0

        self.state_machine = StateMachineTarget(self)
        self.state_machine.start()

    def draw(self):
        self.state_machine.draw()

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))
