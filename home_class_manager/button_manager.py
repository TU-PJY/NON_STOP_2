from pico2d import *
from config import *
from game_work import game_framework
from mods import play_mode


def load_file(self):  # 캐릭터 선택 버튼을 출력하기 위한 이미지 로드
    self.ch1 = load_image(player1_right_image_directory)
    self.ch2 = load_image(player2_right_image_directory)
    self.ch3 = load_image(player3_right_image_directory)
    self.ch4 = load_image(player4_right_image_directory)
    self.ch5 = load_image(player5_right_image_directory)
    self.ch6 = load_image(player6_right_image_directory)
    self.ch7 = load_image(player7_right_image_directory)
    self.ch8 = load_image(player8_right_image_directory)
    self.back_button = load_image(button_page_directory)
    self.back_button_back = load_image(shop_button_directory)

    self.ch_sel = load_image(ch_selected_directory)


def home_draw_button(self):
    self.button1.opacify(self.op1)
    self.button2.opacify(self.op2)
    self.button3.opacify(self.op3)

    self.button1.draw(160, HEIGHT / 2 - 100, 300, 80)
    self.font.draw(50, HEIGHT / 2 - 100, '게임 시작', (255, 255, 255))
    self.button2.draw(160, HEIGHT / 2 - 210, 300, 80)
    self.font.draw(80, HEIGHT / 2 - 210, '캐릭터', (255, 255, 255))
    self.button3.draw(160, HEIGHT / 2 - 320, 300, 80)
    self.font.draw(50, HEIGHT / 2 - 320, '홈 나가기', (255, 255, 255))


def ch_draw_button(self):  # 캐릭터 선택 버튼
    self.button4.draw(100, HEIGHT / 2 + 119, 130, 130)
    self.button4.draw(250, HEIGHT / 2 + 119, 130, 130)
    self.button4.draw(400, HEIGHT / 2 + 119, 130, 130)
    self.button4.draw(550, HEIGHT / 2 + 119, 130, 130)
    self.button4.draw(700, HEIGHT / 2 + 119, 130, 130)
    self.button4.draw(850, HEIGHT / 2 + 119, 130, 130)
    self.button4.draw(1000, HEIGHT / 2 + 119, 130, 130)
    self.button4.draw(1150, HEIGHT / 2 + 119, 130, 130)

    self.back_button_back.opacify(self.op4)
    self.back_button_back.draw(60, 60, 100, 100)

    self.back_button.clip_composite_draw(0, 0, 10, 15, 0, 'h', 60, 60, 80, 80)

    match self.data.ch:
        case 1:
            x = 100
        case 2:
            x = 250
        case 3:
            x = 400
        case 4:
            x = 550
        case 5:
            x = 700
        case 6:
            x = 850
        case 7:
            x = 1000
        case 8:
            x = 1150

    self.ch_sel.draw(x, HEIGHT / 2 + 250, 100, 100)

    self.ch1.clip_composite_draw(0, 56, 128, 128, 0, '', 100, HEIGHT / 2 + 200, 500, 285)
    self.ch2.clip_composite_draw(0, 56, 128, 128, 0, '', 250, HEIGHT / 2 + 200, 500, 285)
    self.ch3.clip_composite_draw(0, 56, 128, 128, 0, '', 400, HEIGHT / 2 + 200, 500, 285)
    self.ch4.clip_composite_draw(0, 56, 128, 128, 0, '', 550, HEIGHT / 2 + 200, 500, 285)
    self.ch5.clip_composite_draw(0, 56, 128, 128, 0, '', 700, HEIGHT / 2 + 200, 500, 285)
    self.ch6.clip_composite_draw(0, 56, 128, 128, 0, '', 850, HEIGHT / 2 + 200, 500, 285)
    self.ch7.clip_composite_draw(0, 56, 128, 128, 0, '', 1000, HEIGHT / 2 + 200, 500, 285)
    self.ch8.clip_composite_draw(0, 56, 128, 128, 0, '', 1150, HEIGHT / 2 + 200, 500, 285)


def ch_update_button(self):
    mx = self.cursor.mx
    my = self.cursor.my
    pps = game_framework.pps

    if 10 <= mx <= 110 and 10 <= my <= 110:
        self.op4 += pps / 50
        if self.op4 > 1:
            self.op4 = 1
    else:
        self.op4 -= pps / 50
        if self.op4 < 0:
            self.op4 = 0

    if self.click:
        mx = self.cursor.mx
        my = self.cursor.my

        if 10 <= mx <= 110 and 10 <= my <= 110:
            self.data.mode = 'home'

        elif 35 <= mx <= 165 and HEIGHT / 2 + 65 <= my <= HEIGHT / 2 + 184:
            self.data.ch = 1
        elif 185 <= mx <= 315 and HEIGHT / 2 + 65 <= my <= HEIGHT / 2 + 184:
            self.data.ch = 2
        elif 335 <= mx <= 465 and HEIGHT / 2 + 65 <= my <= HEIGHT / 2 + 184:
            self.data.ch = 3
        elif 385 <= mx <= 615 and HEIGHT / 2 + 65 <= my <= HEIGHT / 2 + 184:
            self.data.ch = 4
        elif 535 <= mx <= 765 and HEIGHT / 2 + 65 <= my <= HEIGHT / 2 + 184:
            self.data.ch = 5
        elif 685 <= mx <= 915 and HEIGHT / 2 + 65 <= my <= HEIGHT / 2 + 184:
            self.data.ch = 6
        elif 835 <= mx <= 1065 and HEIGHT / 2 + 65 <= my <= HEIGHT / 2 + 184:
            self.data.ch = 7
        elif 985 <= mx <= 1315 and HEIGHT / 2 + 65 <= my <= HEIGHT / 2 + 184:
            self.data.ch = 8

        data = [
            {"ch": self.data.ch}
        ]

        with open('data//ch_data.json', 'w') as f:  # 캐릭터 선택 시 데이터에 저장한다
            json.dump(data, f)


def home_update_button(self):
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
        # 게임 시작
        if 10 < self.cursor.mx < 310 and HEIGHT / 2 - 100 - 40 < self.cursor.my < HEIGHT / 2 - 100 + 40:
            game_framework.MODE = 'play'
            game_framework.change_mode(play_mode)

        # 캐릭터
        if 10 < self.cursor.mx < 310 and HEIGHT / 2 - 210 - 40 < self.cursor.my < HEIGHT / 2 - 210 + 40:
            self.op2 = 0
            self.data.mode = 'ch_mode'
