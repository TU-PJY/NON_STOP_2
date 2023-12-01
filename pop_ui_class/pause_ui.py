from pico2d import *
from config import *
from game_work import game_framework
from mods import home_mode


class Back:
    def __init__(self):
        self.image = load_image(pause_bg_directory)
        self.op = 0

    def draw(self):
        self.image.opacify(self.op)
        self.image.draw(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)

    def update(self):
        pps = game_framework.pps

        self.op += pps / 400
        if self.op > 0.6:
            self.op = 0.6


class Button:
    def __init__(self, cursor):
        self.button1 = load_image(button_exit_mode_directory)
        self.button2 = load_image(button_exit_mode_directory)
        self.button3 = load_image(button_exit_mode_directory)
        self.font = load_font(font2_directory, 50)

        self.op1, self.op2, self.op3 = 0, 0, 0

        self.cursor = cursor
        self.click = False

    def draw(self):
        self.button1.opacify(self.op1)
        self.button2.opacify(self.op2)
        self.button3.opacify(self.op3)

        self.button1.draw(WIDTH / 2, HEIGHT / 2 + 110, 540, 80)
        self.button2.draw(WIDTH / 2, HEIGHT / 2, 540, 80)
        self.button3.draw(WIDTH / 2, HEIGHT / 2 - 110, 540, 80)

        self.font.draw(WIDTH / 2 - 203, HEIGHT / 2 + 110, '게임으로 돌아가기', (255, 255, 255))
        self.font.draw(WIDTH / 2 - 155, HEIGHT / 2, '홈으로 나가기', (255, 255, 255))
        self.font.draw(WIDTH / 2 - 230, HEIGHT / 2 - 110, '바탕화면으로 나가기', (255, 255, 255))

    def update(self):
        pps = game_framework.pps
        x, y = self.cursor.mx, self.cursor.my

        if WIDTH / 2 - 270 <= x <= WIDTH / 2 + 270 and HEIGHT / 2 + 70 <= y <= HEIGHT / 2 + 150:
            self.op1 += pps / 50
            if self.op1 > 1:
                self.op1 = 1
        else:
            self.op1 -= pps / 50
            if self.op1 < 0:
                self.op1 = 0

        if WIDTH / 2 - 270 <= x <= WIDTH / 2 + 270 and HEIGHT / 2 - 40 <= y <= HEIGHT / 2 + 40:
            self.op2 += pps / 50
            if self.op2 > 1:
                self.op2 = 1
        else:
            self.op2 -= pps / 50
            if self.op2 < 0:
                self.op2 = 0

        if WIDTH / 2 - 270 <= x <= WIDTH / 2 + 270 and HEIGHT / 2 - 150 <= y <= HEIGHT / 2 - 70:
            self.op3 += pps / 50
            if self.op3 > 1:
                self.op3 = 1
        else:
            self.op3 -= pps / 50
            if self.op3 < 0:
                self.op3 = 0

        if self.click:
            # 게임으로 돌아가기
            if WIDTH / 2 - 270 <= x <= WIDTH / 2 + 270 and HEIGHT / 2 + 70 <= y <= HEIGHT / 2 + 150:
                game_framework.MODE = 'play'
                game_framework.pop_mode()
            # 홈으로 나가기
            if WIDTH / 2 - 270 <= x <= WIDTH / 2 + 270 and HEIGHT / 2 - 40 <= y <= HEIGHT / 2 + 40:
                game_framework.MODE = 'home'
                game_framework.change_mode(home_mode)
            # 바탕화면으로 나가기
            if WIDTH / 2 - 270 <= x <= WIDTH / 2 + 270 and HEIGHT / 2 - 150 <= y <= HEIGHT / 2 - 70:
                game_framework.quit()

class Cursor:
    def __init__(self):
        self.image = load_image(cursor_directory)
        self.mx, self.my = 0, 0

    def draw(self):
        self.image.draw(self.mx + 35, self.my - 35, 70, 70)

    def update(self):
        pass
