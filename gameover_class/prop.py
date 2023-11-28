from pico2d import *
from config import *
from game_work import game_framework, game_manager
import math

from mods import home_mode


class Playerdead:
    def __init__(self):
        self.front = load_image(front_directory)
        self.font = load_font(font_directory, 100)
        self.size = 0

        self.x1 = 0
        self.x2 = WIDTH
        self.acc = 0
        self.delay = 0

        self.front_size = WIDTH / 2

    def draw(self):
        self.front.draw(self.x1 + self.front_size / 2, HEIGHT / 2, self.front_size, HEIGHT)
        self.front.draw(self.x2 - self.front_size / 2, HEIGHT / 2, self.front_size, HEIGHT)

        self.font.draw(self.x1 + self.front_size - 450, HEIGHT / 2, 'GAME', (255, 255, 255))
        self.font.draw(self.x2 - self.front_size + 20, HEIGHT / 2, 'OVER', (255, 255, 255))

    def update(self):
        pps = game_framework.pps
        self.delay += pps / 3

        if self.delay >= 600:
            self.front_size -= self.acc * pps / 4
            self.acc += pps / 100
            if self.front_size < 0:
                game_manager.remove_object(self)

    def handle_event(self):
        pass


class Reward:
    def __init__(self):
        self.back = load_image(reward_bg_directory)
        self.image = load_image(reward_directory)
        self.button = load_image(shop_button_directory)
        self.font = load_font(font2_directory, 60)
        self.mx, self.my = 0, 0
        self.click = False

        self.color = 255


    def draw(self):
        self.back.draw(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
        self.image.draw(WIDTH / 2, HEIGHT - 200, 920, 190)
        self.font.draw(WIDTH / 2 - 220, 200, '홈으로 돌아가기', (255, 255, self.color))

    def update(self):
        pps = game_framework.pps
        if WIDTH / 2 - 230 <= self.mx <= WIDTH / 2 + 220 and 150 <= self.my <= 250:
            self.color -= int(pps) * 2
            if self.color < 0:
                self.color = 0
        else:
            self.color += int(pps) * 2
            if self.color > 255:
                self.color = 255

        if self.click:
            if WIDTH / 2 - 230 <= self.mx <= WIDTH / 2 + 220 and 160 <= self.my <= 240:
                game_framework.change_mode(home_mode)

            else:
                self.click = False

    def handle_event(self):
        pass
