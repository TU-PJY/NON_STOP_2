from class_manager.weapon_manager import *


# Player location -> Gun class


class Shoot:
    @staticmethod
    def enter(weapon, e):
        if weapon.weapon_type == 0:
            weapon.trigger = True
        elif weapon.weapon_type == 1:
            weapon.use = True

    @staticmethod
    def exit(weapon, e):
        if weapon.gun == 'M1':  # 반자동 소총만 예외적으로 트리거 해제 시 연사 딜레이가 초기화 되도록 함
            weapon.shoot_delay = 0

        weapon.trigger = False
        weapon.shoot = False
        weapon.use = False

        if q_down(e):
            change_weapon(weapon)

    @staticmethod
    def do(weapon):
        calc_pps()
        update_delay(weapon)
        shoot_gun(weapon)
        wield_melee(weapon)

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

    @staticmethod
    def do(weapon):
        calc_pps()
        update_delay(weapon)
        update_melee_position(weapon)

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
            Idle: {l_down: Shoot, q_down: Idle},
            Shoot: {l_up: Idle, q_down: Shoot}
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
    def __init__(self, p):
        load_gun_image(self)
        load_melee_image(self)
        self.p = p

        self.weapon_type = 0  # 0: Gun, 1: Melee
        self.gun = 'SCAR_H'
        self.deg = 0  # 총 이미지 각도
        self.flip = ''

        self.trigger = False  # 마우스 좌클릭 시 True
        self.shoot = False  # True일시 격발
        self.shoot_delay = 0  # 0이 될때마다 self.shoot == True

        self.flame_display_time = 0

        self.melee = 'KNIFE'
        self.melee_x = 0
        self.melee_deg = 170
        self.use = False
        self.wield = False
        self.wield_delay = 0

        self.state_machine = StateMachineGun(self)
        self.state_machine.start()

    def draw(self):
        self.state_machine.draw()

    def update(self):
        if game_framework.MODE == 'play':
            self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))
