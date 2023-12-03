from game_class_manager.weapon_manager.etc import *
from game_class_manager.weapon_manager.file_loader import load_gun_image, load_melee_image, load_gun_sound, \
    load_melee_sound
from game_class_manager.weapon_manager.flame_output import draw_flame
from game_class_manager.weapon_manager.gun_output import draw_gun
from game_class_manager.weapon_manager.gun_shoot import shoot_gun
from game_class_manager.weapon_manager.melee_output import draw_melee
from game_class_manager.weapon_manager.melee_wield import wield_melee, melee_skill, update_melee_skill, \
    update_rapier_player, \
    set_skill, init_melee
from game_class_manager.weapon_manager.weapon_animation import spin_win, update_melee_position, swing
from game_work import game_framework


class Shoot:
    @staticmethod
    def enter(weapon, e):
        if weapon.weapon_type == 0:
            weapon.trigger = True
            if weapon.reload_need:
                check_ammo(weapon)  # 잔탄 체크 후 재장전 여부 결정
            if weapon.gun == 'WIN':  # 장전 도중 발사하면 재장전 상태 해제
                if weapon.reloading:
                    weapon.reloading = False
                    weapon.cur_reload_time = 0
                if weapon.reload_need and weapon.rifle_ammo > 0:
                    weapon.reloading = True

        elif weapon.weapon_type == 1 and not weapon.skill_enable:
            weapon.use = True

    @staticmethod
    def exit(weapon, e):
        weapon.trigger = False
        weapon.shoot = False
        weapon.use = False

        if weapon.gun_type == 'rifle' and not weapon.gun == 'WIN':
            weapon.shoot_delay = 0
        if weapon.gun_type == 'ar' and weapon.gun == 'MINI14':
            weapon.shoot_delay = 0

        if q_down(e):
            change_weapon(weapon)
            init_melee(weapon)
            weapon.cur_reload_time = 0  # 근접무기 전환 시 재장전이 취소된다
            weapon.reloading = False

        if r_down(e) and weapon.weapon_type == 0:
            if weapon.gun == 'sr':
                if not weapon.zoom:
                    weapon.zoom = True
                elif weapon.zoom:
                    weapon.zoom = False

        if r_down(e) and weapon.weapon_type == 1 and not weapon.skill_enable:
            set_skill(weapon)

        if weapon.weapon_type == 0:
            if weapon.limit_ammo - weapon.cur_ammo > 0:  # 탄창이 꽉 찬 상태에서는 재장전을 실행하지 않는다
                if reload_down(e) and not weapon.reloading:  # 재장전, 소유 탄약이 0인 상태에서는 재장전 하지 않는다
                    check_ammo(weapon)

        if shift_down(e) and weapon.throwable:
            throw_grenade(weapon)

    @staticmethod
    def do(weapon):
        update_delay(weapon)
        shoot_gun(weapon)
        wield_melee(weapon)
        if weapon.weapon_type == 0:
            update_sniper_bolt(weapon)
        if weapon.is_spin:
            spin_win(weapon)

        if weapon.reloading:
            if weapon.gun == 'WIN':
                reload_one(weapon)
            else:
                reload_gun(weapon)

        if weapon.swing:
            swing(weapon)

        if weapon.melee == 'RAPIER' and weapon.weapon_type == 1:
            update_rapier_player(weapon)

        if weapon.skill_enable:
            melee_skill(weapon)
            update_melee_skill(weapon)

        update_skill_delay(weapon)

        update_throw_delay(weapon)

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
            init_melee(weapon)
            weapon.cur_reload_time = 0
            weapon.reloading = False

        if r_down(e) and weapon.weapon_type == 0:
            if weapon.gun_type == 'sr':
                if not weapon.zoom:
                    weapon.zoom = True
                elif weapon.zoom:
                    weapon.zoom = False

        if r_down(e) and weapon.weapon_type == 1 and not weapon.skill_enable:
            set_skill(weapon)

        if weapon.weapon_type == 0:
            if weapon.limit_ammo - weapon.cur_ammo > 0:  # 탄창이 꽉 찬 상태에서는 재장전을 실행하지 않는다
                if reload_down(e) and not weapon.reloading:  # 재장전, 소유 탄약이 0인 상태에서는 재장전 하지 않는다
                    check_ammo(weapon)

        if shift_down(e) and weapon.throwable:
            throw_grenade(weapon)

    @staticmethod
    def do(weapon):
        update_delay(weapon)
        update_melee_position(weapon)
        if weapon.weapon_type == 0:
            update_sniper_bolt(weapon)
        if weapon.is_spin:
            spin_win(weapon)

        if weapon.reloading:
            if weapon.gun == 'WIN':
                reload_one(weapon)
            else:
                reload_gun(weapon)

        if weapon.swing:
            swing(weapon)

        if weapon.melee == 'RAPIER' and weapon.weapon_type == 1:
            update_rapier_player(weapon)

        if weapon.skill_enable:
            melee_skill(weapon)
            update_melee_skill(weapon)

        update_skill_delay(weapon)

        update_throw_delay(weapon)

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
            Idle: {l_down: Shoot, q_down: Idle, r_down: Idle, r_up: Idle, reload_down: Idle, shift_down: Idle},
            Shoot: {l_up: Idle, q_down: Idle, r_down: Shoot, r_up: Shoot, reload_down: Idle, shift_down: Shoot}
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
        load_gun_sound(self)
        load_melee_sound(self)
        self.p = p
        self.mp = mp

        self.weapon_type = 0  # 0: Gun, 1: Melee
        self.gun = 'M1911'
        self.prev_gun = 'M1911'
        self.deg = 0  # 총 이미지 각도
        self.flip = ''
        self.update_deg = True  # 이 변수가 false이면 총기 이미지 각도가 업데이트 되지 않는다

        self.trigger = False  # 마우스 좌클릭 시 True
        self.shoot = False  # True일시 격발
        self.shoot_delay = 0  # 0이 될때마다 self.shoot == True

        self.gun_type = 'pistol'  # 현재 총 타입
        self.prev_gun_type = 'pistol'  # 교체 전 이전 총 타입

        self.flame_display_time = 0  # 총구 화염 출력 시간

        self.melee = 'KNIFE'
        self.prev_melee = 'KNIFE'
        self.melee_x = 0
        self.melee_deg = 170
        self.use = False  # 무기 사용 상태
        self.wield = False  # 무기 공격 여부
        self.wield_delay = 0

        self.hit_once = False  # 겹쳐있는 몬스터에게 한꺼번에 대미지를 주지 않도록 한다.

        # sr 전용 변수
        self.zoom = False
        self.bolt_action = False  # 해당 변수가 true일 시 sr 정조준이 해제된다

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

        # bat 전용 변수
        self.swing = False
        self.swing_down, self.swing_up = False, False

        # rapier 전용 변수
        self.rapier_y = 0
        self.rapid_x = 0

        # 근접무기 특수 능력 변수
        self.skill_time = 0
        self.skill_enable = False
        self.hit_ground = False

        self.skill_delay_rapier = 0  # 근접무기 스킬 사용 딜레이
        self.skill_delay_katana = 0
        self.skill_delay_axe = 0

        self.skill_delay_time_rapier = 0  # ui 출력용 변수
        self.skill_delay_time_katana = 0
        self.skill_delay_time_axe = 0

        self.skill_temp_rapier = 0  # 모드 변경 시 쿨타임을 저장하기 위한 변수
        self.skill_temp_katana = 0
        self.skill_temp_axe = 0

        self.skill_usable_rapier = True  # True일 시 스킬 사용 가능
        self.skill_usable_katana = True
        self.skill_usable_axe = True

        # 수류탄 전용 변수
        self.throwable = True
        self.throw_delay = 0  # 수류탄 사용 간격
        self.throw_delay_time = 0  # ui에 쿨타임을 출력하기 위한 변수
        self.temp_time = 0  # 모드 전환 시 쿨타임을 저장하기 위한 임시 변수

        # 탄약 관련
        # 개발 중에는 99999로 초기화
        self.pistol_ammo = 100  # pistol, smg 탄종, 게임 시작 시 기본으로 100발이 주어짐
        self.ar_ammo = 0  # ar 탄종
        self.rifle_ammo = 0  # rifle 탄종
        self.sniper_ammo = 0  # sr 탄종

        self.cur_ammo = 7  # 현재 탄창에 있는 탄약 수, 기본 권총의 장탄 수 
        self.limit_ammo = 7  # 총기마다 다른 장탄수를 가진다.

        self.reload_need = False  # true일 시 발사 불가
        self.reload_time = 150  # 재장전 소요 시간
        self.cur_reload_time = 0  # 해당 값이 reload_time에 도달해야 재장전이 완료된다.

        self.reloading = False  # true일 시 재장전 중

        self.eq_page = 1  # 상점창에서 특정 페이지에서만 장착중인 아이템을 표시하도록 한다.

        # 구입 여부를 버튼의 가로세로 인덱스로 저장, 잠김 표시를 위함
        self.buy_list_gun = [[False for _ in range(4)] for _ in range(5)]  # 구입 여부를 저장한다, true면 구입, false면 구입 안 함
        self.buy_list_gun2 = [[False for _ in range(1)] for _ in range(5)]  # page2 전용 배열
        self.buy_list_melee = [[False for _ in range(1)] for _ in range(5)]  # 근접무기 구입 여부를 저장한다

        self.buy_list_gun[0][0] = True  # 기본무기는 처음부터 사용 가능
        self.buy_list_melee[0][0] = True

        self.equip_list_melee = [[False for _ in range(1)] for _ in range(5)]
        self.equip_list_melee[0][0] = True

        self.equip_list_gun1 = [[False for _ in range(4)] for _ in range(5)]  # 장착 중인 총기 강조 표시용 리스트
        self.equip_list_gun2 = [[False for _ in range(1)] for _ in range(5)]  # page2용
        self.equip_list_gun1[0][0] = True

        self.gren_x = 0  # 몬스터가 날아가는 방향을 정하기 위한 수류탄 위치 변수
        self.gren_level = 1  # 레벨이 오를수록 폭발 반경이 넓어진다 최대 3레벨 까지

        self.play_sound = True  # 재장전 사운드를 한 번만 플레이 하도록 한다

        self.shell_count = 0  # 이 숫자만큼 리볼버 재장전 시 탄피를 배출한다
        self.revolver_shell_out = False  # true일 동안만 탄피 생성
        self.out_delay = 0

        self.state_machine = StateMachineGun(self)
        self.state_machine.start()

    def draw(self):
        self.state_machine.draw()

    def update(self):
        if game_framework.MODE == 'play':
            self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))
