from pico2d import *

from config import *
from game_class.prop import Arrow
from game_work import game_manager, game_framework


def calc_pps():
    global pps 
    pps = PPS * game_framework.frame_time


def load_monster(self):
    if self.type == 1:
        self.type1 = load_image(type1_directory)
        self.type1_damage = load_image(type1_damage_directory)
    elif self.type == 2:
        self.type2 = load_image(type2_directory)
        self.type2_damage = load_image(type2_damage_directory)
    elif self.type == 3:
        self.type3 = load_image(type3_directory)
        self.type3_damage = load_image(type3_damage_directory)
    elif self.type == 4:
        self.type4 = load_image(type4_directory)
        self.type4_damage = load_image(type4_damage_directory)

    # 체력바 이미지
    self.hp_back = load_image(hp_back_directory)
    self.hp_front = load_image(hp_front_directory)


def draw_monster(m):
    m.hp_back.draw(m.x + m.p.efx, m.y + 100 + m.p.efy, m.hp_length + 10, 25)
    m.hp_front.draw(m.x + m.p.efx - ((m.hp_length - m.hp) / 2), m.y + 100 + m.p.efy, m.hp, 20)

    if m.dir == 0:  # 보는 방향에 따라 이미지 방향이 달라진다
        m.flip = ''
    elif m.dir == 1:
        m.flip = 'h'

    if m.type == 1:
        m.type1_damage.opacify(int(m.op))
        m.type1.clip_composite_draw \
            (int(m.frame) * 64, 0, 64, 64, 0, m.flip, m.x + m.p.efx, m.y + m.p.efy + m.size / 6, 280, 280 + m.size)
        m.type1_damage.clip_composite_draw \
            (int(m.frame) * 64, 0, 64, 64, 0, m.flip, m.x + m.p.efx, m.y + m.p.efy + m.size / 6, 280, 280 + m.size)

        draw_rectangle \
            (m.x - 50 + m.p.efx, m.y + 50 + m.p.efy, m.x + 50 + m.p.efx, m.y - 70 + m.p.efy)

    if m.type == 2:
        m.type2_damage.opacify(int(m.op))
        m.type2.clip_composite_draw \
            (int(m.frame) * 128, 0, 128, 128, 0, m.flip, m.x + m.p.efx, m.y + m.p.efy + m.size / 2, 400, 400 + m.size)
        m.type2_damage.clip_composite_draw \
            (int(m.frame) * 128, 0, 128, 128, 0, m.flip, m.x + m.p.efx, m.y + m.p.efy + m.size / 2, 400, 400 + m.size)

        draw_rectangle \
            (m.x - 65 + m.p.efx, m.y + 65 + m.p.efy, m.x + 65 + m.p.efx, m.y - 65 + m.p.efy)

    if m.type == 3:
        m.type3_damage.opacify(int(m.op))
        m.type3.clip_composite_draw \
            (int(m.frame) * 128, 0, 128, 128, 0, m.flip, m.x + m.p.efx, m.y + m.p.efy + m.size2 * 50 + m.size / 5,
             300, 300 + m.size2 * 100 + m.size)
        m.type3_damage.clip_composite_draw \
            (int(m.frame) * 128, 0, 128, 128, 0, m.flip, m.x + m.p.efx, m.y + m.p.efy + m.size2 * 50 + m.size / 5,
             300, 300 + m.size2 * 100 + m.size)

        draw_rectangle \
            (m.x - 60 + m.p.efx, m.y + 60 + m.p.efy, m.x + 60 + m.p.efx, m.y - 60 + m.p.efy)

    if m.type == 4:
        m.type4_damage.opacify(int(m.op))
        m.type4.clip_composite_draw \
            (int(m.frame) * 128, 0, 128, 128, 0, m.flip, m.x + m.p.efx, m.y + m.p.efy, 450, 450)
        m.type4_damage.clip_composite_draw \
            (int(m.frame) * 128, 0, 128, 128, 0, m.flip, m.x + m.p.efx, m.y + m.p.efy, 450, 450)

        draw_rectangle \
            (m.x - 55 + m.p.efx, m.y + 55 + m.p.efy, m.x + 55 + m.p.efx, m.y - 55 + m.p.efy)


def update_monster_size(m):
    global pps
    if m.size > 0:
        m.size -= 2 * pps / 3


def update_monster_opacify(m):
    global pps 
    if m.op > 0:
        m.op -= 4 * pps / 3
        if m.op < 0:
            m.op = 0
    

