from class_manager.weapon_manager.etc import *
from class_manager.weapon_manager.file_loader import load_gun_image, load_melee_image
from class_manager.weapon_manager.flame_output import draw_flame
from class_manager.weapon_manager.gun_output import draw_gun
from class_manager.weapon_manager.gun_shoot import shoot_gun
from class_manager.weapon_manager.melee_output import draw_melee
from class_manager.weapon_manager.melee_wield import wield_melee
from class_manager.weapon_manager.weapon_animation import spin_win, update_melee_position
from game_work import game_framework


class Shoot:
    @staticmethod
    def enter(weapon, e):
        if weapon.weapon_type == 0:
            weapon.trigger = True
            if weapon.reload_need:
                weapon.reloading = True

        elif weapon.weapon_type == 1:
            weapon.use = True

    @staticmethod
    def exit(weapon, e):
        weapon.trigger = False
        weapon.shoot = False
        weapon.use = False

        if weapon.gun == 'LVOAS':  # LVOAS는 2점사 소총이므로 따로 처리를 해주어야 한다
            weapon.shoot_count = 0

        if q_down(e):
            change_weapon(weapon)

        if r_down(e) and weapon.weapon_type == 0:
            if weapon.gun == 'sr':
                if not weapon.zoom:
                    weapon.zoom = True
                elif weapon.zoom:
                    weapon.zoom = False

        if weapon.limit_ammo - weapon.cur_ammo > 0:  # 탄창이 꽉 찬 상태에서는 재장전을 실행하지 않는다
            if reload_down(e) and not weapon.reloading:  # 재장전
                weapon.reloading = True


    @staticmethod
    def do(weapon):
        update_delay(weapon)
        shoot_gun(weapon)
        wield_melee(weapon)
        if weapon.is_spin:
            spin_win(weapon)
        update_sniper_bolt(weapon)

        if weapon.reloading:
            reload_gun(weapon)

    @staticmethod
    def draw(weapon):
        draw_gun(weapon)
        draw_melee(weapon)
        draw_flame(weapon)
        update_melee_position(weapon)


class Idle:
    @staticmethod
    def enter(weapon, e):
        pass

    @staticmethod
    def exit(weapon, e):
        if q_down(e):
            change_weapon(weapon)
        if r_down(e) and weapon.weapon_type == 0:
            if weapon.gun_type == 'sr':
                if not weapon.zoom:
                    weapon.zoom = True
                elif weapon.zoom:
                    weapon.zoom = False

        if weapon.limit_ammo - weapon.cur_ammo > 0:  # 탄창이 꽉 찬 상태에서는 재장전을 실행하지 않는다
            if reload_down(e) and not weapon.reloading:  # 재장전
                weapon.reloading = True

    @staticmethod
    def do(weapon):
        update_delay(weapon)
        update_melee_position(weapon)
        if weapon.is_spin:
            spin_win(weapon)
        update_sniper_bolt(weapon)

        if weapon.reloading:
            reload_gun(weapon)

    @staticmethod
    def draw(weapon):
        draw_gun(weapon)
        draw_melee(weapon)
        draw_flame(weapon)


class StateMachineGun:
    def __init__(self, weapon):
        self.weapon = weapon
        self.cur_state = Idle
        self.table = {
            Idle: {l_down: Shoot, q_down: Idle, r_down: Idle, r_up: Idle, reload_down: Idle},
            Shoot: {l_up: Idle, q_down: Shoot, r_down: Shoot, r_up: Shoot, reload_down: Idle}
        }

    def start(self):
        self.cur_state.enter(self.weapon, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.weapon)

    def handle_event(self, e):  # state event handling
        for check_event, next_state in self.table[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.weapon, e)
                self.cur_state = next_state
                self.cur_state.enter(self.weapon, e)
                return True
        return False

    def draw(self):
        self.cur_state.draw(self.weapon)


class Weapon:
    def __init__(self, p, mp):
        load_gun_image(self)
        load_melee_image(self)
        self.p = p
        self.mp = mp

        self.weapon_type = 0  # 0: Gun, 1: Melee
        self.gun = 'M1911'
        self.deg = 0  # 총 이미지 각도
        self.flip = ''

        self.trigger = False  # 마우스 좌클릭 시 True
        self.shoot = False  # True일시 격발
        self.shoot_delay = 0  # 0이 될때마다 self.shoot == True
        self.gun_type = 'pistol'  # 현재 총 타입 
        self.prev_gun_type = 'pistol'  # 교체 전 이전 총 타입 

        self.flame_display_time = 0

        self.melee = 'KNIFE'
        self.melee_x = 0
        self.melee_deg = 170
        self.use = False
        self.wield = False
        self.wield_delay = 0

        self.hit_once = False  # 겹쳐있는 몬스터에게 한꺼번에 대미지를 주지 않도록 한다.

        # sr 전용 변수
        self.zoom = False
        self.bolt_action = False

        # sr, WIN 전용 변수
        self.spin = 0
        self.is_spin = False
        self.shell_out = False

        # LVOAS 전용 변수
        self.shoot_count = 0

        # QHAND 전용 변수
        self.fire_pos = 'in'  # in이면 안쪽 총, out이면 바깥쪽 총

        # 관통 구현 변수
        self.pen_enable = False
        self.pen_count = 0
        self.pen_limit = 0

        # 탄약 관련
        # 개발 중에는 99999로 초기화
        self.num_ammo_small = 99999  # pistol, smg 탄종, 게임 시작 시 기본으로 100발이 주어짐
        self.num_ammo_middle = 99999  # ar, 일부 rifle 탄종
        self.num_ammo_big = 99999  # rifle, ar 탄종

        # self.num_ammo_small = 100  # pistol, smg 탄종, 게임 시작 시 기본으로 100발이 주어짐
        # self.num_ammo_middle = 0  # ar, 일부 rifle 탄종
        # self.num_ammo_big = 0  # rifle, ar 탄종

        self.cur_ammo = 7  # 현재 탄창에 있는 탄약 수, 기본 권총의 장탄 수 
        self.limit_ammo = 7  # 총기마다 다른 장탄수를 가진다.

        self.reload_need = False  # true일 시 발사 불가
        self.reload_time = 150  # 재장전 소요 시간
        self.cur_reload_time = 0  # 해당 값이 reload_time에 도달해야 재장전이 완료된다.

        self.reloading = False # true일 시 재장전 중

        self.state_machine = StateMachineGun(self)
        self.state_machine.start()

    def draw(self):
        self.state_machine.draw()

    def update(self):
        if game_framework.MODE == 'play':
            self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))
