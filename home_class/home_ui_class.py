import random

from pico2d import *

from config import *
from game_work import game_framework, game_manager
from home_class_manager.button_manager import home_update_button, home_draw_button, ch_draw_button, load_file, \
    ch_update_button, exit_draw_button, exit_update_button
from mods import play_mode, home_mode


class Bgm:
    def __init__(self):
        self.sound = load_music(home_bgm_directory)
        self.sound.set_volume(32)
        self.sound.repeat_play()

    def draw(self):
        pass

    def update(self):
        pass


class Data:  # 홈 모드에서 사용되는 데이터를 저장하기 위한 가상 객체
    def __init__(self):
        self.mode = 'title_mode'  # 모드에 따라 보이는 화면이 달라진다.
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

        # 기준 화면 높이: 960px
        self.kx, self.ky = WIDTH / 2 + 300, -500 + (HEIGHT - 960)
        self.kacc = 0
        self.deg, self.pos = 0, 0

        self.button_sound = load_wav(button_click_directory)
        self.ch_sound = load_wav(ch_change_directory)

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
    def __init__(self, data):
        self.image = load_image(cursor_directory)
        self.mx, self.my = 0, 0
        self.data = data

    def draw(self):
        if not self.data.mode == 'loading_mode':
            self.image.draw(self.mx + 35, self.my - 35, 70, 70)

    def update(self):
        pass


class Start:  # 홈모드 -> 플레이 모드 전환 시
    def __init__(self, data):
        self.y1 = HEIGHT + HEIGHT / 2
        self.y2 = - HEIGHT / 2
        self.up = load_image(front_directory)
        self.down = load_image(front_directory)
        self.font = load_font(font_directory, 80)
        self.font2 = load_font(font_directory, 40)
        self.font3 = load_font(font2_directory, 30)
        self.font_out = False
        self.acc = 0
        self.delay = 0
        self.data = data
        self.volume = 32

        self.tip = random.randint(0, 4)  # 랜덤으로 팁을 표시한다

    def draw(self):
        self.up.draw(WIDTH / 2, self.y1, WIDTH, HEIGHT)
        self.down.draw(WIDTH / 2, self.y2, WIDTH, HEIGHT)
        self.font.draw(WIDTH / 2 - 600, self.y1 - HEIGHT / 2 + 90, 'OKAY! LETS GO!', (172, 162, 132))

        match self.tip:
            case 0:
                self.font3.draw(20, self.y2 + HEIGHT / 2 - 30, 'TIP: 근접무기로 적 처치 시 더 많은 코인을 얻을 수 있습니다.', (172, 162, 132))
            case 1:
                self.font3.draw(20, self.y2 + HEIGHT / 2 - 30, 'TIP: 무작정 난사하는 것은 그다지 좋은 전략이 아닙니다.', (172, 162, 132))
            case 2:
                self.font3.draw(20, self.y2 + HEIGHT / 2 - 30, 'TIP: 벽에 기대지 마세요!', (172, 162, 132))
            case 3:
                self.font3.draw(20, self.y2 + HEIGHT / 2 - 30, 'TIP: 적이 코 앞에 있을 때는 근접무기를 휘두르는 것이 더 좋을 수 있습니다.', (172, 162, 132))
            case 4:
                self.font3.draw(20, self.y2 + HEIGHT / 2 - 30, 'TIP: 적들에게 둘러 쌓였을 때 상대하지 않고 옆으로 빠져나가는 것이 더 안전할 수 있습니다.', (172, 162, 132))

        if self.font_out:
            self.font2.draw(20, 50, 'LOADING...', (172, 162, 132))

    def update(self):
        pps = game_framework.pps

        if self.data.mode == 'loading_mode':
            self.volume -= pps / 50  # 브금이 점차 작아진다
            if self.volume <= 0:
                self.volume = 0
            home_mode.bgm.sound.set_volume(int(self.volume))

            self.delay += pps / 4

            # if self.y1 > HEIGHT:
            self.y1 -= self.acc * pps / 4
            self.y2 += self.acc * pps / 4
            self.acc += pps / 100

            if self.y1 < HEIGHT:
                self.y1 = HEIGHT
                self.y2 = 0
                self.acc = self.acc / 2 * -1

            if self.delay >= 550:
                self.font_out = True

            if self.delay >= 600:
                home_mode.bgm.sound.stop()
                game_framework.MODE = 'play'
                game_framework.change_mode(play_mode)


