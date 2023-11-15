def draw_melee(weapon):

    if weapon.weapon_type == 1:
        if weapon.melee_x == 0 and weapon.melee == 'KNIFE':
            weapon.melee_deg = 170

        if weapon.melee == 'BAT' and not weapon.swing:
            weapon.melee_deg = 120

        if weapon.melee == 'KNIFE':
            y = weapon.p.py - 10  # 고정값

        if weapon.melee == 'BAT':
            y = weapon.p.py

        if weapon.melee == 'KNIFE':
            if weapon.p.dir == 1:
                x = weapon.p.px + weapon.melee_x + 50
                weapon.knife_right.clip_composite_draw(0, 0, 150, 100, weapon.melee_deg, '', x, y, 100, 50)
            elif weapon.p.dir == 0:
                x = weapon.p.px - weapon.melee_x - 50
                weapon.knife_left.clip_composite_draw(0, 0, 150, 100, -weapon.melee_deg, '', x, y, 100, 50)

        elif weapon.melee == 'BAT':
            if not weapon.swing or (weapon.swing and weapon.swing_up):
                if weapon.p.dir == 1:
                    x = weapon.p.px + weapon.melee_x
                    weapon.bat.clip_composite_draw(0, 0, 50, 400, weapon.melee_deg, '', x, y, 50, 400)
                elif weapon.p.dir == 0:
                    x = weapon.p.px - weapon.melee_x
                    weapon.bat.clip_composite_draw(0, 0, 50, 400, -weapon.melee_deg, 'h', x, y, 50, 400)

            elif weapon.swing and weapon.swing_down:
                if weapon.p.dir == 1:
                    x = weapon.p.px + weapon.melee_x
                    weapon.bat_swing.clip_composite_draw(0, 0, 400, 400, weapon.melee_deg, '', x, y, 400, 400)
                elif weapon.p.dir == 0:
                    x = weapon.p.px - weapon.melee_x
                    weapon.bat_swing.clip_composite_draw(0, 0, 400, 400, -weapon.melee_deg, 'h', x, y, 400, 400)


