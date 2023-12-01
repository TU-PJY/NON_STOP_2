from pico2d import *

from config import *
from game_work import game_framework, game_manager
from mods import home_mode, pause_mode


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


class Back2:
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


class Button:
    def __init__(self, cursor):
        self.button1 = load_image(button_exit_mode_directory)
        self.button2 = load_image(button_exit_mode_directory)
        self.button3 = load_image(button_exit_mode_directory)

        self.button4 = load_image(button_home_mode_directory)
        self.button5 = load_image(button_home_mode_directory)

        self.warning = load_image(warning_directory)

        self.font = load_font(font2_directory, 50)
        self.font2 = load_font(font2_directory, 40)
        self.font3 = load_font(font2_directory, 50)
        self.font4 = load_font(font_directory, 40)

        self.op1, self.op2, self.op3, self.op4, self.op5 = 0, 0, 0, 0, 0

        self.cursor = cursor
        self.click = False

        self.mode = 'select'

    def draw(self):
        if self.mode == 'select':
            self.button1.opacify(self.op1)
            self.button2.opacify(self.op2)
            self.button3.opacify(self.op3)

            self.button1.draw(WIDTH / 2, HEIGHT / 2 + 110, 540, 80)
            self.button2.draw(WIDTH / 2, HEIGHT / 2, 540, 80)
            self.button3.draw(WIDTH / 2, HEIGHT / 2 - 110, 540, 80)

            self.font.draw(WIDTH / 2 - 203, HEIGHT / 2 + 110, '게임으로 돌아가기', (255, 255, 255))
            self.font.draw(WIDTH / 2 - 155, HEIGHT / 2, '홈으로 나가기', (255, 255, 255))
            self.font.draw(WIDTH / 2 - 230, HEIGHT / 2 - 110, '바탕화면으로 나가기', (255, 255, 255))

        elif self.mode == 'exit_to_home' or self.mode == 'exit_to_desktop':
            self.button4.opacify(self.op4)
            self.button5.opacify(self.op5)

            self.button4.draw(WIDTH / 2 - 170, HEIGHT / 2 - 90, 300, 80)
            self.button5.draw(WIDTH / 2 + 170, HEIGHT / 2 - 90, 300, 80)

            self.font4.draw(WIDTH / 2 - 210, HEIGHT / 2 - 90, 'NO', (255, 255, 255))
            self.font4.draw(WIDTH / 2 + 105, HEIGHT / 2 - 90, 'YES', (255, 255, 255))

            if self.mode == 'exit_to_home':
                self.warning.draw(WIDTH / 2, HEIGHT / 2 + 200, 210, 180)
                self.font2.draw(WIDTH / 2 - 290, HEIGHT / 2 + 80, '모든 진행 상황이 초기화 됩니다.', (255, 255, 255))
                self.font2.draw(WIDTH / 2 - 290, HEIGHT / 2 - 20, '계속하시겠습니까?', (255, 255, 255))

            if self.mode == 'exit_to_desktop':
                self.warning.draw(WIDTH / 2, HEIGHT / 2 + 250, 210, 180)
                self.font2.draw(WIDTH / 2 - 290, HEIGHT / 2 + 130, '모든 진행 상황이 초기화 되며,', (255, 255, 255))
                self.font2.draw(WIDTH / 2 - 290, HEIGHT / 2 + 80, '게임을 종료합니다.', (255, 255, 255))
                self.font2.draw(WIDTH / 2 - 290, HEIGHT / 2 - 20, '계속하시겠습니까?', (255, 255, 255))

    def update(self):
        pps = game_framework.pps
        x, y = self.cursor.mx, self.cursor.my

        if self.mode == 'select':
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
                    bg = Back2()
                    game_manager.add_object(bg, 7)
                    game_framework.MODE = 'play'
                    game_framework.pop_mode()
                # 홈으로 나가기
                if WIDTH / 2 - 270 <= x <= WIDTH / 2 + 270 and HEIGHT / 2 - 40 <= y <= HEIGHT / 2 + 40:
                    self.mode = 'exit_to_home'
                    self.op2 = 0
                # 바탕화면으로 나가기
                if WIDTH / 2 - 270 <= x <= WIDTH / 2 + 270 and HEIGHT / 2 - 150 <= y <= HEIGHT / 2 - 70:
                    self.mode = 'exit_to_desktop'
                    self.op3 = 0

        elif self.mode == 'exit_to_home' or self.mode == 'exit_to_desktop':
            if WIDTH / 2 - 320 <= x <= WIDTH / 2 - 20 and HEIGHT / 2 - 130 <= y <= HEIGHT / 2 - 50:
                self.op4 += pps / 50
                if self.op4 > 1:
                    self.op4 = 1
            else:
                self.op4 -= pps / 50
                if self.op4 < 0:
                    self.op4 = 0

            if WIDTH / 2 + 20 <= x <= WIDTH / 2 + 320 and HEIGHT / 2 - 130 <= y <= HEIGHT / 2 - 50:
                self.op5 += pps / 50
                if self.op5 > 1:
                    self.op5 = 1
            else:
                self.op5 -= pps / 50
                if self.op5 < 0:
                    self.op5 = 0

            if self.click:
                if self.mode == 'exit_to_home':
                    # NO
                    if WIDTH / 2 - 320 <= x <= WIDTH / 2 - 20 and HEIGHT / 2 - 130 <= y <= HEIGHT / 2 - 50:
                        self.op4 = 0
                        self.mode = 'select'
                    # YES
                    if WIDTH / 2 + 20 <= x <= WIDTH / 2 + 320 and HEIGHT / 2 - 130 <= y <= HEIGHT / 2 - 50:
                        game_framework.MODE = 'home'
                        self.mode = 'none'
                        end = End()
                        game_manager.add_object(end, 7)

                elif self.mode == 'exit_to_desktop':
                    # NO
                    if WIDTH / 2 - 320 <= x <= WIDTH / 2 - 20 and HEIGHT / 2 - 130 <= y <= HEIGHT / 2 - 50:
                        self.op4 = 0
                        self.mode = 'select'
                    # YES
                    if WIDTH / 2 + 20 <= x <= WIDTH / 2 + 320 and HEIGHT / 2 - 130 <= y <= HEIGHT / 2 - 50:
                        game_framework.quit()

        self.click = False


