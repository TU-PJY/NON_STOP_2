def draw_monster(m):
    x = m.x + m.p.ex
    y = m.y + m.p.ey
    m.hp_back.draw(x, y + 100, 210, 25)  # 체력 바
    m.hp_front.draw(x - 100 + (200 * m.hp / m.hp_length) / 2, y + 100, 200 * m.hp / m.hp_length, 20)

    m.flip = '' if m.dir == 0 else 'h'  # 보는 방향에 따라 이미지 방향이 바뀐다.

    if m.type == 1:
        m.type1_damage.opacify(m.op)
        m.type1.clip_composite_draw \
            (int(m.frame) * 64, 0, 64, 64, 0, m.flip, x, y + m.size / 6, 280, 280 + m.size)
        m.type1_damage.clip_composite_draw \
            (int(m.frame) * 64, 0, 64, 64, 0, m.flip, x, y + m.size / 6, 280, 280 + m.size)

    if m.type == 2:
        m.type2_damage.opacify(m.op)
        m.type2.clip_composite_draw \
            (int(m.frame) * 128, 0, 128, 128, 0, m.flip, x, y, 400, 400 + m.size)
        m.type2_damage.clip_composite_draw \
            (int(m.frame) * 128, 0, 128, 128, 0, m.flip, x, y, 400, 400 + m.size)

    if m.type == 3:
        m.type3_damage.opacify(m.op)
        m.type3.clip_composite_draw \
            (int(m.frame) * 128, 0, 128, 128, 0, m.flip, x, y + m.size2 * 50 + m.size / 5,
             300, 300 + m.size2 * 100 + m.size)
        m.type3_damage.clip_composite_draw \
            (int(m.frame) * 128, 0, 128, 128, 0, m.flip, x, y + m.size2 * 50 + m.size / 5,
             300, 300 + m.size2 * 100 + m.size)

    if m.type == 4:
        m.type4_damage.opacify(m.op)
        m.type4.clip_composite_draw \
            (int(m.frame) * 128, 0, 128, 128, 0, m.flip, x, y, 450, 450)
        m.type4_damage.clip_composite_draw \
            (int(m.frame) * 128, 0, 128, 128, 0, m.flip, x, y, 450, 450)
