from config import *
from mods import play_mode
from ui_manager.shop_manager.etc import make_button_pos
from ui_manager.shop_manager.file_loader import load_shop_resource
from ui_manager.shop_manager.item_output import draw_items
from ui_manager.shop_manager.item_selector import click_button
from ui_manager.shop_manager.window_output import draw_shop_window, draw_cursor, window_animation, update_cat_button


class Shop:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.button_x = []
        self.button_y = []
        self.window_y = -500
        self.mx = 0
        self.my = 0
        self.click = False  # 마우스 누름 여부
        self.select_mode = 0  # 초기값 총 선택
        self.cat_x = []
        self.cat_y = []
        if not play_mode.weapon.gun_type == 'sr':
            self.page = 1
        else:
            self.page = 2

        self.page_right_x = 0
        self.page_left_x = 0
        self.page_right_y = 0
        self.page_left_y = 0

        load_shop_resource(self)
        make_button_pos(self)

    def draw(self):
        draw_shop_window(self)
        draw_items(self)
        draw_cursor(self)

    def update(self):
        window_animation(self)
        update_cat_button(self)
        if self.click:
            click_button(self)

    def handle_event(self):
        pass
