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

    @staticmethod
    def do(weapon):
        update_delay(weapon)
        shoot_gun(weapon)
        wield_melee(weapon)
        if weapon.is_spin:
            spin_win(weapon)
        update_sniper_bolt(weapon)

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

    @staticmethod
    def do(weapon):
        update_delay(weapon)
        update_melee_position(weapon)
        if weapon.is_spin:
            spin_win(weapon)
        update_sniper_bolt(weapon)

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
            Idle: {l_down: Shoot, q_down: Idle, r_down: Idle, r_up: Idle},
            Shoot: {l_up: Idle, q_down: Shoot, r_down: Shoot, r_up: Shoot}
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
        self.gun = 'AKS74'
        self.deg = 0  # 총 이미지 각도
        self.flip = ''

        self.trigger = False  # 마우스 좌클릭 시 True
        self.shoot = False  # True일시 격발
        self.shoot_delay = 0  # 0이 될때마다 self.shoot == True
        self.gun_type = 'smg'

        self.flame_display_time = 0

        self.melee = 'KNIFE'
        self.melee_x = 0
        self.melee_deg = 170
        self.use = False
        self.wield = False
        self.wield_delay = 0

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

        self.state_machine = StateMachineGun(self)
        self.state_machine.start()

    def draw(self):
        self.state_machine.draw()

    def update(self):
        if game_framework.MODE == 'play':
            self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))
