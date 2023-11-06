from class_manager.target_manager import *


# MOUSEBUTTON -> Gun class -> Target class


class Update:
    @staticmethod
    def enter(t, e):
        pass

    @staticmethod
    def exit(t, e):
        pass

    @staticmethod
    def do(t):
        calc_pps()
        update_target(t)
        make_target_point(t)

    @staticmethod
    def draw(t):
        draw_target(t)


class StateMachineTarget:
    def __init__(self, t):
        self.t = t
        self.cur_state = Update
        self.table = {
            Update: {},
        }

    def start(self):
        self.cur_state.enter(self.t, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.t)

    def handle_event(self, e):  # state event handling
        for check_event, next_state in self.table[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.t, e)
                self.cur_state = next_state
                self.cur_state.enter(self.t, e)
                return True
        return False

    def draw(self):
        self.cur_state.draw(self.t)


class Target:
    def __init__(self, p, weapon):
        load_target(self)
        self.p = p
        self.weapon = weapon

        self.dis, self.recoil = 0, 0
        self.dis2 = 0
        self.reduce_delay = 0

        self.tx, self.ty = 0, 0  # 조준점 범위 내에서 랜점으로 생성되는 좌표
        self.target_dot_display_time = 0

        self.tmx = 0  # 근접무기 타겟 x 좌표
        self.tmy = 0  # 근접무기 타겟 y 좌표

        self.state_machine = StateMachineTarget(self)
        self.state_machine.start()

    def draw(self):
        self.state_machine.draw()

    def update(self):
        if game_framework.MODE == 'play':
            self.state_machine.update()

    def handle_events(self, event):
        self.state_machine.handle_event(('INPUT', event))
