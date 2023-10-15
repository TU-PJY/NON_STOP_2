from Func.Display_func import *
from Func.Player_func import *


# 실시간으로 총이 마우스 좌표를 향해야 하므로 Class_Player가 마우스 좌표를 받아 Class_Gun으로 전달한다.
# 플레이어 이동 시 맵 자체가 움직이는 방식이기 때문에 컨트롤러의 키 누름 여부와 현재 플레이어 좌표를 Class_Map으로 전달한다.
# 화면 효과는 전적으로 Player 클래스에서 구동된다.


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

        p.size_up = True
        p.size_deg = 0
        p.y_size = 0

    @staticmethod
    def do(p):
        p.dir = 1 if p.mx > p.x else 0
        jump(p)
        look_mouse(p)
        shake_display(p)
        push_display(p)
        walk_animation(p)

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
        jump(p)
        look_mouse(p)
        push_display(p)
        shake_display(p)

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
        load_player_image(self)

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

        self.shoot_shake = False
        self.shake_timer = 0
        self.shake_x, self.shake_y = 0, 0
        self.shake_range = 0

        self.y_size = 0  # 걸을 때 플레이어 크기가 고무줄처럼 커졌다 작아진다.
        self.size_deg = 0
        self.size_up = True

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
