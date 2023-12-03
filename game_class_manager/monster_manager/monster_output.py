def draw_monster(m):
    from game_class.monster import Monster

    x = m.x + m.p.ex
    y = m.y + m.p.ey
    Monster.hp_back.draw(x, y + 100, 210, 25)  # 체력 바
    Monster.hp_front.draw(x - 100 + (200 * m.hp / m.hp_length) / 2, y + 100, 200 * m.hp / m.hp_length, 20)

    m.flip = '' if m.dir == 0 else 'h'  # 보는 방향에 따라 이미지 방향이 바뀐다.

    if m.type == 1:
        Monster.type1_damage.opacify(m.op)
        Monster.type1.clip_composite_draw \
            (int(m.frame) * 64, 0, 64, 64, 0, m.flip, x, y + m.size / 6, 280, 280 + m.size)
        Monster.type1_damage.clip_composite_draw \
            (int(m.frame) * 64, 0, 64, 64, 0, m.flip, x, y + m.size / 6, 280, 280 + m.size)

    if m.type == 2:
        Monster.type2_damage.opacify(m.op)
        Monster.type2.clip_composite_draw \
            (int(m.frame) * 128, 0, 128, 128, 0, m.flip, x, y, 400, 400 + m.size)
        Monster.type2_damage.clip_composite_draw \
            (int(m.frame) * 128, 0, 128, 128, 0, m.flip, x, y, 400, 400 + m.size)

    if m.type == 3:
        Monster.type3_damage.opacify(m.op)
        Monster.type3.clip_composite_draw \
            (int(m.frame) * 128, 0, 128, 128, 0, m.flip, x, y + m.size2 * 50 + m.size / 5,
             300, 300 + m.size2 * 100 + m.size)
        Monster.type3_damage.clip_composite_draw \
            (int(m.frame) * 128, 0, 128, 128, 0, m.flip, x, y + m.size2 * 50 + m.size / 5,
             300, 300 + m.size2 * 100 + m.size)

    if m.type == 4:
        Monster.type4_damage.opacify(m.op)
        Monster.type4.clip_composite_draw \
            (int(m.frame) * 128, 0, 128, 128, 0, m.flip, x, y, 450, 450)
        Monster.type4_damage.clip_composite_draw \
            (int(m.frame) * 128, 0, 128, 128, 0, m.flip, x, y, 450, 450)
