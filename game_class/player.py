from class_manager.player_manager import *
from game_work.display_manager import *
from mods import play_mode


# 실시간으로 총이 마우스 좌표를 향해야 하므로 Class_Player가 마우스 좌표를 받아 Class_Gun으로 전달한다.
# 플레이어 이동 시 맵 자체가 움직이는 방식이기 때문에 컨트롤러의 키 누름 여부와 현재 플레이어 좌표를 Class_Map으로 전달한다.
# 화면 효과는 전적으로 Player 클래스에서 구동된다.


class Move:
    @staticmethod
    def enter(p, e):
        if right_down(e) or left_up(e):
            p.mv_right = True

        if right_up(e) or left_down(e):
            p.mv_left = True

    @staticmethod
    def exit(p, e):
        if space_down(e):
            if not p.mv_jump:
                if p.jump_count < p.jump_level:
                    p.jump_acc = JUMP_ACC
                    p.jump_count += 1
                    p.mv_jump = True
        else:
            if play_mode.weapon.melee == 'KATANA' and play_mode.weapon.skill_enable:
                play_mode.weapon.skill_enable = False
                p.rotate = 0
                p.speed = p.temp_speed

            p.mv_right = False
            p.mv_left = False

            p.size_up = True
            p.size_deg = 0
            p.size = 0

    @staticmethod
    def do(p):
        if not play_mode.weapon.skill_enable:
            p.dir = 1 if p.mx > p.x else 0

        jump(p)
        walk_animation(p)
        look_mouse(p)
        update_camera(p)
        process_effect(p)
        update_damage_delay(p)

        shake_display(p)
        push_display(p)
        dmg_shake(p)

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
            if not p.mv_jump:
                if p.jump_count < p.jump_level:
                    p.jump_acc = JUMP_ACC
                    p.jump_count += 1
                    p.mv_jump = True

    @staticmethod
    def do(p):
        if not play_mode.weapon.skill_enable:
            p.dir = 1 if p.mx > p.x else 0

        jump(p)
        look_mouse(p)
        update_camera(p)
        process_effect(p)
        update_damage_delay(p)

        push_display(p)
        shake_display(p)
        dmg_shake(p)

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
        self.mx, self.my = 0, 0  # 마우스 좌표

        self.hp = 200

        # player data
        self.x, self.y, self.dir = WIDTH / 2, 250, 1
        self.mv_right, self.mv_left, self.mv_jump = False, False, False  # 플레이어 이동, 점프
        self.dmg_delay = 0  # 플레이어가 받는 대미지 딜레이

        self.temp_speed = 0  # 추후 근접무기 특수 능력 구현에 사용
        self.speed = 4  # 플레이어 이동 속도 (사실상 맵 움직이는 속도)
        self.jump_acc = JUMP_ACC
        self.jump_count = 0
        self.jump_level = 1  # 레벨이 오를수록 연속 점프 횟수가 많아짐
        self.jump_delay = 0

        self.coin = 0

        self.rotate = 0  # 플레이어가 마우스 좌표를 살짝 따라 본다

        self.size = 0  # 걸을 때 플레이어 크기가 고무줄처럼 커졌다 작아진다.
        self.size_deg = 0
        self.look_mouse = True  # True일 시 플레이어는 마우스를 따라본다.

        # display effects
        self.push_y = 0  # 이 수치만큼 화면의 모든 이미지들이 아래로 눌린다.
        self.shake_x, self.shake_y = 0, 0
        self.shake_range = 0  # 화면 흔들림의 정도
        self.camera_y = 0  # 화면이 마우스 좌표를 살짝 따라간다.
        self.camera_x = 0
        self.camera_h = 0  # 플레이어 점프 시 플레이어, 무기를 제외한 나머지 객제들의 위치가 살짝 내려간다.

        self.dmg_shake_range = 0
        self.shake_dx, self.shake_dy = 0, 0

        self.ex, self.ey = 0, 0  # 플레이어 좌표를 제외한 디스플레이 효과 변수. 객체 좌표에 더하여 사용
        self.px, self.py = 0, 0  # 플레이어 좌표
        self.wx, self.wy = 0, 0  # 무기 좌표

        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        if game_framework.MODE == 'play':
            self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.px - 40, self.py - 65 - self.size * 50, self.px + 40, self.py + 60 - self.size * 50

    def handle_collision(self, group, other):
        pass
