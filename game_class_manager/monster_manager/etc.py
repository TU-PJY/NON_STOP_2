import math

from config import *
from game_class.prop import Coin, Dead, Splash
from game_work import game_framework, game_manager


def monster_animation(m):
    pps = game_framework.pps
    if not m.is_attack and m.attack_motion_time <= 0 and not m.type == 3:  # type3은 프레임 업데이트를 하지 않음
        m.frame = (m.frame + APT * FPA * game_framework.frame_time) % 2

    # type 3 animation
    if m.type == 3:
        m.size_deg += 1 * pps / 80
        if not m.is_jump:
            m.size2 = math.sin(m.size_deg) / 6  # 위 아래로 rubber animation 출력
            m.frame = 0
        if m.is_jump:  # 점프 시 프레임이 다름
            m.frame = 1
            m.size2 = 0


def update_delay(m):  # 몬스터 관련 딜레이 업데이트
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


def update_monster_size(m):  # 몬스터 공격 피드백 관리
    pps = game_framework.pps
    if m.size > 0:
        m.size -= 2 * pps / 3


def update_monster_opacify(m):  # 몬스터 대미지 피드백 관리
    pps = game_framework.pps
    if m.op > 0:
        m.op -= int(4 * pps / 3)
        if m.op < 0:
            m.op = 0


def update_monster_pos(m):  # 화면 상의 몬스터 위치 업데이트
    speed = game_framework.pps * m.p.speed
    if m.p.mv_right:
        m.x -= speed
        if m.type == 2:
            m.temp_x -= speed

    elif m.p.mv_left:
        m.x += speed
        if m.type == 2:
            m.temp_x += speed


def add_object_after_dead(m):
    if m.type == 3:  # 슬라임의 경우 터지면서 죽는다
        splash = Splash(m.p, m.x, m.y)
        game_manager.add_object(splash, 4)

    if m.type == 1 or m.type == 4 or m.type == 2:  # 총기의 종류에 따라 밀려나는 정도가 다르다
        if not m.ex_dead:
            if m.weapon.weapon_type == 0:
                if m.weapon.gun_type == 'rifle':
                    dead = Dead(m.p, m.mp, m.x, m.y, m.dir, m.type, 1)
                elif m.weapon.gun_type == 'sr':
                    dead = Dead(m.p, m.mp, m.x, m.y, m.dir, m.type, 2)
                else:
                    dead = Dead(m.p, m.mp, m.x, m.y, m.dir, m.type)

            elif m.weapon.weapon_type == 1:
                if m.weapon.skill_enable:
                    if m.weapon.melee == 'KATANA' or m.weapon.melee == 'AXE':
                        dead = Dead(m.p, m.mp, m.x, m.y, m.dir, m.type, 4)
                    if m.weapon.melee == 'RAPIER':
                        dead = Dead(m.p, m.mp, m.x, m.y, m.dir, m.type, 1)
                else:
                    if m.weapon.melee == 'BAT' or m.weapon.melee == 'KATANA' or m.weapon.melee == 'AXE':
                        dead = Dead(m.p, m.mp, m.x, m.y, m.dir, m.type, 1)
                    else:
                        dead = Dead(m.p, m.mp, m.x, m.y, m.dir, m.type)

        elif m.ex_dead:
            if m.weapon.gren_x < m.x:
                dead = Dead(m.p, m.mp, m.x, m.y, 0, m.type, 3)
            elif m.x < m.weapon.gren_x:
                dead = Dead(m.p, m.mp, m.x, m.y, 1, m.type, 3)

    if m.weapon.melee == 'KATANA' or m.weapon.melee == 'AXE' and m.weapon.skill_enable and m.weapon.weapon_type == 1:
        coin = Coin(m.p, m.mp, m.x, m.y + 200, m.dir, 2)  # 카타나 스킬에 의해 죽은 경우 조금 더 높은 곳에 드랍
    elif m.ex_dead:
        coin = Coin(m.p, m.mp, m.x, m.y, m.dir, 3)  # 수튜탄에 죽는경우 코인이 날아간다
    else:
        coin = Coin(m.p, m.mp, m.x, m.y, m.dir)

    game_manager.add_object(dead, 3)  # 시체를 추가한다
    game_manager.add_object(coin, 3)  # 코인을 드랍한다
    game_manager.add_collision_pair('player:coin', None, coin)
    game_manager.remove_object(m)
