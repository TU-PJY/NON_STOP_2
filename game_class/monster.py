from pico2d import draw_rectangle, load_wav, load_image
from game_class.prop import PlayerDamage, Feedback
from game_class_manager.monster_manager.etc import monster_animation, update_monster_pos, update_monster_opacify, \
    update_delay, update_monster_size
from game_class_manager.monster_manager.file_loader import load_file
from game_class_manager.monster_manager.monster_attack import process_attack
from game_class_manager.monster_manager.monster_damage import damage_monster
from game_class_manager.monster_manager.monster_move import move_monster
from game_class_manager.monster_manager.monster_output import draw_monster
from game_work import game_framework, game_manager
from config import *


class Update:
    @staticmethod
    def enter(m, e):
        pass

    @staticmethod
    def exit(m, e):
        pass

    @staticmethod
    def do(m):
        damage_monster(m)
        monster_animation(m)
        update_monster_pos(m)
        update_monster_opacify(m)
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
    type1 = None
    type1_damage = None
    type2 = None
    type2_damage = None
    type3 = None
    type3_damage = None
    type4 = None
    type4_damage = None

    hp_back = None
    hp_front = None

    bow = None

    def __init__(self, p, weapon, target, mp, x, y, speed, hp, frame, monster_type):
        self.p, self.weapon, self.target = p, weapon, target
        self.mp = mp
        self.type, self.x, self.y, self.hp, self.speed, self.frame = \
            monster_type, x, y, hp, speed, frame

        load_file(self)

        # 공용 변수
        self.atk_delay, self.dir = 0, 0
        self.attack_motion_time = 0  # 해당 시간동안 공격 모션을 보여준다.
        self.size = 0  # 공격 시 크기 변화 애니메이션
        self.is_attack, self.is_hit = False, False
        self.incline = 0
        self.hp_length = self.hp
        self.op = 0
        self.flip = ''
        self.once = False  # 대미지가 중복으로 발생하지 않도록 한다.
        self.ex_dead = False

        #  저지력이 강한 총기는 일정 시간동안 강력한 넉백을 가한다
        self.knockback = False  # true이면 뒤로 밀려난다
        self.knockback_dir = 0  # 바라보는 방향 기준으로 넉백 방향을 지정한다
        self.back_acc = 0  # 넉백 가속

        # type2 전용 변수
        if self.type == 2:
            self.is_dash = False
            self.dash_delay = 0
            self.temp_x, self.temp_y = 0, 0  # 대쉬 목적지 좌표

        # type3 전용 변수
        elif self.type == 3:
            self.is_jump = False
            self.size2 = 0  # rubber animation 크기 변수
            self.size_deg = 0  # rubber animation 전용 크기 변수
            self.jump_acc = 0
            self.acc_delay = 0
            self.jump_delay = 0  # 0이 될때마다 점프

        # type4 전용 변수
        elif self.type == 4:
            self.is_shoot = False
            self.shoot_delay = 100

        self.state_machine = StateMachineTarget(self)
        self.state_machine.start()

    def draw(self):
        self.state_machine.draw()
        # draw_rectangle(*self.get_bb())

    def update(self):
        if game_framework.MODE == 'play':
            self.state_machine.update()

            # sr계열 격발 후 다시 관통 대미지를 한 번만 주도록 세팅한다.
            if self.weapon.shoot_delay <= 10 and self.weapon.weapon_type == 0:
                self.once = False  # 한 개체당 한 번씩만 관통 대미지를 받도록 한다.

            if self.weapon.weapon_type == 1 and not self.weapon.skill_enable:
                self.once = False

    def handle_events(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def get_bb(self):  # 각 몬스터마다 히트박스 크기가 다름
        if self.type == 1:
            return self.x + self.p.ex - 45, self.y + self.p.ey - 70, self.x + self.p.ex + 45, self.y + self.p.ey + 60
        elif self.type == 2:
            return self.x + self.p.ex - 50, self.y + self.p.ey - 55, self.x + self.p.ex + 45, self.y + self.p.ey + 55
        elif self.type == 3:
            return self.x + self.p.ex - 60, self.y + self.p.ey - 60, self.x + self.p.ex + 60, self.y + self.p.ey + 60
        elif self.type == 4:
            return self.x + self.p.ex - 45, self.y + self.p.ey - 55, self.x + self.p.ex + 45, self.y + self.p.ey + 45

    def handle_collision(self, group, other):
        if group == 'player:monster':  # 근접무기 스킬 사용 중에는 대미지를 받지 않는다.
            if not self.weapon.skill_enable:
                if self.type == 1:  # type1 접촉 시 이동 정지
                    self.is_attack = True

                if self.atk_delay <= 0 and not self.type == 4:  # 실질적인 공격, 원거리형 몬스터인 타입4는 근접 대미지가 없다.
                    self.attack_motion_time = 100
                    self.atk_delay = 200
                    self.size = 200

                    if self.p.dmg_delay <= 0:
                        match self.type:  # 몬스터마다 대미지가 다르다
                            case 1:
                                self.p.cur_hp -= 25
                            case 2:
                                self.p.cur_hp -= 15
                            case 3:
                                self.p.cur_hp -= 30

                        self.p.damage_sound.play()

                        self.p.dmg_shake_range = 30
                        self.p.dmg_delay = 200  # 해당 변수가 0이 되어야 플레이어는 다음 대미지를 받는다
                        pd = PlayerDamage()  # 대미지를 받으면 화면에 대미지 피드백을 표시한다
                        game_manager.add_object(pd, 7)

        if group == 'weapon:monster':  # 총이나 근접무기에 맞을 경우 대미지를 가한다
            if self.weapon.weapon_type == 1:  # katana, axe 스킬 공격의 경우 범위 내 중첩 대미지로 판정
                # AXE의 경우 스킬 사용 시 몬스터는 즉사한다
                if self.weapon.hit_ground and self.weapon.melee == 'AXE':
                    if not self.once and self.hp > 0:
                        self.hp -= 200
                        self.once = True

                elif self.weapon.skill_enable and self.weapon.melee == 'KATANA':
                    if not self.once and self.hp > 0:
                        self.hp -= 200
                        self.once = True

                else:  # 나머지 근접 무기 공격
                    if self.hp > 0 and not self.weapon.hit_once:
                        self.is_hit = True
                        self.weapon.hit_once = True

            elif self.weapon.weapon_type == 0:  # 여러개의 몬스터 히트박스가 중첩될경우 한 마리만 대미지를 가한다.
                if not self.weapon.hit_once and self.hp > 0:
                    self.is_hit = True  # 대미지를 가하지만
                    self.weapon.hit_once = True  # 한 마리에게만 가한다

        if group == 'bullet:monster':  # sr 계열 총기 관통 대미지
            # 대미지를 여러 번 받지 않게 끔 한다.
            if self.mp.playerToWallLeft <= self.x <= self.mp.playerToWallRight:
                if not self.once and self.hp > 0:
                    self.op = 1

                    if self.weapon.pen_enable:
                        fd = Feedback(self.x + self.p.cam_x, self.y + self.p.cam_y + self.p.cam_h, 1)
                        game_manager.add_object(fd, 7)  # 명중 피드백

                        if self.weapon.gun == 'SPRING':
                            self.hp -= 250 - 50 * self.weapon.pen_count  # 관통이 될 수록 대미지가 감소한다.
                            self.knockback_dir = self.dir
                            self.knockback = True
                            self.back_acc = 16 - (1 * self.weapon.pen_count)
                            self.weapon.pen_count += 1

                        elif self.weapon.gun == 'KAR98':
                            self.hp -= 250 - 40 * self.weapon.pen_count  # 관통이 될 수록 대미지가 감소한다.
                            self.knockback_dir = self.dir
                            self.knockback = True
                            self.back_acc = 16 - (1 * self.weapon.pen_count)
                            self.weapon.pen_count += 1

                        elif self.weapon.gun == 'M24':
                            self.hp -= 250 - 30 * self.weapon.pen_count  # 관통이 될 수록 대미지가 감소한다.
                            self.knockback_dir = self.dir
                            self.knockback = True
                            self.back_acc = 16 - (1 * self.weapon.pen_count)
                            self.weapon.pen_count += 1

                        elif self.weapon.gun == 'AWP':
                            self.hp -= 250 - 30 * self.weapon.pen_count  # 관통이 될 수록 대미지가 감소한다.
                            self.knockback_dir = self.dir
                            self.knockback = True
                            self.back_acc = 16 - (1 * self.weapon.pen_count)
                            self.weapon.pen_count += 1

                        elif self.weapon.gun == 'CHEYTAC':
                            self.hp -= 300 - 30 * self.weapon.pen_count  # 관통이 될 수록 대미지가 감소한다.
                            self.knockback_dir = self.dir
                            self.knockback = True
                            self.back_acc = 18 - (1 * self.weapon.pen_count)
                            self.weapon.pen_count += 1

                        if self.weapon.pen_count == self.weapon.pen_limit:  # 최대 관통 수를 초과하면 더 이상 초과하지 않는다.
                            self.weapon.pen_count = 0
                            self.weapon.pen_enable = False
                    self.once = True  # 이 변수가 true가 되면 더 이상 대미지가 중첩되지 않는다.

        if group == 'grenade:monster':
            # 수류탄 폭발에 맞으면 무조건 즉사
            if self.mp.playerToWallLeft <= self.x <= self.mp.playerToWallRight:
                self.ex_dead = True