class Cursor:
    def __init__(self):
        self.image = load_image(cursor_directory)
        self.mx, self.my = 0, 0

    def draw(self):
        if not pause_mode.button.mode == 'none':
            self.image.draw(self.mx + 35, self.my - 35, 70, 70)

    def update(self):
        pass


class End:
    def __init__(self):
        self.y1 = HEIGHT + HEIGHT / 2
        self.y2 = - HEIGHT / 2
        self.up = load_image(front_directory)
        self.down = load_image(front_directory)
        self.font = load_font(font_directory, 80)
        self.font2 = load_font(font_directory, 40)
        self.font_out = False
        self.acc = 0
        self.delay = 0

    def draw(self):
        self.up.draw(WIDTH / 2, self.y1, WIDTH, HEIGHT)
        self.down.draw(WIDTH / 2, self.y2, WIDTH, HEIGHT)
        self.font.draw(50, self.y1 - HEIGHT / 2 + 90, 'BYE BYE', (255, 255, 255))

    def update(self):
        pps = game_framework.pps
        self.delay += pps / 4

        self.y1 -= self.acc * pps / 4
        self.y2 += self.acc * pps / 4
        self.acc += pps / 100

        if self.y1 < HEIGHT:
            self.y1 = HEIGHT
            self.y2 = 0
            self.acc = self.acc / 2 * -1

        if self.delay >= 550:
            game_framework.MODE = 'home'
            game_framework.change_mode(home_mode)
