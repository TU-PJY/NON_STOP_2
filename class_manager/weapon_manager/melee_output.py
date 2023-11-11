def draw_melee(weapon):
    y = weapon.p.py - 10  # 고정값
    if weapon.weapon_type == 1:
        if weapon.melee_x == 0 and weapon.melee == 'KNIFE':
            weapon.melee_deg = 170

        if weapon.melee == 'KNIFE':
            if weapon.p.dir == 1:
                x = weapon.p.px + weapon.melee_x + 50
                weapon.knife_right.clip_composite_draw(0, 0, 150, 100, weapon.melee_deg, '', x, y, 100, 50)
            elif weapon.p.dir == 0:
                x = weapon.p.px - weapon.melee_x - 50
                weapon.knife_left.clip_composite_draw(0, 0, 150, 100, -weapon.melee_deg, '', x, y, 100, 50)
