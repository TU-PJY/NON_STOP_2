from game_class.prop import Bullet, Feedback, Coin, Splash, Dead
from game_class_manager.monster_manager.etc import add_object_after_dead
from game_work import game_manager
from mods import play_mode


def damage_monster(m):  # 맵 안에서만 대미지를 받는다
    if m.mp.playerToWallLeft - 30 <= m.p.x <= m.mp.playerToWallRight + 30:
        if m.weapon.shoot:
            if m.is_hit:  # 맞은걸로 판정되면 대미지를 가한다.
                if m.weapon.gun == 'M1911':
                    m.hp -= 30
                elif m.weapon.gun == 'M92':
                    m.hp -= 30
                elif m.weapon.gun == 'DEGLE':
                    m.hp -= 45
                elif m.weapon.gun == 'M500':
                    m.hp -= 50
                elif m.weapon.gun == 'QHAND':
                    m.hp -= 25

                elif m.weapon.gun == 'AKS74':
                    m.hp -= 17
                elif m.weapon.gun == 'UMP':
                    m.hp -= 20
                elif m.weapon.gun == 'VECTOR':
                    m.hp -= 11
                elif m.weapon.gun == 'THOMPSON':
                    m.hp -= 20
                elif m.weapon.gun == 'P90':
                    m.hp -= 16

                elif m.weapon.gun == 'SCAR_H':
                    m.hp -= 28
                elif m.weapon.gun == 'M16':
                    m.hp -= 18
                elif m.weapon.gun == 'MP44':
                    m.hp -= 35
                elif m.weapon.gun == 'AUG':
                    m.hp -= 25
                elif m.weapon.gun == 'GROZA':
                    m.hp -= 23

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
                    bullet = Bullet \
                        (m.weapon, m.p, m.mp, m.target.tx - m.p.ex, m.target.ty - m.p.ey, m.weapon.deg, 'None')
                    game_manager.add_object(bullet, 3)
                    game_manager.add_collision_pair('bullet:monster', bullet, None)
                    m.weapon.pen_enable = True  # 해당 변수가 활성화 되어야 관통이 된다.

                m.op = 100  # 몬스터가 빨갛게 변하며 대미지를 입었다는 피드백을 전달
                m.is_hit = False  # 다시 대미지를 받을 준비를 한다
                m.weapon.hit_once = False

                if not m.weapon.gun_type == 'sr':
                    fd = Feedback(m.target.tx, m.target.ty)
                    game_manager.add_object(fd, 7)

        elif m.weapon.wield:  # 근접무기
            if m.is_hit:
                if m.weapon.melee == 'KNIFE':
                    m.hp -= 60
                elif m.weapon.melee == 'BAT':
                    m.hp -= 120
                elif m.weapon.melee == 'RAPIER':
                    m.hp -= 30
                elif m.weapon.melee == 'KATANA':
                    m.hp -= 100
                elif m.weapon.melee == 'AXE':
                    m.hp -= 150

                m.op = 100  # 몬스터가 빨갛게 변하며 대미지를 입었다는 피드백을 전달
                m.is_hit = False
                m.weapon.hit_once = False

        elif m.ex_dead:  # 수류탄 폭발 대미지
            m.hp -= 500

    if m.hp <= 0:  # hp가 0이 될 경우 죽는다.
        play_mode.tool.spawn_num -= 1  # 스폰된 몬스터 수 감소
        play_mode.tool.kill_count -= 1  # 킬 카운드 감소
        play_mode.ig.ky = 70  # 킬 피드백 재생
        add_object_after_dead(m)

