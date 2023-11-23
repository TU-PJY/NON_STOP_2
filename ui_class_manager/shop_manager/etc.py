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


def set_equiped_gun_ind_pos(self):  # 장착 중인 아이템 표시
    if self.select_mode == 0:
        if self.page == 1:
            if play_mode.weapon.gun == 'M1911':
                self.eq_gun_x, self.eq_gun_y = 0, 0
            elif play_mode.weapon.gun == 'M92':
                self.eq_gun_x, self.eq_gun_y = 1, 0
            elif play_mode.weapon.gun == 'DEGLE':
                self.eq_gun_x, self.eq_gun_y = 2, 0
            elif play_mode.weapon.gun == 'M500':
                self.eq_gun_x, self.eq_gun_y = 3, 0
            elif play_mode.weapon.gun == 'QHAND':
                self.eq_gun_x, self.eq_gun_y = 4, 0
            elif play_mode.weapon.gun == 'AKS74':
                self.eq_gun_x, self.eq_gun_y = 0, 1
            elif play_mode.weapon.gun == 'UMP':
                self.eq_gun_x, self.eq_gun_y = 1, 1
            elif play_mode.weapon.gun == 'VECTOR':
                self.eq_gun_x, self.eq_gun_y = 2, 1
            elif play_mode.weapon.gun == 'THOMPSON':
                self.eq_gun_x, self.eq_gun_y = 3, 1
            elif play_mode.weapon.gun == 'P90':
                self.eq_gun_x, self.eq_gun_y = 4, 1
            elif play_mode.weapon.gun == 'SCAR_H':
                self.eq_gun_x, self.eq_gun_y = 0, 2
            elif play_mode.weapon.gun == 'M16':
                self.eq_gun_x, self.eq_gun_y = 1, 2
            elif play_mode.weapon.gun == 'MP44':
                self.eq_gun_x, self.eq_gun_y = 2, 2
            elif play_mode.weapon.gun == 'AUG':
                self.eq_gun_x, self.eq_gun_y = 3, 2
            elif play_mode.weapon.gun == 'GROZA':
                self.eq_gun_x, self.eq_gun_y = 4, 2
            elif play_mode.weapon.gun == 'M1':
                self.eq_gun_x, self.eq_gun_y = 0, 3
            elif play_mode.weapon.gun == 'WIN':
                self.eq_gun_x, self.eq_gun_y = 1, 3
            elif play_mode.weapon.gun == 'MINI14':
                self.eq_gun_x, self.eq_gun_y = 2, 3
            elif play_mode.weapon.gun == 'FAL':
                self.eq_gun_x, self.eq_gun_y = 3, 3
            elif play_mode.weapon.gun == 'LVOAS':
                self.eq_gun_x, self.eq_gun_y = 4, 3

        elif self.page == 2:
            if play_mode.weapon.gun == 'SPRING':
                self.eq_gun_x, self.eq_gun_y = 0, 0
            elif play_mode.weapon.gun == 'KAR98':
                self.eq_gun_x, self.eq_gun_y = 1, 0
            elif play_mode.weapon.gun == 'M24':
                self.eq_gun_x, self.eq_gun_y = 2, 0
            elif play_mode.weapon.gun == 'AWP':
                self.eq_gun_x, self.eq_gun_y = 3, 0
            elif play_mode.weapon.gun == 'CHEYTAC':
                self.eq_gun_x, self.eq_gun_y = 4, 0

    elif self.select_mode == 1:
        if play_mode.weapon.melee == 'KNIFE':
            self.eq_melee_x, self.eq_melee_y = 0, 0
        if play_mode.weapon.melee == 'BAT':
            self.eq_melee_x, self.eq_melee_y = 1, 0
        if play_mode.weapon.melee == 'RAPIER':
            self.eq_melee_x, self.eq_melee_y = 2, 0
        if play_mode.weapon.melee == 'KATANA':
            self.eq_melee_x, self.eq_melee_y = 3, 0
        if play_mode.weapon.melee == 'AXE':
            self.eq_melee_x, self.eq_melee_y = 4, 0
