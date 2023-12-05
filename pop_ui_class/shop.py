from pico2d import load_image, load_wav

from config import *
from game_work import game_manager, game_framework
from mods import play_mode
from pop_ui_class_manager.shop_manager.etc import make_button_pos, set_equiped_gun_ind_pos
from pop_ui_class_manager.shop_manager.file_loader import load_shop_resource
from pop_ui_class_manager.shop_manager.item_output import draw_items
from pop_ui_class_manager.shop_manager.item_pointer import hover_item
from pop_ui_class_manager.shop_manager.item_selector import select_item
from pop_ui_class_manager.shop_manager.page_and_cat_manager import click_button
from pop_ui_class_manager.shop_manager.window_output import draw_shop_window, draw_cursor, window_animation, \
    update_cat_button, \
    update_ind_size, draw_ind, update_item_size


class Shop:
    button_sound = None
    cant_buy = None
    select_gun = None
    select_melee = None
    buy_ammo = None
    buy_medkit = None
    buy_upgrade = None
    buy_sound = None

    window = None
    back = None
    button = None
    button_gun = None
    button_melee = None
    button_exp = None
    button_page_left = None
    button_page_right = None
    font = None
    font_small = None
    info = None
    info_back = None

    cursor = None

    coin_icon = None

    ind_equip = None
    ind_select = None

    ind_lock = None

    image_m1911 = None
    image_m92 = None
    image_m500 = None
    image_degle = None
    image_qhand = None

    image_aks74 = None
    image_ump = None
    image_vector = None
    image_thompson = None
    image_p90 = None

    image_scar = None
    image_m16 = None
    image_mp44 = None
    image_aug = None
    image_groza = None

    image_m1 = None
    image_win = None
    image_mini14 = None
    image_fal = None
    image_lvoas = None

    image_spring = None
    image_kar98 = None
    image_m24 = None
    image_awp = None
    image_cheytac = None

    image_knife = None
    image_bat = None
    image_rapier = None
    image_katana = None
    image_axe = None

    image_ammo_pistol = None
    image_ammo_ar = None
    image_ammo_rifle = None
    image_ammo_sr = None

    medkit = None
    hpup = None
    regenup = None
    grenup = None
    doublejump = None
    speedup = None

    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2

        self.height = HEIGHT

        # 기준 화면 세로 길이: 960px
        self.window_y = -500 + (self.height - 960)  # 초기 윈도우 y 위치, 화면 세로 길이에 따라 초기 위치가 달라진다
        self.acc = 23 - (self.height - 960) / 200

        self.button_x = []  # 아이템 버튼의 x, y 좌표
        self.button_y = []
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

        self.eq_gun_x = 0  # 장착 중인 총 표시 위치, 버튼의 인덱스로 위치를 잡는다.
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

        self.op = 0

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


class Back3:
    def __init__(self):
        self.image = load_image(pause_bg_directory)
        self.op = 0.6

    def draw(self):
        self.image.opacify(self.op)
        self.image.draw(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)

    def update(self):
        pps = game_framework.pps
        self.op -= pps / 400
        if self.op < 0:
            game_manager.remove_object(self)
