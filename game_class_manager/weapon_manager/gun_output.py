import math


def draw_gun(weapon):
    x = weapon.p.wx

    # 특정 총기는 위치를 조금 다르게 지정
    if weapon.weapon_type == 0:
        if weapon.gun == 'M1':
            y = weapon.p.wy + 5

        if weapon.gun == 'GROZA':
            y = weapon.p.wy - 5

        else:
            y = weapon.p.wy

        if weapon.update_deg:
            weapon.deg = math.atan2(weapon.p.my - y, weapon.p.mx - x)  # 총기 이미지 출력 각도

        # GUN_NAME에 따라 사용하는 총기가 달라진다.
        if weapon.gun == 'M1911':
            if weapon.p.dir == 1:
                weapon.m1911_right.clip_composite_draw(0, 0, 200, 100, weapon.deg, '', x, y, 320, 160)
            elif weapon.p.dir == 0:
                weapon.m1911_left.clip_composite_draw(0, 0, 200, 100, weapon.deg, 'h, v', x, y, 320, 160)

        if weapon.gun == 'M92':
            if weapon.p.dir == 1:
                weapon.m92_right.clip_composite_draw(0, 0, 200, 100, weapon.deg, '', x, y, 300, 150)
            elif weapon.p.dir == 0:
                weapon.m92_left.clip_composite_draw(0, 0, 200, 100, weapon.deg, 'h, v', x, y, 300, 150)

        if weapon.gun == 'M500':
            if weapon.reloading:
                if weapon.p.dir == 1:
                    weapon.m500_spin_right.clip_composite_draw(0, 0, 200, 200, weapon.spin, '', x + 30, y, 300, 250)
                elif weapon.p.dir == 0:
                    weapon.m500_spin_left.clip_composite_draw(0, 0, 200, 200, -weapon.spin, 'h, v', x - 30, y, 300, 250)
            else:
                if weapon.p.dir == 1:
                    weapon.m500_right.clip_composite_draw(0, 0, 200, 100, weapon.deg, '', x, y, 300, 150)
                elif weapon.p.dir == 0:
                    weapon.m500_left.clip_composite_draw(0, 0, 200, 100, weapon.deg, 'h, v', x, y, 300, 150)

        if weapon.gun == 'DEGLE':
            if weapon.p.dir == 1:
                weapon.degle_right.clip_composite_draw(0, 0, 200, 100, weapon.deg, '', x, y, 320, 160)
            elif weapon.p.dir == 0:
                weapon.degle_left.clip_composite_draw(0, 0, 200, 100, weapon.deg, 'h, v', x, y, 320, 160)

        if weapon.gun == 'QHAND':
            if weapon.reloading:
                if weapon.p.dir == 1:
                    weapon.qhand_spin_right.clip_composite_draw(0, 0, 100, 100, weapon.spin, '', x + 50, y, 200, 150)
                    weapon.qhand_spin_right.clip_composite_draw(0, 0, 100, 100, weapon.spin, '', x + 10, y, 200, 150)

                elif weapon.p.dir == 0:
                    weapon.qhand_spin_left.clip_composite_draw(0, 0, 100, 100, -weapon.spin, 'h, v', x - 50, y, 200, 150)
                    weapon.qhand_spin_left.clip_composite_draw(0, 0, 100, 100, -weapon.spin, 'h, v', x - 10, y, 200, 150)
            else:
                if weapon.p.dir == 1:
                    weapon.qhand_right.clip_composite_draw(0, 0, 200, 100, weapon.deg, '', x, y, 300, 150)
                elif weapon.p.dir == 0:
                    weapon.qhand_left.clip_composite_draw(0, 0, 200, 100, weapon.deg, 'h, v', x, y, 300, 150)

        elif weapon.gun == 'AKS74':
            if weapon.p.dir == 1:
                weapon.aks74_right.clip_composite_draw(0, 0, 200, 100, weapon.deg, '', x, y, 200, 100)
            elif weapon.p.dir == 0:
                weapon.aks74_left.clip_composite_draw(0, 0, 200, 100, weapon.deg, 'h, v', x, y, 200, 100)

        elif weapon.gun == 'UMP':
            if weapon.p.dir == 1:
                weapon.ump_right.clip_composite_draw(0, 0, 200, 100, weapon.deg, '', x, y, 200, 100)
            elif weapon.p.dir == 0:
                weapon.ump_left.clip_composite_draw(0, 0, 200, 100, weapon.deg, 'h, v', x, y, 200, 100)

        elif weapon.gun == 'VECTOR':
            if weapon.p.dir == 1:
                weapon.vector_right.clip_composite_draw(0, 0, 200, 100, weapon.deg, '', x, y, 200, 100)
            elif weapon.p.dir == 0:
                weapon.vector_left.clip_composite_draw(0, 0, 200, 100, weapon.deg, 'h, v', x, y, 200, 100)

        elif weapon.gun == 'THOMPSON':
            if weapon.p.dir == 1:
                weapon.thompson_right.clip_composite_draw(0, 0, 200, 100, weapon.deg, '', x, y, 200, 100)
            elif weapon.p.dir == 0:
                weapon.thompson_left.clip_composite_draw(0, 0, 200, 100, weapon.deg, 'h, v', x, y, 200, 100)

        elif weapon.gun == 'P90':
            if weapon.p.dir == 1:
                weapon.p90_right.clip_composite_draw(0, 0, 200, 100, weapon.deg, '', x, y, 200, 100)
            elif weapon.p.dir == 0:
                weapon.p90_left.clip_composite_draw(0, 0, 200, 100, weapon.deg, 'h, v', x, y, 200, 100)

        elif weapon.gun == 'SCAR_H':
            if weapon.p.dir == 1:
                weapon.scar_right.clip_composite_draw(0, 0, 200, 100, weapon.deg, '', x, y, 240, 140)
            elif weapon.p.dir == 0:
                weapon.scar_left.clip_composite_draw(0, 0, 200, 100, weapon.deg, 'h, v', x, y, 240, 140)

        elif weapon.gun == 'M16':
            if weapon.p.dir == 1:
                weapon.m16_right.clip_composite_draw(0, 0, 200, 100, weapon.deg, '', x, y, 240, 140)
            elif weapon.p.dir == 0:
                weapon.m16_left.clip_composite_draw(0, 0, 200, 100, weapon.deg, 'h, v', x, y, 240, 140)

        elif weapon.gun == 'MP44':
            if weapon.p.dir == 1:
                weapon.mp44_right.clip_composite_draw(0, 0, 200, 100, weapon.deg, '', x, y, 240, 140)
            elif weapon.p.dir == 0:
                weapon.mp44_left.clip_composite_draw(0, 0, 200, 100, weapon.deg, 'h, v', x, y, 240, 140)

        elif weapon.gun == 'AUG':
            if weapon.p.dir == 1:
                weapon.aug_right.clip_composite_draw(0, 0, 200, 100, weapon.deg, '', x, y, 240, 140)
            elif weapon.p.dir == 0:
                weapon.aug_left.clip_composite_draw(0, 0, 200, 100, weapon.deg, 'h, v', x, y, 240, 140)

        elif weapon.gun == 'GROZA':
            if weapon.p.dir == 1:
                weapon.groza_right.clip_composite_draw(0, 0, 200, 100, weapon.deg, '', x, y, 240, 140)
            elif weapon.p.dir == 0:
                weapon.groza_left.clip_composite_draw(0, 0, 200, 100, weapon.deg, 'h, v', x, y, 240, 140)

        elif weapon.gun == 'M1':
            if weapon.p.dir == 1:
                weapon.m1_right.clip_composite_draw(0, 0, 250, 100, weapon.deg, '', x, y, 270, 120)
            elif weapon.p.dir == 0:
                weapon.m1_left.clip_composite_draw(0, 0, 250, 100, weapon.deg, 'h, v', x, y, 270, 120)

        elif weapon.gun == 'WIN':
            if weapon.is_spin and weapon.shoot_delay < 200:  # 윈체스터는 총을 휘둘러 장전한다
                if weapon.p.dir == 1:
                    weapon.win_spin_right.clip_composite_draw(0, 0, 300, 300, weapon.deg + weapon.spin,
                                                              '', x, y, 300, 300)
                elif weapon.p.dir == 0:
                    weapon.win_spin_left.clip_composite_draw(0, 0, 300, 300, weapon.deg - weapon.spin,
                                                             'h, v', x, y, 300, 300)
            else:
                if weapon.p.dir == 1:
                    weapon.win_right.clip_composite_draw(0, 0, 300, 100, weapon.deg, '', x, y, 300, 100)
                elif weapon.p.dir == 0:
                    weapon.win_left.clip_composite_draw(0, 0, 300, 100, weapon.deg, 'h, v', x, y, 300, 100)

        elif weapon.gun == 'MINI14':
            if weapon.p.dir == 1:
                weapon.mini14_right.clip_composite_draw(0, 0, 200, 100, weapon.deg, '', x, y, 230, 130)
            elif weapon.p.dir == 0:
                weapon.mini14_left.clip_composite_draw(0, 0, 200, 100, weapon.deg, 'h, v', x, y, 230, 130)

        elif weapon.gun == 'FAL':
            if weapon.p.dir == 1:
                weapon.fal_right.clip_composite_draw(0, 0, 250, 100, weapon.deg, '', x, y, 270, 120)
            elif weapon.p.dir == 0:
                weapon.fal_left.clip_composite_draw(0, 0, 250, 100, weapon.deg, 'h, v', x, y, 270, 120)

        elif weapon.gun == 'LVOAS':
            if weapon.p.dir == 1:
                weapon.lvoas_right.clip_composite_draw(0, 0, 250, 100, weapon.deg, '', x, y, 250, 100)
            elif weapon.p.dir == 0:
                weapon.lvoas_left.clip_composite_draw(0, 0, 250, 100, weapon.deg, 'h, v', x, y, 250, 100)

        elif weapon.gun == 'SPRING':
            if weapon.p.dir == 1:
                weapon.spring_right.clip_composite_draw(0, 0, 250, 100, weapon.deg, '', x, y, 270, 120)
            elif weapon.p.dir == 0:
                weapon.spring_left.clip_composite_draw(0, 0, 250, 100, weapon.deg, 'h, v', x, y, 270, 120)

        elif weapon.gun == 'KAR98':
            if weapon.p.dir == 1:
                weapon.kar98_right.clip_composite_draw(0, 0, 250, 100, weapon.deg, '', x, y, 270, 120)
            elif weapon.p.dir == 0:
                weapon.kar98_left.clip_composite_draw(0, 0, 250, 100, weapon.deg, 'h, v', x, y, 270, 120)

        elif weapon.gun == 'M24':
            if weapon.p.dir == 1:
                weapon.m24_right.clip_composite_draw(0, 0, 250, 100, weapon.deg, '', x, y, 270, 120)
            elif weapon.p.dir == 0:
                weapon.m24_left.clip_composite_draw(0, 0, 250, 100, weapon.deg, 'h, v', x, y, 270, 120)

        elif weapon.gun == 'AWP':
            if weapon.p.dir == 1:
                weapon.awp_right.clip_composite_draw(0, 0, 300, 100, weapon.deg, '', x, y, 340, 120)
            elif weapon.p.dir == 0:
                weapon.awp_left.clip_composite_draw(0, 0, 300, 100, weapon.deg, 'h, v', x, y, 340, 120)

        elif weapon.gun == 'CHEYTAC':
            if weapon.p.dir == 1:
                weapon.cheytac_right.clip_composite_draw(0, 0, 300, 100, weapon.deg, '', x, y, 340, 120)
            elif weapon.p.dir == 0:
                weapon.cheytac_left.clip_composite_draw(0, 0, 300, 100, weapon.deg, 'h, v', x, y, 340, 120)