def move_monster(m):
    global pps
    m.dir = 1 if m.p.x > m.x else 0

    if not m.is_attack and m.attack_motion_time <= 0:
        if not m.p.x - 5 <= m.x <= m.p.x + 5:
            if m.dir == 0:
                m.x -= m.speed * pps / 4
            elif m.dir == 1:
                m.x += m.speed * pps / 4

        if m.type == 2: 
            if m.y < 670:  # 670보다 낮게 있으면 자기 자리로 복귀한다
                m.y += pps / 4
                if m.y >= 670:
                    m.y = 670
            elif m.y > 670: # 670보다 높게 있으면 자기 자리로 복귀한다
                m.y -= pps / 4
                if m.y <= 670:
                    m.y = 670

        if m.type == 3:
            if not m.is_jump and m.jump_delay <= 0:  # 점프하면서 이동
                m.jump_acc = JUMP_ACC
                m.is_jump = True

            if m.is_jump:
                m.y += m.jump_acc * pps / 2.5

                if m.y <= 230 and m.jump_acc < 0:  # 땅에 착지할 경우
                    m.y = 230
                    m.is_jump = False
                    m.acc_delay = 0
                    m.jump_delay = 330  # 점프 타이밍이 존재

                m.jump_acc -= pps / 90


def monster_animation(m):
    global pps
    # all type animation except type 3
    if not m.is_attack and m.attack_motion_time <= 0 and not m.type == 3:  # type3은 프레임 업데이트를 하지 않음
        m.frame = (m.frame + APT * FPA * game_framework.frame_time) % 2

    # type 3 animation
    if m.type == 3:
        m.size_deg += 1 * pps / 80
        if not m.is_jump:
            m.size2 = math.sin(m.size_deg) / 6
            m.frame = 0

        if m.is_jump:  # 점프 시 프레임이 다름
            m.frame = 1
            m.size2 = 0


def process_attack(m):
    global pps
    # type 1 attack
    if m.type == 1:
        m.is_attack = True if math.sqrt((m.x - m.p.x) ** 2 + (m.p.y - m.y + (m.p.y - 250) / 1.5) ** 2) <= 100 else False
        if m.is_attack:
            if m.atk_delay <= 0:
                m.attack_motion_time = 50
                m.atk_delay = 200
                m.size = 200

            if m.attack_motion_time > 0:
                m.frame = 2
            else:
                m.frame = 1

    # type 2 attack
    if m.type == 2:
        if math.sqrt((m.p.x - m.x) ** 2 + (m.p.y - m.y + (m.p.y - 250) / 1.5) ** 2) <= 110 and not m.is_dash:  # 접촉
            if m.atk_delay <= 0:
                m.size = 200
                m.atk_delay = 200

        if m.mp.playerToWallLeft + 100 < m.x < m.mp.playerToWallRight - 100:  # 스폰 지점에서 바로 대쉬하지 않도록
            if m.dash_delay <= 0:
                if math.sqrt((m.x - m.p.x) ** 2 + (
                        m.p.y - m.y + (m.p.y - 250) / 1.5) ** 2) <= 800 and not m.is_attack and m.atk_delay <= 0:
                    m.incline = math.atan2(m.p.y - m.y + (m.p.y - 250) / 1.5, m.p.x - m.x)
                    m.temp_x, m.temp_y = m.p.x, m.p.y + (m.p.y - 250) / 1.5
                    m.is_dash = True
                    m.is_attack = True

        if m.is_dash:  # True일 시 대쉬 공격
            m.frame = 3
            m.x += 7 * math.cos(m.incline) * pps / 4
            m.y += 7 * math.sin(m.incline) * pps / 4

            if math.sqrt((m.p.x - m.x) ** 2 + (m.p.y - m.y + (m.p.y - 250) / 1.5) ** 2) <= 100:  # 대쉬 접촉
                m.size = 200

            if m.temp_x - 10 <= m.x <= m.temp_x + 10 and m.temp_y - 10 <= m.y <= m.temp_y + 10:
                m.dash_delay = 650
                m.is_dash = False
                m.is_attack = False

    # type 3 attack
    if m.type == 3:
        if math.sqrt((m.p.x - m.x) ** 2 + (m.p.y - m.y + (m.p.y - 250) / 1.5) ** 2) <= 110:
            if m.atk_delay <= 0:
                m.size = 200
                m.atk_delay = 200

    # type 4 attack
    if m.type == 4:
        if m.mp.playerToWallLeft + 100 <= m.x <= m.mp.playerToWallRight - 100:
            if math.sqrt((m.p.x - m.x) ** 2 + (m.p.y - m.y + (m.p.y - 250) / 1.5) ** 2) <= 800:
                m.is_attack = True
            else:
                m.is_attack = False
                m.shoot_delay = 150

            if m.is_attack:
                m.incline = math.atan2(m.p.y - m.y + (m.p.y - 250) / 1.5 + 50, m.p.x - m.x)
                m.frame = 2
                if m.shoot_delay <= 0:
                    ar = Arrow(m.p, m.mp, m.x, m.y, m.incline, m.dir)  # 일정 간격으로 화살을 발사한다
                    game_manager.add_object(ar, 2)
                    m.shoot_delay = 450


