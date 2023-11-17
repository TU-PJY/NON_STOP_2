from config import *
from game_work import game_framework


def draw_shop_window(self):
    self.back.draw(self.x, self.y, WIDTH, HEIGHT)
    self.back.opacify(80)
    self.button_gun.draw(self.cat_x[0], self.cat_y[0], 200, 120)
    self.button_melee.draw(self.cat_x[1], self.cat_y[1], 200, 120)
    self.button_exp.draw(self.cat_x[2], self.cat_y[2], 200, 120)
    self.window.draw(self.x, self.window_y, 950, 550)

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


def draw_cursor(self):
    self.cursor.draw(self.mx + 50, self.my - 50, 70, 70)


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


def update_cat_button(self):
    self.cat_y[self.select_mode] = self.window_y + 290
