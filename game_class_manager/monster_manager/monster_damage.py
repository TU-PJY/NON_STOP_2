from game_class.prop import Bullet, Feedback
from game_class_manager.monster_manager.etc import add_object_after_dead
from game_work import game_manager
from mods import play_mode


def knockback_gun(m, gun):  # 총에 맞으면 살짝 뒤로 밀려난다
    back = 0
    match m.dir:
        case 1:
            back = -1
        case 0:
            back = 1

    match gun:
        case 'SCAR_H':
            if m.mp.playerToWallLeft < m.x < m.mp.playerToWallRight:
                m.x += 20 * back
        case 'M16':
            if m.mp.playerToWallLeft < m.x < m.mp.playerToWallRight:
                m.x += 15 * back
        case 'MP44':
            m.knockback = True
            m.knockback_dir = m.dir
            m.back_acc = 4
        case 'AUG':
            if m.mp.playerToWallLeft < m.x < m.mp.playerToWallRight:
                m.x += 20 * back
        case 'GROZA':
            if m.mp.playerToWallLeft < m.x < m.mp.playerToWallRight:
                m.x += 10 * back
        case 'M1':
            m.knockback = True
            m.knockback_dir = m.dir
            m.back_acc = 7
        case 'WIN':
            m.knockback = True
            m.knockback_dir = m.dir
            m.back_acc = 9
        case 'MINI14':
            m.knockback = True
            m.knockback_dir = m.dir
            m.back_acc = 5
        case 'FAL':
            m.knockback = True
            m.knockback_dir = m.dir
            m.back_acc = 7
        case 'LVOAS':
            m.knockback = True
            m.knockback_dir = m.dir
            m.back_acc = 5


def knockback_melee(m, melee):
    match melee:
        case 'KNIFE':
            m.back_acc = 4
        case 'BAT':
            m.back_acc = 6
        case 'RAPIER':
            m.back_acc = 3
        case 'KATANA':
            m.back_acc = 8
        case 'AXE':
            m.back_acc = 10

    m.knockback = True
    m.knockback_dir = m.dir


def damage_monster(m):  # 맵 안에서만 대미지를 받는다
    if m.mp.playerToWallLeft <= m.p.x <= m.mp.playerToWallRight:
        if m.weapon.shoot:
            if m.is_hit:  # 맞은걸로 판정되면 대미지를 가한다.
                if m.weapon.gun == 'M1911':
                    m.hp -= 30
                elif m.weapon.gun == 'M92':
                    m.hp -= 25
                elif m.weapon.gun == 'DEGLE':
                    m.hp -= 40
                elif m.weapon.gun == 'M500':
                    m.hp -= 60
                elif m.weapon.gun == 'QHAND':
                    m.hp -= 25

                elif m.weapon.gun == 'AKS74':
                    m.hp -= 17
                elif m.weapon.gun == 'UMP':
                    m.hp -= 20
                elif m.weapon.gun == 'VECTOR':
                    m.hp -= 13
                elif m.weapon.gun == 'THOMPSON':
                    m.hp -= 20
                elif m.weapon.gun == 'P90':
                    m.hp -= 17

                elif m.weapon.gun == 'SCAR_H':
                    m.hp -= 22
                elif m.weapon.gun == 'M16':
                    m.hp -= 20
                elif m.weapon.gun == 'MP44':
                    m.hp -= 40
                elif m.weapon.gun == 'AUG':
                    m.hp -= 23
                elif m.weapon.gun == 'GROZA':
                    m.hp -= 21

                elif m.weapon.gun == 'M1':
                    m.hp -= 80
                elif m.weapon.gun == 'WIN':
                    m.hp -= 180
                elif m.weapon.gun == 'MINI14':
                    m.hp -= 55
                elif m.weapon.gun == 'FAL':
                    m.hp -= 80
                elif m.weapon.gun == 'LVOAS':
                    m.hp -= 55

                elif m.weapon.gun_type == 'sr':
                    # 관통을 위한 가상 객체 생성
                    bullet = Bullet \
                        (m.weapon, m.p, m.mp, m.target.tx - m.p.ex, m.target.ty - m.p.ey, m.weapon.deg, 'None')
                    game_manager.add_object(bullet, 3)
                    game_manager.add_collision_pair('bullet:monster', bullet, None)
                    m.weapon.pen_enable = True  # 해당 변수가 활성화 되어야 관통이 된다.

                if m.hp > 0:
                    knockback_gun(m, m.weapon.gun)

                m.op = 1  # 몬스터가 빨갛게 변하며 대미지를 입었다는 피드백을 전달
                m.is_hit = False  # 다시 대미지를 받을 준비를 한다
                m.weapon.hit_once = False

                if not m.weapon.gun_type == 'sr':
                    fd = Feedback(m.target.tx, m.target.ty, 1)
                    game_manager.add_object(fd, 7)

        elif m.weapon.wield:  # 근접무기
            if m.is_hit:
                if m.weapon.melee == 'KNIFE':
                    m.p.shake_range = 30
                    m.weapon.melee_hit.play()
                    m.hp -= 60
                elif m.weapon.melee == 'BAT':
                    m.p.shake_range = 40
                    m.weapon.melee_hit2.play()
                    m.hp -= 120
                elif m.weapon.melee == 'RAPIER':
                    m.p.shake_range = 30
                    m.weapon.melee_hit.play()
                    m.hp -= 30
                elif m.weapon.melee == 'KATANA':
                    m.p.shake_range = 40
                    m.weapon.melee_hit.play()
                    m.hp -= 120
                elif m.weapon.melee == 'AXE':
                    m.p.shake_range = 40
                    m.weapon.melee_hit2.play()
                    m.hp -= 180

                if m.hp > 0:
                    knockback_melee(m, m.weapon.melee)

                m.op = 1  # 몬스터가 빨갛게 변하며 대미지를 입었다는 피드백을 전달
                m.is_hit = False
                m.weapon.hit_once = False

                fd = Feedback(m.x + m.p.ex, m.y + m.p.ey, 2)
                game_manager.add_object(fd, 7)

        elif m.ex_dead:  # 수류탄 폭발 대미지
            m.hp -= 500

    if m.hp <= 0:  # hp가 0이 될 경우 죽는다.
        add_object_after_dead(m)
