from mods import play_mode


def draw_items(self):
    from pop_ui_class.shop import Shop
    # 페이지 및 카테고리에 따라 아이템이 다르게 출력된다
    if self.select_mode == 0:
        if self.page == 1:
            Shop.image_m1911.draw(self.button_x[0] - 40, self.button_y[0], 400, 200)
            Shop.image_m92.draw(self.button_x[1] - 50, self.button_y[0], 400, 200)
            Shop.image_degle.draw(self.button_x[2] - 50, self.button_y[0], 400, 200)
            Shop.image_m500.draw(self.button_x[3] - 63, self.button_y[0], 400, 200)
            Shop.image_qhand.draw(self.button_x[4] - 70, self.button_y[0], 300, 150)

            Shop.image_aks74.draw(self.button_x[0] - 35, self.button_y[1], 240, 120)
            Shop.image_ump.draw(self.button_x[1] - 30, self.button_y[1], 240, 120)
            Shop.image_vector.draw(self.button_x[2] - 30, self.button_y[1], 240, 120)
            Shop.image_thompson.draw(self.button_x[3] - 35, self.button_y[1], 250, 120)
            Shop.image_p90.draw(self.button_x[4] - 30, self.button_y[1], 240, 120)

            Shop.image_scar.draw(self.button_x[0] - 40, self.button_y[2], 240, 120)
            Shop.image_m16.draw(self.button_x[1] - 40, self.button_y[2], 240, 120)
            Shop.image_mp44.draw(self.button_x[2] - 40, self.button_y[2], 240, 120)
            Shop.image_aug.draw(self.button_x[3] - 35, self.button_y[2], 240, 120)
            Shop.image_groza.draw(self.button_x[4] - 30, self.button_y[2], 240, 120)

            Shop.image_m1.draw(self.button_x[0] - 45, self.button_y[3], 250, 100)
            Shop.image_win.draw(self.button_x[1] - 52, self.button_y[3], 250, 75)
            Shop.image_mini14.draw(self.button_x[2] - 35, self.button_y[3], 200, 100)
            Shop.image_fal.draw(self.button_x[3] - 47, self.button_y[3], 250, 100)
            Shop.image_lvoas.draw(self.button_x[4] - 47, self.button_y[3], 230, 90)

        elif self.page == 2:
            Shop.image_spring.draw(self.button_x[0] - 50, self.button_y[0], 240, 95)
            Shop.image_kar98.draw(self.button_x[1] - 50, self.button_y[0], 240, 95)
            Shop.image_m24.draw(self.button_x[2] - 50, self.button_y[0], 240, 90)
            Shop.image_awp.draw(self.button_x[3] - 50, self.button_y[0], 250, 80)
            Shop.image_cheytac.draw(self.button_x[4] - 55, self.button_y[0], 250, 80)

    elif self.select_mode == 1:
        Shop.image_knife.draw(self.button_x[0], self.button_y[0], 150, 100)
        Shop.image_bat.rotate_draw(-45, self.button_x[1] - 43, self.button_y[0] - 30, 35, 325)
        Shop.image_rapier.rotate_draw(0.5, self.button_x[2] - 50, self.button_y[0] - 25, 300, 75)
        Shop.image_katana.rotate_draw(-45, self.button_x[3] - 45, self.button_y[0] - 33, 35, 260)
        Shop.image_axe.rotate_draw(-45, self.button_x[4] - 28, self.button_y[0] - 20, 128, 256)

    elif self.select_mode == 2:
        Shop.image_ammo_pistol.draw \
            (self.button_x[0], self.button_y[0], self.size_list[0][0], self.size_list[0][0])
        Shop.image_ammo_ar.draw \
            (self.button_x[1], self.button_y[0], self.size_list[1][0], self.size_list[1][0])
        Shop.image_ammo_rifle.draw \
            (self.button_x[2], self.button_y[0], self.size_list[2][0], self.size_list[2][0])
        Shop.image_ammo_sr.draw \
            (self.button_x[3], self.button_y[0], self.size_list[3][0], self.size_list[3][0])

        color = (50, 50, 50)

        Shop.medkit.draw(self.button_x[4], self.button_y[0], self.size_list[4][0], self.size_list[4][0])

        Shop.hpup.draw(self.button_x[0], self.button_y[1], self.size_list[0][1], self.size_list[0][1])
        if play_mode.p.hp_count == 3:
            color_hp = (0, 255, 0)
        else:
            color_hp = (50, 50, 50)
        Shop.font_small.draw(self.button_x[0] - 35, self.button_y[1] - 70, '%d | 3' % play_mode.p.hp_count, color_hp)

        Shop.regenup.draw(self.button_x[1], self.button_y[1], self.size_list[1][1], self.size_list[1][1])
        if play_mode.p.regen_count == 3:
            color_regen = (0, 255, 0)
        else:
            color_regen = (50, 50, 50)
        Shop.font_small.draw \
            (self.button_x[1] - 35, self.button_y[1] - 70, '%d | 3' % play_mode.p.regen_count, color_regen)

        Shop.speedup.draw(self.button_x[2], self.button_y[1], self.size_list[2][1], self.size_list[2][1])
        if play_mode.p.speed_count == 3:
            color_speed = (0, 255, 0)
        else:
            color_speed = (50, 50, 50)
        Shop.font_small.draw \
            (self.button_x[2] - 35, self.button_y[1] - 70, '%d | 3' % play_mode.p.speed_count, color_speed)

        Shop.doublejump.draw(self.button_x[3], self.button_y[1], self.size_list[3][1], self.size_list[3][1])
        if play_mode.p.jump_level == 3:
            color_jump = (0, 255, 0)
        else:
            color_jump = (50, 50, 50)
        Shop.font_small.draw \
            (self.button_x[3] - 35, self.button_y[1] - 70, '%d | 1' % play_mode.p.double_jump, color_jump)

        Shop.grenup.draw(self.button_x[4], self.button_y[1], self.size_list[4][1], self.size_list[4][1])
        if play_mode.p.gren_count == 2:
            color_gren = (0, 255, 0)
        else:
            color_gren = (50, 50, 50)
        Shop.font_small.draw \
            (self.button_x[4] - 35, self.button_y[1] - 70, '%d | 2' % play_mode.p.gren_count, color_gren)
