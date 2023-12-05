from game_class.prop import PlayerDamage
from game_class_manager.player_manager import *
from game_work import game_manager
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
        if space_down(e) and not play_mode.weapon.skill_enable:
            if p.jump_count < p.jump_level:
                p.jump_sound.play()
                if p.jump_count == 0:
                    p.jump_acc = JUMP_ACC
                else:
                    p.jump_acc = JUMP_ACC / 1.2  # 두 번쨰 점프는 가속도를 조금 적게 준다
                p.jump_count += 1
                p.sound_delay = 0
                p.mv_jump = True

        elif ctrl_down(e):  # 응급처치 키드를 사용하여 체력 회복
            if p.medkit_count > 0 and p.cur_hp < p.hp and p.usable_medkit:
                p.medkit_sound.play()
                p.cur_hp += 100
                p.medkit_count -= 1
                heal = PlayerDamage(True)  # 플레이어 대미지 피드백 클래스를 활용한다
                game_manager.add_object(heal, 7)
                if p.cur_hp > p.hp:
                    p.cur_hp = p.hp
                    p.regen_timer = 0
                set_medkit_delay(p)

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

            # p.sound_delay = 0

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
        explode_shake(p)

        update_medkit_delay(p)
        regen_hp(p)
        check_hp(p)

        play_player_sound(p)

    @staticmethod
    def draw(p):
        draw_player(p)


class Idle:
    @staticmethod
    def enter(p, e):
        pass

    @staticmethod
    def exit(p, e):
        if space_down(e) and not play_mode.weapon.skill_enable:
            if p.jump_count < p.jump_level:
                p.jump_sound.play()
                if p.jump_count == 0:
                    p.jump_acc = JUMP_ACC
                else:
                    p.jump_acc = JUMP_ACC / 1.3  # 두 번쨰 점프부터 가속도를 조금 적게 준다
                p.jump_count += 1
                p.mv_jump = True

        elif ctrl_down(e):  # 응급처치 키드를 사용하여 체력 회복
            if p.medkit_count > 0 and p.cur_hp < p.hp and p.usable_medkit:
                p.medkit_sound.play()
                p.cur_hp += 100
                p.medkit_count -= 1
                heal = PlayerDamage(True)  # 플레이어 대미지 피드백 클래스를 활용한다
                game_manager.add_object(heal, 7)
                if p.cur_hp > p.hp:
                    p.cur_hp = p.hp
                    p.regen_timer = 0
                set_medkit_delay(p)

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
        explode_shake(p)

        update_medkit_delay(p)
        regen_hp(p)
        check_hp(p)

    @staticmethod
    def draw(p):
        draw_player(p)


class StateMachine:
    def __init__(self, p):
        self.p = p
        self.cur_state = Idle
        self.table = {
            Idle: {right_down: Move, left_down: Move, left_up: Move, right_up: Move, space_down: Idle, ctrl_down: Idle},
            Move: {right_down: Idle, left_down: Idle, left_up: Idle, right_up: Idle, space_down: Move, ctrl_down: Move},
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

        self.mx, self.my = WIDTH / 2 - 10, 250

        self.hp = 200  # 업그레이드하면 체력이 커진다
        self.cur_hp = 200  # 현재 체력, 피격 시 감소한다
        self.regen_timer = 0
        self.regen_delay = 700  # 플레이어 체력 회복 딜레이

        self.medkit_count = 1  # 회복 아이템 개수
        self.medkit_delay_time = 0
        self.medkit_delay_temp = 0
        self.medkit_delay = 0
        self.usable_medkit = True

        # player data
        self.x, self.y, self.dir = WIDTH / 2, 250, 1
        self.mv_right, self.mv_left, self.mv_jump = False, False, False  # 플레이어 이동, 점프
        self.dmg_delay = 0  # 플레이어가 받는 대미지 딜레이

        self.temp_speed = 0  # 추후 근접무기 특수 능력 구현에 사용
        self.speed = 1  # 플레이어 이동 속도 (사실상 맵 움직이는 속도)
        self.jump_acc = JUMP_ACC
        self.jump_count = 0
        self.jump_level = 2  # 레벨이 오를수록 연속 점프 횟수가 많아짐
        self.jump_delay = 0

        self.coin = 300000  # 플레이어가 소지한 코인 개수
        self.get_coin = False  # true일 시 코인 획득 피드백 재생

        self.rotate = 0  # 플레이어가 마우스 좌표를 살짝 따라 본다

        self.size = 0  # 걸을 때 플레이어 크기가 고무줄처럼 커졌다 작아진다.
        self.size_deg = 0
        self.look_mouse = True  # True일 시 플레이어는 마우스를 따라본다.

        # display effects
        self.push_y = 0  # 이 수치만큼 화면의 모든 이미지들이 아래로 눌린다.
        self.shake_x, self.shake_y = 0, 0
        self.shake_range = 0  # 화면 흔들림의 정도
        self.cam_y = 0  # 카메라 변수, 객체 좌표에 더하여 사용
        self.cam_x = 0
        self.cam_h = 0  # 플레이어 점프 시 플레이어, 무기를 제외한 나머지 객제들의 위치가 살짝 내려간다.

        self.dmg_shake_range = 0  # 플레이어가 대미지를 받을 시 화면이 흔들리는 수치
        self.shake_dx, self.shake_dy = 0, 0

        self.ex_shake_range = 0  # 폭발물 폭발 시 화면아 흔들리는 수치
        self.shake_ex, self.shake_ey = 0, 0

        self.ex, self.ey = 0, 0  # 플레이어 좌표를 제외한 디스플레이 효과 변수. 객체 좌표에 더하여 사용
        self.px, self.py = 0, 0  # 플레이어 좌표
        self.wx, self.wy = 0, 0  # 무기 좌표

        # 업그레이드 정보를 유지하기 위해 player 클래스에 저장
        self.hp_count = 0  # 최대 3단계
        self.regen_count = 0  # 최대 3단계
        self.speed_count = 0  # 최대 3단계
        self.double_jump = 0  # 최대 1단계, play_mode.p.jump_level로 전달
        self.gren_count = 0  # 최대 2단계

        self.hp_cost = 1500
        self.regen_cost = 1500
        self.speed_cost = 1500
        self.gren_cost = 10000
        self.medkit_cost = 1000  # 기본 1000에서 시작하여 1000씩 비싸진다

        self.sound_delay = 0

        self.volume = 64
        self.play_bgm.set_volume(self.volume)

        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        if game_framework.MODE == 'play':
            self.state_machine.update()

    def __getstate__(self):
        state = {'ch': self.ch}
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.__init__()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.px - 35, self.py - 60 - self.size * 50, self.px + 35, self.py + 60

    def handle_collision(self, group, other):
        pass
