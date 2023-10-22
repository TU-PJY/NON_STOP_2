from game_work.display_manager import *
from class_manager.player_manager import *


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
        if space_down(e):
            p.mv_jump = True
        else:
            p.mv_right = False
            p.mv_left = False

            p.size_up = True
            p.size_deg = 0
            p.size = 0

    @staticmethod
    def do(p):
        p.dir = 1 if p.mx > p.x else 0

        walk_animation(p)
        jump(p)
        look_mouse(p)
        update_camera(p)
        calculate_player_pos(p)
        update_damage_delay(p)

        shake_display(p)
        push_display(p)

    @staticmethod
    def draw(p):
        draw_player(p)


class Idle:
    @staticmethod
    def enter(p, e):
        pass

    @staticmethod
    def exit(p, e):
        if space_down(e):
            p.mv_jump = True

    @staticmethod
    def do(p):
        p.dir = 1 if p.mx > p.x else 0
        jump(p)
        look_mouse(p)
        update_camera(p)
        calculate_player_pos(p)
        update_damage_delay(p)

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
            Idle: {right_down: Move, left_down: Move, left_up: Move, right_up: Move, space_down: Idle},
            Move: {right_down: Idle, left_down: Idle, left_up: Idle, right_up: Idle, space_down: Move},
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
        self.mv_right, self.mv_left, self.mv_jump = False, False, False  # 플레이어 이동, 점프
        self.px, self.py, self.py2 = 0, 0, 0  # 디스플레이 효과를 모두 포함한 최종 좌표
        self.efx, self.efy = 0, 0  # 플레이어 좌표를 제외한 디스플레이 효과 변수. 객체 좌표에 더하여 사용

        self.mx, self.my = 0, 0  # 마우스 좌표

        self.dmg_delay = 0

        self.speed = 4  # 플레이어 이동 속도 (사실상 맵 움직이는 속도)
        self.jump_acc = JUMP_ACC
        self.acc_delay = 0
        self.land_y = 0  # 이 수치만큼 화면의 모든 이미지들이 아래로 눌린다.
        self.rotate = 0  # 플레이어가 마우스 좌표를 살짝 따라 본다

        self.shake_time = 0  # 화면 흔들림 변수. time이 1 이상일 경우 화면이 흔들리게 된다.
        self.shake_x, self.shake_y = 0, 0
        self.shake_range = 0  # 화면 흔들림의 정도

        self.size = 0  # 걸을 때 플레이어 크기가 고무줄처럼 커졌다 작아진다.
        self.size_deg = 0
        self.size_up = True

        self.look_mouse = True  # True일 시 플레이어는 마우스를 따라본다.

        self.camera_y = 0  # 화면이 마우스 좌표를 살짝 따라간다.
        self.camera_x = 0

        self.p_to_wall_left = 0
        self.p_to_wall_right = 0  # 플레이어와 벽간의 거리, 몬스터 벽 충돌 처리에 사용

        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
