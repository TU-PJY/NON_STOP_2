from func.monster_manager import *


class Update:
    @staticmethod
    def enter(m, e):
        pass

    @staticmethod
    def exit(m, e):
        pass

    @staticmethod
    def do(m):
        update_frame(m)
        update_monster_pos(m)
        move_monster(m)
        process_attack(m)
        update_delay(m)
        update_monster_size(m)

    @staticmethod
    def draw(m):
        draw_monster(m)


class StateMachineTarget:
    def __init__(self, m):
        self.m = m
        self.cur_state = Update
        self.table = {
            Update: {},
        }

    def start(self):
        self.cur_state.enter(self.m, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.m)

    def handle_event(self, e):  # state event handling
        for check_event, next_state in self.table[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.m, e)
                self.cur_state = next_state
                self.cur_state.enter(self.m, e)
                return True
        return False

    def draw(self):
        self.cur_state.draw(self.m)


class Monster:
    def __init__(self, p, weapon, target, x, y, speed, hp, frame, fdelay, monster_type):
        load_monster(self)
        self.p, self.weapon, self.target = p, weapon, target
        self.type, self.x, self.y, self.hp, self.speed, self.frame, self.fdelay =\
            monster_type, x, y, hp, speed, frame, fdelay

        self.atk_delay, self.dir = 0, 0
        self.attack_motion_time = 0  # 해당 시간동안 공격 모션을 보여준다.
        self.size = 0  # 공격 시 크기 변화 애니메이션

        self.is_attack, self.is_hit = False, False

        self.is_dash = False  # 몬스터 대쉬 공격 여부
        self.dash_delay = 0
        self.temp_x, self.temp_y = 0, 0
        self.incline = 0

        self.state_machine = StateMachineTarget(self)
        self.state_machine.start()

    def draw(self):
        self.state_machine.draw()

    def update(self):
        self.state_machine.update()

    def handle_events(self, event):
        self.state_machine.handle_event(('INPUT', event))
