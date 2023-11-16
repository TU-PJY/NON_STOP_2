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
        make_target_point(t)
        update_target(t)

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

        self.tmx = 0  # 근접무기 타겟 x 좌표
        self.tmy = 0  # 근접무기 타겟 y 좌표

        self.scope_size_x, self.scope_size_y = 32768, 16384
        self.draw_scope = False

        self.state_machine = StateMachineTarget(self)
        self.state_machine.start()

    def draw(self):
        if game_framework.MODE == 'play':
            self.state_machine.draw()
        if self.weapon.weapon_type == 1:
            draw_rectangle(*self.get_melee_bb())

    def update(self):
        if game_framework.MODE == 'play':
            self.state_machine.update()

    def handle_events(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def handle_collision(self, group, other):
        pass

    def get_bb(self):
        if self.weapon.weapon_type == 0:  # 총의 경우 타겟 내부에 생성된 지점을 히트박스로 리턴한다.
            if not self.weapon.gun_type == 'sr' and self.weapon.shoot:  # 총을 쏘는 순간에만 조준점 좌표를 제공한다.
                return self.tx, self.ty, self.tx, self.ty

            elif self.weapon.gun_type == 'sr' and self.weapon.zoom and self.weapon.shoot:
                return self.tx, self.ty, self.tx, self.ty

            else:
                return -9999, -9999, -9999, -9999

        elif self.weapon.weapon_type == 1:  # 근접무기 히트박스, 방향에 따라 좌표가 다름
            if self.weapon.wield:
                if self.weapon.melee == 'KNIFE':
                    if self.p.dir == 0:
                        return self.tmx + self.p.ex, self.tmy + self.p.ey - 35 - self.p.cam_h, \
                               self.p.x + self.p.ex, self.p.y + self.p.ey + 30 - self.p.cam_h
                    elif self.p.dir == 1:
                        return self.p.x + self.p.ex, self.p.y + self.p.ey - 35 - self.p.cam_h, \
                               self.tmx + self.p.ex, self.p.y + self.p.ey + 30 - self.p.cam_h

                elif self.weapon.melee == 'BAT':
                    if self.p.dir == 0:
                        return self.tmx + self.p.ex, self.tmy + self.p.ey - 65 - self.p.cam_h, \
                               self.p.x + self.p.ex, self.p.y + self.p.ey + 80 - self.p.cam_h
                    elif self.p.dir == 1:
                        return self.p.x + self.p.ex, self.p.y + self.p.ey - 65 - self.p.cam_h, \
                               self.tmx + self.p.ex, self.p.y + self.p.ey + 80 - self.p.cam_h

                elif self.weapon.melee == 'RAPIER':
                    if self.p.dir == 0:
                        return self.tmx + self.p.ex, self.tmy + self.p.ey - 35 - self.p.cam_h, \
                               self.p.x + self.p.ex, self.p.y + self.p.ey + 30 - self.p.cam_h
                    elif self.p.dir == 1:
                        return self.p.x + self.p.ex, self.p.y + self.p.ey - 35 - self.p.cam_h, \
                               self.tmx + self.p.ex, self.p.y + self.p.ey + 30 - self.p.cam_h

                elif self.weapon.melee == 'KATANA':
                    if self.p.dir == 0:
                        return self.tmx + self.p.ex, self.tmy + self.p.ey - 65 - self.p.cam_h, \
                               self.p.x + self.p.ex, self.p.y + self.p.ey + 100 - self.p.cam_h
                    elif self.p.dir == 1:
                        return self.p.x + self.p.ex, self.p.y + self.p.ey - 65 - self.p.cam_h, \
                               self.tmx + self.p.ex, self.p.y + self.p.ey + 100 - self.p.cam_h

            elif self.weapon.skill_enable:
                if self.weapon.melee == 'KATANA':
                    if self.p.dir == 0:
                        return self.tmx + self.p.ex, self.tmy + self.p.ey - 65 - self.p.cam_h, \
                               self.p.x + self.p.ex, self.p.y + self.p.ey + 100 - self.p.cam_h
                    elif self.p.dir == 1:
                        return self.p.x + self.p.ex, self.p.y + self.p.ey - 65 - self.p.cam_h, \
                               self.tmx + self.p.ex, self.p.y + self.p.ey + 100 - self.p.cam_h

                elif self.weapon.melee == 'RAPIER':
                    if self.p.dir == 0:
                        return self.tmx + self.p.ex, self.tmy + self.p.ey - 35 - self.p.cam_h, \
                               self.p.x + self.p.ex, self.p.y + self.p.ey + 30 - self.p.cam_h
                    elif self.p.dir == 1:
                        return self.p.x + self.p.ex, self.p.y + self.p.ey - 35 - self.p.cam_h, \
                               self.tmx + self.p.ex, self.p.y + self.p.ey + 30 - self.p.cam_h

            else:
                return -9999, -9999, -9999, -9999

    def get_melee_bb(self):  # 디버깅용 bb, 히트박스 출력용
        if self.weapon.melee == 'KNIFE':
            if self.p.dir == 0:
                return self.tmx + self.p.ex, self.tmy + self.p.ey - 35 - self.p.cam_h, \
                       self.p.x + self.p.ex, self.p.y + self.p.ey + 30 - self.p.cam_h
            elif self.p.dir == 1:
                return self.p.x + self.p.ex, self.p.y + self.p.ey - 35 - self.p.cam_h, \
                       self.tmx + self.p.ex, self.p.y + self.p.ey + 30 - self.p.cam_h

        elif self.weapon.melee == 'BAT':
            if self.p.dir == 0:
                return self.tmx + self.p.ex, self.tmy + self.p.ey - 65 - self.p.cam_h, \
                       self.p.x + self.p.ex, self.p.y + self.p.ey + 80 - self.p.cam_h
            elif self.p.dir == 1:
                return self.p.x + self.p.ex, self.p.y + self.p.ey - 65 - self.p.cam_h, \
                       self.tmx + self.p.ex, self.p.y + self.p.ey + 80 - self.p.cam_h

        elif self.weapon.melee == 'RAPIER':
            if self.p.dir == 0:
                return self.tmx + self.p.ex, self.tmy + self.p.ey - 35 - self.p.cam_h, \
                       self.p.x + self.p.ex, self.p.y + self.p.ey + 30 - self.p.cam_h
            elif self.p.dir == 1:
                return self.p.x + self.p.ex, self.p.y + self.p.ey - 35 - self.p.cam_h, \
                       self.tmx + self.p.ex, self.p.y + self.p.ey + 30 - self.p.cam_h

        elif self.weapon.melee == 'KATANA':
            if self.p.dir == 0:
                return self.tmx + self.p.ex, self.tmy + self.p.ey - 65 - self.p.cam_h, \
                       self.p.x + self.p.ex, self.p.y + self.p.ey + 100 - self.p.cam_h
            elif self.p.dir == 1:
                return self.p.x + self.p.ex, self.p.y + self.p.ey - 65 - self.p.cam_h, \
                       self.tmx + self.p.ex, self.p.y + self.p.ey + 100 - self.p.cam_h
