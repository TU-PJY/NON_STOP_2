from config import *
from mods import play_mode
from ui_class_manager.shop_manager.etc import make_button_pos, set_equiped_gun_ind_pos
from ui_class_manager.shop_manager.file_loader import load_shop_resource
from ui_class_manager.shop_manager.item_output import draw_items
from ui_class_manager.shop_manager.item_pointer import hover_item
from ui_class_manager.shop_manager.item_selector import select_item
from ui_class_manager.shop_manager.page_and_cat_manager import click_button
from ui_class_manager.shop_manager.window_output import draw_shop_window, draw_cursor, window_animation, \
    update_cat_button, \
    update_ind_size, draw_ind, update_item_size


class Shop:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.button_x = []  # 아이템 버튼의 x, y 좌표
        self.button_y = []
        self.window_y = -500  # 초기 윈도우 t 위치
        self.mx = 0  # 마우스좌표
        self.my = 0
        self.click = False  # 마우스 누름 여부
        self.right_click = False  # 마우스 우클릭 여부
        self.select_gun = ''  # 현재 선택한 총
        self.select_melee = ''  # 현재 선택한 근접무기
        self.select_item = ''  # 현재 선택한 아이템

        self.select_mode = 0  # 초기값 총 선택
        self.cat_x = []  # 카테고리 버튼의 x, y 좌표
        self.cat_y = []
        #  페이지에 사용 중인 총이 있다면 해당 총이 존재하는 페이지를 먼저 출력
        if not play_mode.weapon.gun_type == 'sr':
            self.page = 1
        else:
            self.page = 2

        self.page_right_x = 0  # 페이지 이동 버튼 좌표
        self.page_left_x = 0
        self.page_right_y = 0
        self.page_left_y = 0

        self.ep_gun_x = 0  # 장착 중인 총 표시 위치, 버튼의 인덱스로 위치를 잡는다.
        self.eq_gun_y = 0
        self.eq_page = play_mode.weapon.eq_page  # 현재 장착 중인 총이 존재하는 페이지에서만 표시한다

        self.eq_melee_x = 0  # 장착 중인 근접 무기 표시 위치
        self.eq_melee_y = 0

        self.ind_sel_x = 0  # 마우스로 선택한 아이템 표시기 위치
        self.ind_sel_y = 0
        self.sel_page = 0  # 특정 페이지에서만 표시되도록 함
        self.sel_cat = 0  # 특정 카테고리에서만 표시되도록 함

        self.eq_size_x = 160  # 표시기 크기
        self.eq_size_y = 110

        self.sel_size_big, self.sel_size_small = True, False  # 선택 아이템 피드백 변수
        self.sel_size_x = 160
        self.sel_size_y = 110
        self.sel_size_delay = 0

        self.size_list = [[100 for i in range(4)] for j in range(5)]

        self.ind_sel_on = False  # 아이템 선택 시 현재 선택중인 아이템을 표시함다. 해당 아이템 장착 시 사라진다.
        self.data_change = False  # 구입한 항목에 대해서만 아이템 관련 변수 값 변경을 허용한다.

        load_shop_resource(self)
        make_button_pos(self)

    def draw(self):
        draw_shop_window(self)
        draw_items(self)
        draw_ind(self)
        draw_cursor(self)
        hover_item(self)  # 정보가 맨 위에 출력해야 하므로 예외적으로 draw에 작성

    def update(self):
        window_animation(self)
        update_cat_button(self)
        update_item_size(self)

        if self.click:
            click_button(self)
            select_item(self)

        update_ind_size(self)
        set_equiped_gun_ind_pos(self)

    def handle_event(self):
        pass
