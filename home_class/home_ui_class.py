from pico2d import *

from config import *
from game_work import game_framework
from home_class_manager.button_manager import home_update_button, home_draw_button, ch_draw_button, load_file, \
    ch_update_button, exit_draw_button, exit_update_button
from mods import play_mode


class Data:  # 홈 모드에서 사용되는 데이터를 저장하기 위한 가상 객체
    def __init__(self):
        self.mode = 'home'  # 모드에 따라 보이는 화면이 달라진다.
        self.exp = 0  # 캐릭터를 구매하는데에 필요한 재화

    def __getstate__(self):
        state = {'ch': self.ch}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def draw(self):
        pass

    def update(self):
        pass


class Button:
    def __init__(self, data, cursor):
        self.font = load_font(font2_directory, 50)
        self.cursor = cursor
        self.op1, self.op2, self.op3 = 0, 0, 0
        self.op4 = 0
        self.click = False
        self.data = data
        self.sel_x = 0

        self.op_bg = 0

        self.kx, self.ky = WIDTH / 2 + 300, -500
        self.kacc = 0
        self.deg, self.pos = 0, 0

        load_file(self)

    def draw(self):
        if self.data.mode == 'home':
            home_draw_button(self)
        elif self.data.mode == 'ch_mode':
            ch_draw_button(self)
        elif self.data.mode == 'exit_mode':
            exit_draw_button(self)

    def update(self):
        if self.data.mode == 'home':
            home_update_button(self)
        elif self.data.mode == 'ch_mode':
            ch_update_button(self)
        elif self.data.mode == 'exit_mode':
            exit_update_button(self)

        self.click = False


class Background:
    def __init__(self, data, cursor):
        self.cursor = cursor
        self.back = load_image(bg_back_image_directory)
        self.bg = load_image(bg_image_directory)
        self.logo = load_image(logo_directory)
        self.data = data

    def draw(self):
        ex = (WIDTH / 2 - self.cursor.mx) / 30
        ey = (HEIGHT / 2 - self.cursor.my) / 30
        self.back.draw(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
        self.bg.draw(WIDTH / 2 + ex, HEIGHT / 2 - 200 + ey, 4096, 1100)
        if self.data.mode == 'home':
            self.logo.draw(WIDTH / 2 + ex + 50, HEIGHT - 200 + ey, 1000, 500)

    def update(self):
        pass


class Playerimage:
    def __init__(self, cursor, data):
        self.ch1 = load_image(player1_right_image_directory)
        self.ch1 = load_image(player1_right_image_directory)
        self.ch2 = load_image(player2_right_image_directory)
        self.ch3 = load_image(player3_right_image_directory)
        self.ch4 = load_image(player4_right_image_directory)
        self.ch5 = load_image(player5_right_image_directory)
        self.ch6 = load_image(player6_right_image_directory)
        self.ch7 = load_image(player7_right_image_directory)
        self.ch8 = load_image(player8_right_image_directory)

        self.gun_image = load_image(scar_h_right_directory)
        self.cursor = cursor
        self.size = 0
        self.deg = 0
        self.data = data

    def draw(self):
        ex = (WIDTH / 2 - self.cursor.mx) / 10
        ey = (HEIGHT / 2 - self.cursor.my) / 10
        match self.data.ch:
            case 1:
                self.ch1.rotate_draw(math.radians(-3), 450 + ex, 100 + ey + self.size / 2, 1500, 1500 + self.size)
            case 2:
                self.ch2.rotate_draw(math.radians(-3), 450 + ex, 100 + ey + self.size / 2, 1500, 1500 + self.size)
            case 3:
                self.ch3.rotate_draw(math.radians(-3), 450 + ex, 100 + ey + self.size / 2, 1500, 1500 + self.size)
            case 4:
                self.ch4.rotate_draw(math.radians(-3), 450 + ex, 100 + ey + self.size / 2, 1500, 1500 + self.size)
            case 5:
                self.ch5.rotate_draw(math.radians(-3), 450 + ex, 100 + ey + self.size / 2, 1500, 1500 + self.size)
            case 6:
                self.ch6.rotate_draw(math.radians(-3), 450 + ex, 100 + ey + self.size / 2, 1500, 1500 + self.size)
            case 7:
                self.ch7.rotate_draw(math.radians(-3), 450 + ex, 100 + ey + self.size / 2, 1500, 1500 + self.size)
            case 8:
                self.ch8.rotate_draw(math.radians(-3), 450 + ex, 100 + ey + self.size / 2, 1500, 1500 + self.size)

        self.gun_image.rotate_draw(math.radians(-3), 456 + ex, 80 + ey + self.size / 2, 1000, 500)

    def update(self):
        pps = game_framework.pps
        self.size = math.sin(self.deg) * 30
        self.deg += pps / 500


class Monsterimage:
    def __init__(self, cursor):
        self.type4 = load_image(type4_directory)
        self.size = 0
        self.deg = 0
        self.cursor = cursor

    def draw(self):
        ex = (WIDTH / 2 - self.cursor.mx) / 10
        ey = (HEIGHT / 2 - self.cursor.my) / 10
        self.type4.clip_composite_draw \
            (2 * 128, 0, 128, 128, math.radians(-3), '', WIDTH - 100 + ex, 50 + ey + self.size / 2, 1500,
             1500 + self.size)

    def update(self):
        pps = game_framework.pps
        self.size = math.sin(self.deg) * 30
        self.deg += pps / 300


class Cursor:
    def __init__(self):
        self.image = load_image(cursor_directory)
        self.mx, self.my = 0, 0

    def draw(self):
        self.image.draw(self.mx + 35, self.my - 35, 70, 70)

    def update(self):
        pass
