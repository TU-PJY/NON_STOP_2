from pico2d import *

from config import *
from game_class.prop import Arrow, Bullet, Feedback
from game_work import game_manager, game_framework


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
    x = m.x + m.p.ex
    y = m.y + m.p.ey
    m.hp_back.draw(x, y + 100, 210, 25)  # 체력 바
    m.hp_front.draw(x - 100 + (200 * m.hp / m.hp_length) / 2, y + 100, 200 * m.hp / m.hp_length, 20)

    m.flip = '' if m.dir == 0 else 'h'  # 보는 방향에 따라 이미지 방향이 바뀐다.

    if m.type == 1:
        m.type1_damage.opacify(int(m.op))
        m.type1.clip_composite_draw \
            (int(m.frame) * 64, 0, 64, 64, 0, m.flip, x, y + m.size / 6, 280, 280 + m.size)
        m.type1_damage.clip_composite_draw \
            (int(m.frame) * 64, 0, 64, 64, 0, m.flip, x, y + m.size / 6, 280, 280 + m.size)

    if m.type == 2:
        m.type2_damage.opacify(int(m.op))
        m.type2.clip_composite_draw \
            (int(m.frame) * 128, 0, 128, 128, 0, m.flip, x, y, 400, 400 + m.size)
        m.type2_damage.clip_composite_draw \
            (int(m.frame) * 128, 0, 128, 128, 0, m.flip, x, y, 400, 400 + m.size)

    if m.type == 3:
        m.type3_damage.opacify(int(m.op))
        m.type3.clip_composite_draw \
            (int(m.frame) * 128, 0, 128, 128, 0, m.flip, x, y + m.size2 * 50 + m.size / 5,
             300, 300 + m.size2 * 100 + m.size)
        m.type3_damage.clip_composite_draw \
            (int(m.frame) * 128, 0, 128, 128, 0, m.flip, x, y + m.size2 * 50 + m.size / 5,
             300, 300 + m.size2 * 100 + m.size)

    if m.type == 4:
        m.type4_damage.opacify(int(m.op))
        m.type4.clip_composite_draw \
            (int(m.frame) * 128, 0, 128, 128, 0, m.flip, x, y, 450, 450)
        m.type4_damage.clip_composite_draw \
            (int(m.frame) * 128, 0, 128, 128, 0, m.flip, x, y, 450, 450)


def move_monster(m):
    pps = game_framework.pps
    m.dir = 1 if m.p.x > m.x else 0

    if not m.is_attack and m.attack_motion_time <= 0:
        if not m.p.x - 5 <= m.x <= m.p.x + 5:  # 몬스터 제자리 와리가리 방지
            if m.dir == 0:
                m.x -= m.speed * pps / 4
            elif m.dir == 1:
                m.x += m.speed * pps / 4

    if m.type == 2 and not m.is_dash:
        if m.y < 670:  # 670보다 낮게 있으면 자기 자리로 복귀한다
            m.y += 2 * pps / 4
            if m.y >= 670:
                m.y = 670
        elif m.y > 670:  # 670보다 높게 있으면 자기 자리로 복귀한다
            m.y -= 2 * pps / 4
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
                m.jump_delay = 330  # 점프 타이밍이 존재

            m.jump_acc -= pps / 90


# cam_h는 플레이어와 상대적 위치 차이를 발생시키기 때문에 몬스터 y위치에 cam_h를 포함해줘야함
def process_attack(m):
    pps = game_framework.pps
    # type 1 attack
    if m.type == 1:
        if m.is_attack:
            if m.attack_motion_time > 0:
                m.frame = 2
            else:
                m.frame = 1
                m.is_attack = False

    # type 2 attack
    if m.type == 2:
        if m.mp.playerToWallLeft - 50 < m.x < m.mp.playerToWallRight + 50:  # 스폰 지점에서 바로 대쉬하지 않도록
            if m.dash_delay <= 0 and not m.is_attack and m.atk_delay <= 0:
                if math.sqrt((m.x - m.p.x) ** 2 + ((m.y + m.p.cam_h) - m.p.y) ** 2) <= 600:
                    m.incline = math.atan2(m.p.y - (m.y + m.p.cam_h), m.p.x - m.x)
                    m.temp_x, m.temp_y = m.p.x, m.p.y - m.p.cam_h
                    m.is_dash = True
                    m.is_attack = True

        if m.is_dash:  # True일 시 대쉬 공격
            m.frame = 3
            m.x += 7 * math.cos(m.incline) * pps / 4
            m.y += 7 * math.sin(m.incline) * pps / 4

            if m.temp_x - 10 <= m.x <= m.temp_x + 10 and m.temp_y - 10 <= m.y <= m.temp_y + 10:
                m.dash_delay = 700
                m.is_dash = False
                m.is_attack = False

    # type 3 attack
    if m.type == 3:
        pass

    # type 4 attack
    if m.type == 4:
        if m.mp.playerToWallLeft + 100 <= m.x <= m.mp.playerToWallRight - 100:
            if math.sqrt((m.p.x - m.x) ** 2 + (m.p.y - (m.y + m.p.cam_h)) ** 2) <= 750:
                m.is_attack = True
            else:
                m.is_attack = False
                m.shoot_delay = 150

            if m.is_attack:
                m.incline = math.atan2(m.p.y + 70 - (m.y + m.p.cam_h), m.p.x - m.x)  # 머리쪽으로 살짝 높혀서 쏜다
                m.frame = 2
                if m.shoot_delay <= 0:
                    ar = Arrow(m.p, m.mp, m.x, m.y, m.incline, m.dir)  # 일정 간격으로 화살을 발사한다
                    game_manager.add_object(ar, 2)
                    m.shoot_delay = 450


