from config import *
from mods import play_mode


def make_button_pos(self):  # shop 버튼 위치 생성
    # 모든 버튼의 위치가 창의 y 좌표를 기준으로 생성된다
    for i in range(5):
        self.button_x.append(WIDTH / 2 - 345 + (170 * i))
        for j in range(4):
            self.button_y.append(self.window_y + 175 - (115 * j))

    for i in range(3):
        self.cat_x.append((WIDTH / 2 - 320) + 200 * i)
        for j in range(1):
            self.cat_y.append(self.window_y + 270)

    self.page_left_x = WIDTH / 2 + 500
    self.page_left_y = self.window_y - 200
    self.page_right_x = WIDTH / 2 + 600
    self.page_right_y = self.window_y - 200


def set_equiped_gun_ind_pos(self):  # 장착 중인 아이템 강조
    if self.select_mode == 0:
        if self.page == 1:
            for i in range(5):
                for j in range(4):
                    if play_mode.weapon.equip_list_gun1[i][j]:
                        self.eq_gun_x, self.eq_gun_y = i, j

        elif self.page == 2:
            for i in range(5):
                for j in range(1):
                    if play_mode.weapon.equip_list_gun2[i][j]:
                        self.eq_gun_x, self.eq_gun_y = i, j

    elif self.select_mode == 1:
        for i in range(5):
            for j in range(1):
                if play_mode.weapon.equip_list_melee[i][j]:
                    self.eq_melee_x, self.eq_melee_y = i, j
