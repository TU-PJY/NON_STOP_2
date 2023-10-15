from Func.Weapon_func import *


# Player location -> Gun class
# 이름은 Class_Gun 이지만 근접무기도 여기서 처리한다.


class Shoot:
    @staticmethod
    def enter(gun, e):
        if l_down(e):
            if gun.weapon_type == 0:
                gun.trigger = True
            elif gun.weapon_type == 1:
                gun.use = True

    @staticmethod
    def exit(gun, e):
        gun.trigger = False
        gun.shoot = False
        gun.use = False

    @staticmethod
    def do(gun):
        update_delay(gun)
        shoot_gun(gun)
        wield_melee(gun)

    @staticmethod
    def draw(gun):
        draw_gun(gun)
        draw_melee(gun)
        draw_flame(gun)
        update_melee_position(gun)


class Idle:
    @staticmethod
    def enter(gun, e):
        pass

    @staticmethod
    def exit(gun, e):
        pass

    @staticmethod
    def do(gun):
        update_delay(gun)
        update_melee_position(gun)

    @staticmethod
    def draw(gun):
        draw_gun(gun)
        draw_melee(gun)
        draw_flame(gun)


class StateMachineGun:
    def __init__(self, gun):
        self.gun = gun
        self.cur_state = Idle
        self.table = {
            Idle: {l_down: Shoot},
            Shoot: {l_up: Idle}
        }

    def start(self):
        self.cur_state.enter(self.gun, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.gun)

    def handle_event(self, e):  # state event handling
        for check_event, next_state in self.table[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.gun, e)
                self.cur_state = next_state
                self.cur_state.enter(self.gun, e)
                return True
        return False

    def draw(self):
        self.cur_state.draw(self.gun)


class Weapon:
    def __init__(self, p):
        load_gun_image(self)
        load_melee_image(self)
        self.p = p

        self.weapon_type = 0  # 0: Gun, 1: Melee
        self.name = 'SCAR_H'
        self.deg = 0  # 총 이미지 각도

        self.trigger = False
        self.shoot = False
        self.shoot_delay = 0

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
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))
