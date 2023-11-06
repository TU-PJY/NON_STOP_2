from pico2d import *

from config import *
from game_work import game_framework
from mods import play_mode


def calc_pps():
    global pps
    pps = PPS * game_framework.frame_time


def load_shop_resource(self):
    self.window = load_image(shop_window_directory)
    self.back = load_image(pause_bg_directory)
    self.button = load_image(shop_button_directory)
    self.button_gun = load_image(button_gun_directory)
    self.button_melee = load_image(button_melee_directory)
    self.button_exp = load_image(button_exp_directory)
    self.font = load_font(font_directory, 50)

    self.image_scar = load_image(scar_h_right_directory)
    self.image_m16 = load_image(m16_right_directory)
    self.image_mp44 = load_image(mp44_right_directory)
    self.image_aug = load_image(aug_right_directory)
    self.image_groza = load_image(groza_right_directory)

    self.image_aks74 = load_image(aks74_right_directory)
    self.image_ump = load_image(ump_right_directory)
    self.image_vector = load_image(vector_right_directpry)
    self.image_thompson = load_image(thompson_right_directory)
    self.image_p90 = load_image(p90_right_directory)

    self.image_knife = load_image(knife_right_directory)


def make_button_pos(self):  # shop 버튼 위치 생성
    for i in range(5):
        self.button_x.append(WIDTH / 2 - 345 + (170 * i))
        for j in range(4):
            self.button_y.append(self.window_y + 175 - (115 * j))

    for i in range(3):
        self.cat_x.append((WIDTH / 2 - 320) + 200 * i)
        for j in range(1):
            self.cat_y.append(self.window_y + 270)


def draw_shop_window(self):
    self.back.draw(self.x, self.y, WIDTH, HEIGHT)
    self.back.opacify(80)
    self.button_gun.draw(self.cat_x[0], self.cat_y[0], 200, 120)
    self.button_melee.draw(self.cat_x[1], self.cat_y[1], 200, 120)
    self.button_exp.draw(self.cat_x[2], self.cat_y[2], 200, 120)
    self.window.draw(self.x, self.window_y, 950, 550)

    for i in range(5):
        for j in range(4):
            self.button.draw(self.button_x[i], self.button_y[j], 160, 110)
    self.font.draw(WIDTH / 2 + 200, self.window_y + 295, "SHOP", (255, 255, 255))


def draw_items(self):
    if self.select_mode == 0:
        self.image_scar.draw(self.button_x[0] - 30, self.button_y[2], 200, 150)
        self.image_m16.draw(self.button_x[1] - 30, self.button_y[2], 200, 150)
        self.image_mp44.draw(self.button_x[2] - 30, self.button_y[2], 200, 150)
        self.image_aug.draw(self.button_x[3] - 30, self.button_y[2], 200, 150)
        self.image_groza.draw(self.button_x[4] - 30, self.button_y[2], 200, 150)

        self.image_aks74.draw(self.button_x[0] - 30, self.button_y[1], 200, 150)
        self.image_ump.draw(self.button_x[1] - 30, self.button_y[1], 200, 150)
        self.image_vector.draw(self.button_x[2] - 20, self.button_y[1], 200, 150)
        self.image_thompson.draw(self.button_x[3] - 30, self.button_y[1], 200, 150)
        self.image_p90.draw(self.button_x[4] - 30, self.button_y[1], 200, 150)

    if self.select_mode == 1:
        self.image_knife.draw(self.button_x[0], self.button_y[0], 150, 100)


def window_animation(self):
    global pps
    if self.window_y <= HEIGHT / 2:
        self.window_y += 20 * pps / 4
        for i in range(len(self.button_y)):
            self.button_y[i] += 20 * pps / 4
        for i in range(len(self.cat_x)):
            self.cat_y[i] += 20 * pps / 4

    if self.window_y > HEIGHT / 2:
        self.window_y = HEIGHT / 2

        for i in range(len(self.button_y)):
            self.button_y[i] = self.window_y + 175 - (115 * i)

        for i in range(len(self.cat_x)):
            self.cat_y[i] = self.window_y + 270


def update_cat_button(self):
    self.cat_y[self.select_mode] = self.window_y + 290


def click_button(self):
    for i in range(len(self.cat_x)):
        for j in range(len(self.cat_y)):
            if self.cat_x[i] - 100 < self.mx < self.cat_x[i] + 100 and \
                    self.cat_y[i] - 20 < self.my < self.cat_y[i] + 60:
                if i == 0:
                    self.select_mode = 0  # gun
                elif i == 1:
                    self.select_mode = 1  # melee
                elif i == 2:
                    self.select_mode = 2  # exp


    if self.select_mode == 0:
        for i in range(len(self.button_x)):
            for j in range(len(self.button_y)):
                if self.button_x[i] - 90 < self.mx < self.button_x[i] + 90 and \
                        self.button_y[j] - 75 < self.my < self.button_y[j] + 75:
                    if (i, j) == (0, 2):
                        play_mode.weapon.gun = 'SCAR_H'
                    elif (i, j) == (1, 2):
                        play_mode.weapon.gun = 'M16'
                    elif (i, j) == (2, 2):
                        play_mode.weapon.gun = 'MP44'
                    elif (i, j) == (3, 2):
                        play_mode.weapon.gun = 'AUG'
                    elif (i, j) == (4, 2):
                        play_mode.weapon.gun = 'GROZA'
                    elif (i, j) == (0, 1):
                        play_mode.weapon.gun = 'AKS74'
                    elif (i, j) == (1, 1):
                        play_mode.weapon.gun = 'UMP'
                    elif (i, j) == (2, 1):
                        play_mode.weapon.gun = 'VECTOR'
                    elif (i, j) == (3, 1):
                        play_mode.weapon.gun = 'THOMPSON'
                    elif (i ,j) == (4, 1):
                        play_mode.weapon.gun = 'P90'

    self.click = False
