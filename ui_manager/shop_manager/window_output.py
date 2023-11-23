from pico2d import draw_rectangle

from config import *
from game_work import game_framework
from mods import play_mode
from ui_manager.shop_manager.etc import set_equiped_gun_ind_pos


# 상점 창 출력
def draw_shop_window(self):
    self.back.draw(self.x, self.y, WIDTH, HEIGHT)
    self.back.opacify(80)
    self.button_gun.draw(self.cat_x[0], self.cat_y[0], 200, 120)
    self.button_melee.draw(self.cat_x[1], self.cat_y[1], 200, 120)
    self.button_exp.draw(self.cat_x[2], self.cat_y[2], 200, 120)
    self.window.draw(self.x, self.window_y, 950, 550)
    self.coin_icon.draw(WIDTH / 2 - 420, self.window_y - 280, 50, 50)
    self.font_small.draw(WIDTH / 2 - 390, self.window_y - 280, '%d' % play_mode.p.coin, (255, 255, 255))

    # 카테고리 및 페이지에 따라 출력되는 버튼 개수가 다르다
    if self.select_mode == 0:
        if self.page == 1:
            for i in range(5):
                for j in range(4):
                    self.button.draw(self.button_x[i], self.button_y[j], 160, 110)
        elif self.page == 2:
            for i in range(5):
                for j in range(1):
                    self.button.draw(self.button_x[i], self.button_y[j], 160, 110)

    elif self.select_mode == 1:
        for i in range(5):
            for j in range(1):
                self.button.draw(self.button_x[i], self.button_y[j], 160, 110)

    else:
        for i in range(5):
            for j in range(4):
                self.button.draw(self.button_x[i], self.button_y[j], 160, 110)

    self.font.draw(WIDTH / 2 + 200, self.window_y + 295, "SHOP", (255, 255, 255))
    if self.select_mode == 0:
        self.font.draw(WIDTH / 2 + 500, self.window_y - 120, "A", (255, 255, 255))
        self.font.draw(WIDTH / 2 + 570, self.window_y - 120, "D", (255, 255, 255))

        self.button_page_right.composite_draw(0, '', self.page_right_x, self.page_right_y, 80, 100)
        self.button_page_left.composite_draw(0, 'h', self.page_left_x, self.page_left_y, 80, 100)

    self.info_back.draw(WIDTH / 2 + 560, self.window_y + 75, 240, 342)


# 커서 출력
def draw_cursor(self):
    self.cursor.draw(self.mx + 35, self.my - 35, 70, 70)


# 최초 상점 실행 시 밑에서 위로 창이 올라온다
def window_animation(self):
    pps = game_framework.pps

    if self.window_y <= HEIGHT / 2:
        self.window_y += 20 * pps / 4
        for i in range(len(self.button_y)):
            self.button_y[i] += 20 * pps / 4
        for i in range(len(self.cat_x)):
            self.cat_y[i] += 20 * pps / 4

        self.page_right_y += 20 * pps / 4
        self.page_left_y += 20 * pps / 4

    if self.window_y > HEIGHT / 2:
        self.window_y = HEIGHT / 2

        for i in range(len(self.button_y)):
            self.button_y[i] = self.window_y + 175 - (115 * i)

        for i in range(len(self.cat_x)):
            self.cat_y[i] = self.window_y + 270

        self.page_right_y = self.window_y - 200
        self.page_left_y = self.window_y - 200


# 선택한 카테고리 버튼은 위로 올라와 표시된다
def update_cat_button(self):
    self.cat_y[self.select_mode] = self.window_y + 290


def draw_ind(self):
    if self.select_mode == 0:
        if self.page == self.eq_page:
            self.ind_equip.draw\
                (self.button_x[self.eq_gun_x], self.button_y[self.eq_gun_y], self.eq_size_x, self.eq_size_y)

    elif self.select_mode == 1:
        self.ind_equip.draw\
            (self.button_x[self.eq_melee_x], self.button_y[self.eq_melee_y], self.eq_size_x, self.eq_size_y)

    if self.selected_item:
        if self.sel_cat == self.select_mode:
            self.ind_select.draw\
                (self.button_x[self.ind_sel_x], self.button_y[self.ind_sel_y], self.sel_size_x, self.sel_size_y)


def update_ind_size(self):  # 아이템 선택 피드백을 출력한다.
    pps = game_framework.pps
    if self.eq_size_x > 160:
        self.eq_size_x -= pps / 2
    if self.eq_size_y > 110:
        self.eq_size_y -= pps / 2

    if self.eq_size_x < 160:
        self.eq_size_x = 160
    if self.eq_size_y < 110:
        self.eq_size_y = 110

    if self.sel_size_big:  # 이미지가 커졌다 작아졌다를 반복한다.
        self.sel_size_x = 180
        self.sel_size_y = 130
        self.sel_size_delay += pps / 3
        if self.sel_size_delay >= 100:
            self.sel_size_delay = 0
            self.sel_size_small = True
            self.sel_size_big = False

    elif self.sel_size_small:
        self.sel_size_x = 160
        self.sel_size_y = 110
        self.sel_size_delay += pps / 3
        if self.sel_size_delay >= 100:
            self.sel_size_delay = 0
            self.sel_size_big = True
            self.sel_size_small = False

