# 총열 길이가 총마다 다르므로 불꽃 위치도 다르다
import math

from game_work import game_framework


def draw_flame(weapon):
    pps = game_framework.pps
    if weapon.flame_display_time > 0 and weapon.weapon_type == 0:
        weapon.flame_display_time -= pps / 3
        if weapon.gun == 'M1':
            x = weapon.p.wx + math.cos(weapon.deg) * 200
            y = weapon.p.wy + 5 + math.sin(weapon.deg) * 200

        elif weapon.gun == 'FAL' or weapon.gun == 'LVOAS':
            x = weapon.p.wx + math.cos(weapon.deg) * 200
            y = weapon.p.wy + math.sin(weapon.deg) * 200

        elif weapon.gun == 'WIN' or weapon.gun == 'AWP':
            x = weapon.p.wx + math.cos(weapon.deg) * 230
            y = weapon.p.wy + math.sin(weapon.deg) * 230

        elif weapon.gun == 'AKS74' or weapon.gun == 'UMP' or weapon.gun == 'VECTOR' or weapon.gun == 'P90':
            x = weapon.p.wx + math.cos(weapon.deg) * 140
            y = weapon.p.wy + math.sin(weapon.deg) * 140

        elif weapon.gun == 'THOMPSON':
            x = weapon.p.wx + math.cos(weapon.deg) * 150
            y = weapon.p.wy + math.sin(weapon.deg) * 150

        elif weapon.gun == 'GROZA':
            x = weapon.p.wx + math.cos(weapon.deg) * 150
            y = weapon.p.wy - 5 + math.sin(weapon.deg) * 150

        if weapon.gun_type == 'pistol':
            if weapon.gun == 'QHAND':
                if weapon.fire_pos == 'in':
                    x = weapon.p.wx + math.cos(weapon.deg) * 160
                    y = weapon.p.wy + math.sin(weapon.deg) * 160
                else:
                    x = weapon.p.wx + math.cos(weapon.deg) * 200
                    y = weapon.p.wy + math.sin(weapon.deg) * 200

            elif weapon.gun == 'DEGLE' or weapon.gun == 'M500':
                x = weapon.p.wx + math.cos(weapon.deg) * 160
                y = weapon.p.wy + math.sin(weapon.deg) * 160

            else:
                x = weapon.p.wx + math.cos(weapon.deg) * 130
                y = weapon.p.wy + math.sin(weapon.deg) * 130

        else:
            x = weapon.p.wx + math.cos(weapon.deg) * 180
            y = weapon.p.wy + math.sin(weapon.deg) * 180

        if weapon.p.dir == 1:
            weapon.flame_right.clip_composite_draw(0, 0, 100, 100, weapon.deg, '', x, y, 100, 100)
        elif weapon.p.dir == 0:
            weapon.flame_left.clip_composite_draw(0, 0, 100, 100, weapon.deg, 'h, v', x, y, 100, 100)
