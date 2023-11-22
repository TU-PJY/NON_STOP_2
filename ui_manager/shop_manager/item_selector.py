from pico2d import draw_rectangle

from mods import play_mode


def click_button(self):
    if self.select_mode == 0:
        # 페이지 이동 버튼 클릭
        if self.page_right_x - 40 < self.mx < self.page_right_x + 40 and \
                self.page_right_y - 50 < self.my < self.page_right_y + 50:
            if self.page < 2:
                self.page += 1

        elif self.page_left_x - 40 < self.mx < self.page_left_x + 40 and \
                self.page_left_y - 50 < self.my < self.page_left_y + 50:
            if self.page > 1:
                self.page -= 1

    # 카테고리 버튼 클릭
    for i in range(len(self.cat_x)):
        for j in range(len(self.cat_y)):
            if self.cat_x[i] - 100 < self.mx < self.cat_x[i] + 100 and \
                    self.cat_y[j] - 20 < self.my < self.cat_y[j] + 60:
                if i == 0:
                    self.select_mode = 0  # gun
                elif i == 1:
                    self.select_mode = 1  # melee
                elif i == 2:
                    self.select_mode = 2  # exp

    # 아이템 버튼 클릭
    for i in range(len(self.button_x)):
        for j in range(len(self.button_y)):
            if self.button_x[i] - 75 < self.mx < self.button_x[i] + 75 and \
                    self.button_y[j] - 50 < self.my < self.button_y[j] + 50:
                if self.select_mode == 0:
                    if self.page == 1:
                        if (i, j) == (0, 0):
                            self.select_gun = 'M1911'
                        elif (i, j) == (1, 0):
                            self.select_gun = 'M92'
                        elif (i, j) == (2, 0):
                            self.select_gun = 'DEGLE'
                        elif (i, j) == (3, 0):
                            self.select_gun = 'M500'
                        elif (i, j) == (4, 0):
                            self.select_gun = 'QHAND'

                        elif (i, j) == (0, 1):
                            self.select_gun = 'AKS74'
                        elif (i, j) == (1, 1):
                            self.select_gun = 'UMP'
                        elif (i, j) == (2, 1):
                            self.select_gun = 'VECTOR'
                        elif (i, j) == (3, 1):
                            self.select_gun = 'THOMPSON'
                        elif (i, j) == (4, 1):
                            self.select_gun = 'P90'

                        elif (i, j) == (0, 2):
                            self.select_gun = 'SCAR_H'
                        elif (i, j) == (1, 2):
                            self.select_gun = 'M16'
                        elif (i, j) == (2, 2):
                            self.select_gun = 'MP44'
                        elif (i, j) == (3, 2):
                            self.select_gun = 'AUG'
                        elif (i, j) == (4, 2):
                            self.select_gun = 'GROZA'

                        elif (i, j) == (0, 3):
                            self.select_gun = 'M1'
                        elif (i, j) == (1, 3):
                            self.select_gun = 'WIN'
                        elif (i, j) == (2, 3):
                            self.select_gun = 'MINI14'
                        elif (i, j) == (3, 3):
                            self.select_gun = 'FAL'
                        elif (i, j) == (4, 3):
                            self.select_gun = 'LVOAS'

                    elif self.page == 2:
                        if (i, j) == (0, 0):
                            self.select_gun = 'SPRING'
                        if (i, j) == (1, 0):
                            self.select_gun = 'KAR98'
                        if (i, j) == (2, 0):
                            self.select_gun = 'M24'
                        if (i, j) == (3, 0):
                            self.select_gun = 'AWP'
                        if (i, j) == (4, 0):
                            self.select_gun = 'CHEYTAC'

                elif self.select_mode == 1:
                    if (i, j) == (0, 0):
                        self.select_melee = 'KNIFE'
                    elif (i, j) == (1, 0):
                        self.select_melee = 'BAT'
                    elif (i, j) == (2, 0):
                        self.select_melee = 'RAPIER'
                    elif (i, j) == (3, 0):
                        self.select_melee = 'KATANA'
                    elif (i, j) == (4, 0):
                        self.select_melee = 'AXE'

                elif self.select_mode == 2:
                    if (i, j) == (0, 0):
                        self.select_item = 'pistol_ammo'
                    elif (i, j) == (1, 0):
                        self.select_item = 'ar_ammo'
                    elif (i, j) == (2, 0):
                        self.select_item = 'rifle_ammo'
                    elif (i, j) == (3, 0):
                        self.select_item = 'sniper_ammo'

                self.ind_sel_x = i  # 표시할 위치, 페이지, 카테고리 저장
                self.ind_sel_y = j
                self.sel_page = self.page
                self.sel_cat = self.select_mode

                self.selected_item = True  # 선택한 이이템이 표시된다
    self.click = False
