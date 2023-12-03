def click_button(self):
    from pop_ui_class.shop import Shop

    play_sound = True

    if self.select_mode == 0:
        # 페이지 이동 버튼 클릭
        if self.page_right_x - 40 < self.mx < self.page_right_x + 40 and \
                self.page_right_y - 50 < self.my < self.page_right_y + 50:
            Shop.button_sound.play()
            if self.page < 2:
                self.page += 1
                self.ind_sel_on = False

        elif self.page_left_x - 40 < self.mx < self.page_left_x + 40 and \
                self.page_left_y - 50 < self.my < self.page_left_y + 50:
            Shop.button_sound.play()
            if self.page > 1:
                self.page -= 1
                self.ind_sel_on = False

    # 카테고리 버튼 클릭
    for i in range(len(self.cat_x)):
        for j in range(len(self.cat_y)):
            if self.cat_x[i] - 100 < self.mx < self.cat_x[i] + 100 and \
                    self.cat_y[j] - 20 < self.my < self.cat_y[j] + 60:

                if play_sound:
                    Shop.button_sound.play()
                    play_sound = False

                if i == 0:
                    self.select_mode = 0  # gun
                elif i == 1:
                    self.select_mode = 1  # melee
                elif i == 2:
                    self.select_mode = 2  # exp

                self.ind_sel_on = False

    self.click = False