class Start2:  # 플레이 모드 -> 홈 모드 전환 및 게임 시작 시
    def __init__(self):
        self.y1 = HEIGHT
        self.y2 = 0
        self.up = load_image(front_directory)
        self.down = load_image(front_directory)
        self.acc = 0

    def draw(self):
        self.up.draw(WIDTH / 2, self.y1, WIDTH, HEIGHT)
        self.down.draw(WIDTH / 2, self.y2, WIDTH, HEIGHT)

    def update(self):
        pps = game_framework.pps
        self.y1 += self.acc * pps / 4
        self.y2 -= self.acc * pps / 4

        self.acc += pps / 100

        if self.y1 > HEIGHT + HEIGHT / 2:
            game_manager.remove_object(self)


class Start3:  # 스플래시 모드 -> 홈 모드 전환 시
    def __init__(self, data):
        self.data = data
        self.y1 = HEIGHT
        self.y2 = 0
        self.delay = 0
        self.font_delay = 0
        self.bar_delay = 0
        self.bar_on = True
        self.font_on = [False for i in range(5)]
        self.up = load_image(front_directory)
        self.down = load_image(front_directory)
        self.acc = 0
        self.font = load_font(font_directory, 100)
        self.logo = load_image(mata_logo_directory)

        self.bar_x = 150

    def draw(self):
        self.up.draw(WIDTH / 2, self.y1, WIDTH, HEIGHT)
        self.down.draw(WIDTH / 2, self.y2, WIDTH, HEIGHT)

        if self.font_on[0]:
            self.font.draw(150, self.y1 - HEIGHT / 2 + 80, 'M', (172, 162, 132))
            self.bar_x = 260
        if self.font_on[1]:
            self.font.draw(260, self.y1 - HEIGHT / 2 + 80, 'A', (172, 162, 132))
            self.bar_x = 370
        if self.font_on[2]:
            self.font.draw(370, self.y1 - HEIGHT / 2 + 80, 'T', (172, 162, 132))
            self.bar_x = 480
        if self.font_on[3]:
            self.font.draw(480, self.y1 - HEIGHT / 2 + 80, 'A', (172, 162, 132))
            self.bar_x = 590
        if self.font_on[4]:
            self.logo.draw(640, self.y1 - HEIGHT / 2 + 70, 240, 240)
            self.bar_x = 700

        if self.bar_on:
            self.font.draw(self.bar_x, self.y1 - HEIGHT / 2 + 80, '_', (172, 162, 132))

    def update(self):
        pps = game_framework.pps

        self.delay += pps / 4
        self.font_delay += pps / 4

        if self.font_on[4]:
            self.bar_delay += pps / 4

        if self.font_delay >= 100 and not self.font_on[0]:
            self.font_on[0] = True
        if self.font_delay >= 200 and not self.font_on[1]:
            self.font_on[1] = True
        if self.font_delay >= 300 and not self.font_on[2]:
            self.font_on[2] = True
        if self.font_delay >= 400 and not self.font_on[3]:
            self.font_on[3] = True
        if self.font_delay >= 500 and not self.font_on[4]:
            self.font_on[4] = True

        if self.bar_delay >= 100 and not self.bar_on:
            self.bar_on = True
            self.bar_delay = 0

        if self.bar_delay >= 100 and self.bar_on:
            self.bar_on = False
            self.bar_delay = 0

        if self.delay >= 1000:
            self.data.mode = 'home'
            self.y1 += self.acc * pps / 4
            self.y2 -= self.acc * pps / 4

            self.acc += pps / 100

            if self.y1 > HEIGHT + HEIGHT / 2:
                game_manager.remove_object(self)
