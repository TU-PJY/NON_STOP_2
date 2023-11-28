from pico2d import *

from config import *
from game_work import game_framework
from mods import play_mode


class Button:
    def __init__(self, cursor):
        self.button1 = load_image(ammo_ind_back_directory)
        self.button2 = load_image(ammo_ind_back_directory)
        self.button3 = load_image(ammo_ind_back_directory)
        self.font = load_font(font2_directory, 50)
        self.cursor = cursor
        self.op1, self.op2, self.op3 = 0, 0, 0
        self.click = False

    def draw(self):
        self.button1.opacify(self.op1)
        self.button2.opacify(self.op2)
        self.button3.opacify(self.op3)

        self.button1.draw(160, HEIGHT / 2 - 100, 300, 80)
        self.font.draw(50, HEIGHT / 2 - 100, '게임 시작', (255, 255, 255))
        self.button2.draw(160, HEIGHT / 2 - 210, 300, 80)
        self.font.draw(80, HEIGHT / 2 - 210, '캐릭터', (255, 255, 255))
        self.button3.draw(160, HEIGHT / 2 - 320, 300, 80)
        self.font.draw(50, HEIGHT / 2 - 320, '홈 나가기', (255, 255, 255))

    def update(self):
        pps = game_framework.pps
        if 10 < self.cursor.mx < 310 and HEIGHT / 2 - 100 - 40 < self.cursor.my < HEIGHT / 2 - 100 + 40:
            self.op1 += pps / 50
            if self.op1 > 1:
                self.op1 = 1
        else:
            self.op1 -= pps / 50
            if self.op1 < 0:
                self.op1 = 0

        if 10 < self.cursor.mx < 310 and HEIGHT / 2 - 210 - 40 < self.cursor.my < HEIGHT / 2 - 210 + 40:
            self.op2 += pps / 50
            if self.op2 > 1:
                self.op2 = 1
        else:
            self.op2 -= pps / 50
            if self.op2 < 0:
                self.op2 = 0

        if 10 < self.cursor.mx < 310 and HEIGHT / 2 - 320 - 40 < self.cursor.my < HEIGHT / 2 - 320 + 40:
            self.op3 += pps / 50
            if self.op3 > 1:
                self.op3 = 1
        else:
            self.op3 -= pps / 50
            if self.op3 < 0:
                self.op3 = 0

        if self.click:  # 게임 시작 선택 시 play_mode로 넘어간다.
            if 10 < self.cursor.mx < 310 and HEIGHT / 2 - 100 - 40 < self.cursor.my < HEIGHT / 2 - 100 + 40:
                game_framework.MODE = 'play'
                game_framework.change_mode(play_mode)
            self.click = False


class Background:
    def __init__(self, cursor):
        self.cursor = cursor
        self.back = load_image(bg_back_image_directory)
        self.bg = load_image(bg_image_directory)
        self.logo = load_image(logo_directory)

    def draw(self):
        ex = (WIDTH / 2 - self.cursor.mx) / 30
        ey = (HEIGHT / 2 - self.cursor.my) / 30
        self.back.draw(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
        self.bg.draw(WIDTH / 2 + ex, HEIGHT / 2 - 200 + ey, 4096, 1100)
        self.logo.draw(WIDTH / 2 + ex + 50, HEIGHT - 200 + ey, 1000, 500)

    def update(self):
        pass


class Playerimage:
    def __init__(self, cursor):
        self.image = load_image(player1_right_image_directory)
        self.gun_image = load_image(scar_h_right_directory)
        self.cursor = cursor
        self.size = 0
        self.deg = 0

    def draw(self):
        ex = (WIDTH / 2 - self.cursor.mx) / 10
        ey = (HEIGHT / 2 - self.cursor.my) / 10
        self.image.rotate_draw(math.radians(-3), 450 + ex, 100 + ey + self.size / 2, 1500, 1500 + self.size)
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