def damage_monster(m):
    if m.weapon.shoot and m.mp.playerToWallLeft - 50 <= m.p.x <= m.mp.playerToWallRight + 50:
        m.dispx = m.x + m.p.efx  # 화면 상에 실제로 보이는 위치
        m.dispy = m.y + m.p.efy

        if m.type == 1:  # 몬스터가 총에 맞았는지 판정한다.
            m.hit = True if m.dispx - 50 <= m.target.tx <= m.dispx + 50 and \
                            m.dispy - 70 <= m.target.ty <= m.dispy + 50 else False
        elif m.type == 2:
            m.hit = True if m.dispx - 65 <= m.target.tx <= m.dispx + 65 and \
                            m.dispy - 65 <= m.target.ty <= m.dispy + 65 else False
        elif m.type == 3:
            m.hit = True if m.dispx - 60 <= m.target.tx <= m.dispx + 60 and \
                            m.dispy - 60 <= m.target.ty <= m.dispy + 60 else False
        elif m.type == 4:
            m.hit = True if m.dispx - 55 <= m.target.tx <= m.dispx + 55 and \
                            m.dispy - 55 <= m.target.ty <= m.dispy + 55 else False

        if m.hit:  # 맞은걸로 판정되면 대미지를 가한다.
            if m.weapon.gun == 'AKS74':
                m.hp -= 12
            elif m.weapon.gun == 'UMP':
                m.hp -= 18
            elif m.weapon.gun == 'VECTOR':
                m.hp -= 12
            elif m.weapon.gun == 'THOMPSON':
                m.hp -= 20
            elif m.weapon.gun == 'P90':
                m.hp -= 17

            elif m.weapon.gun == 'SCAR_H':
                m.hp -= 22
            elif m.weapon.gun == 'M16':
                m.hp -= 18
            elif m.weapon.gun == 'MP44':
                m.hp -= 40
            elif m.weapon.gun == 'AUG':
                m.hp -= 23
            elif m.weapon.gun == 'GROZA':
                m.hp -= 20
            
            elif m.weapon.gun == 'M1':
                m.hp -= 60

            m.op = 100  # 몬스터가 빨갛게 변하며 대미지를 입었다는 피드백을 전달 
            m.hit = False

    elif m.weapon.wield:
        x1 = m.p.x              # dir == 1일 때의 좌측 x 좌표
        x22 = m.p.x             # dir == 0일 때의 우측 x 좌표
        my = m.y - (m.p.y - 250) / 1.5  # 화면상에 보이는 몬스터 중심 y 좌표
        py = m.p.y - 10         # 무기의 y 좌표

        # 각 근접무기마다 사거리가 다르다
        if m.weapon.melee == 'KNIFE':  # 50 + 근접무기 최대 사거리
            x2 = m.p.x + 220   # dir == 1일 때의 우측 x 좌표
            x11 = m.p.x - 220  # dir == 0일 때의 좌측 x 좌표

        if m.type == 1:  # 몬스터가 근접무기에 맞았는지 판정한다.
            if m.p.dir == 1:
                m.hit = True if x1 <= m.x - 50 <= x2 and my - 70 <= py <= my + 50 else False
            elif m.p.dir == 0:
                m.hit = True if x11 <= m.x + 50 <= x22 and my - 70 <= py <= my + 50 else False

        elif m.type == 2:
            if m.p.dir == 1:
                m.hit = True if x1 <= m.x - 65 <= x2 and my - 65 <= py <= my + 65 else False
            elif m.p.dir == 0:
                m.hit = True if x11 <= m.x + 65 <= x22 and my - 65 / 1.5 <= py <= my + 65 else False

        elif m.type == 3:
            if m.p.dir == 1:
                m.hit = True if x1 <= m.x - 60 <= x2 and my - 60 / 1.5 <= py <= my + 60 else False
            elif m.p.dir == 0:
                m.hit = True if x11 <= m.x + 60 <= x22 and my - 60 <= py <= my + 60 else False

        elif m.type == 4:
            if m.p.dir == 1:
                m.hit = True if x1 <= m.x - 55 <= x2 and my - 55 <= py <= my + 55 else False
            elif m.p.dir == 0:
                m.hit = True if x11 <= m.x + 55 <= x22 and my - 55 <= py <= my + 55 else False

        if m.hit:
            # bm = BloodMelee(m.x, m.p.y + (m.p.y - 250) / 1.5, m.dir, m.p)
            # game_manager.add_object(bm, 2)

            if m.weapon.melee == 'KNIFE':
                m.hp -= 60

            m.op = 100  # 몬스터가 빨갛게 변하며 대미지를 입었다는 피드백을 전달 
            m.hit = False

    if m.hp <= 0:  # hp가 0이 될 경우 죽는다.
        game_manager.remove_object(m)


def update_delay(m):
    global pps
    if m.attack_motion_time > 0:
        m.attack_motion_time -= pps / 3
    if m.atk_delay > 0:
        m.atk_delay -= pps / 3
    if m.dash_delay > 0:
        m.dash_delay -= pps / 3
    if m.shoot_delay > 0:
        m.shoot_delay -= pps / 3
    if m.jump_delay > 0:
        m.jump_delay -= pps / 3


def update_monster_pos(m):
    global pps
    if m.p.mv_right:
        m.x -= m.p.speed * pps / 4
        m.temp_x -= m.p.speed * pps / 4
    elif m.p.mv_left:
        m.x += m.p.speed * pps / 4
        m.temp_x += m.p.speed * pps / 4