def damage_monster(m):
    if m.weapon.shoot and m.mp.playerToWallLeft - 30 <= m.p.x <= m.mp.playerToWallRight + 30:
        if m.is_hit:  # 맞은걸로 판정되면 대미지를 가한다.
            if m.weapon.gun == 'M1911':
                m.hp -= 25
            elif m.weapon.gun == 'M92':
                m.hp -= 23
            elif m.weapon.gun == 'DEGLE':
                m.hp -= 35
            elif m.weapon.gun == 'M500':
                m.hp -= 40
            elif m.weapon.gun == 'QHAND':
                m.hp -= 20

            elif m.weapon.gun == 'AKS74':
                m.hp -= 12
            elif m.weapon.gun == 'UMP':
                m.hp -= 15
            elif m.weapon.gun == 'VECTOR':
                m.hp -= 12
            elif m.weapon.gun == 'THOMPSON':
                m.hp -= 18
            elif m.weapon.gun == 'P90':
                m.hp -= 15

            elif m.weapon.gun == 'SCAR_H':
                m.hp -= 20
            elif m.weapon.gun == 'M16':
                m.hp -= 18
            elif m.weapon.gun == 'MP44':
                m.hp -= 30
            elif m.weapon.gun == 'AUG':
                m.hp -= 21
            elif m.weapon.gun == 'GROZA':
                m.hp -= 20

            elif m.weapon.gun == 'M1':
                m.hp -= 70
            elif m.weapon.gun == 'WIN':
                m.hp -= 100
            elif m.weapon.gun == 'MINI14':
                m.hp -= 50
            elif m.weapon.gun == 'FAL':
                m.hp -= 70
            elif m.weapon.gun == 'LVOAS':
                m.hp -= 40

            elif m.weapon.gun_type == 'sr':
                # 관통을 위한 가상 객체 생성
                bullet = Bullet(m.weapon, m.p, m.mp, m.target.tx - m.p.ex, m.target.ty - m.p.ey, m.weapon.deg, 'AWP')
                game_manager.add_object(bullet, 3)
                game_manager.add_collision_pair('bullet:monster', bullet, None)
                m.weapon.pen_enable = True  # 해당 변수가 활성화 되어야 관통이 된다.

            m.op = 100  # 몬스터가 빨갛게 변하며 대미지를 입었다는 피드백을 전달
            m.is_hit = False
            m.weapon.hit_once = False

            if not m.weapon.gun_type == 'sr':
                fd = Feedback(m.target.tx, m.target.ty)
                game_manager.add_object(fd, 7)

    elif m.weapon.wield:
        if m.is_hit:
            if m.weapon.melee == 'KNIFE':
                m.hp -= 60

            elif m.weapon.melee == 'BAT':
                m.hp -= 120

            elif m.weapon.melee == 'RAPIER':
                m.hp -= 30

            elif m.weapon.melee == 'KATANA':
                m.hp -= 100

            m.op = 100  # 몬스터가 빨갛게 변하며 대미지를 입었다는 피드백을 전달
            m.is_hit = False
            m.weapon.hit_once = False

    if m.hp <= 0:  # hp가 0이 될 경우 죽는다.
        game_manager.remove_object(m)


def monster_animation(m):
    pps = game_framework.pps
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


def update_delay(m):
    pps = game_framework.pps
    if m.attack_motion_time > 0:
        m.attack_motion_time -= pps / 3
    if m.atk_delay > 0:
        m.atk_delay -= pps / 3
    if m.type == 2 and m.dash_delay > 0:
        m.dash_delay -= pps / 3
    if m.type == 4 and m.shoot_delay > 0:
        m.shoot_delay -= pps / 3
    if m.type == 3 and m.jump_delay > 0:
        m.jump_delay -= pps / 3


def update_monster_size(m):
    pps = game_framework.pps
    if m.size > 0:
        m.size -= 2 * pps / 3


def update_monster_opacify(m):
    pps = game_framework.pps
    if m.op > 0:
        m.op -= int(4 * pps / 3)
        if m.op < 0:
            m.op = 0


def update_monster_pos(m):
    pps = game_framework.pps
    if m.p.mv_right:
        m.x -= m.p.speed * pps / 4
        if m.type == 2:
            m.temp_x -= m.p.speed * pps / 4

    elif m.p.mv_left:
        m.x += m.p.speed * pps / 4
        if m.type == 2:
            m.temp_x += m.p.speed * pps / 4
