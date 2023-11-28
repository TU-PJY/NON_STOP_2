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
        self.button = load_image(ammo_ind_back_directory)
        self.font = load_font(font2_directory, 60)
        self.mx, self.my = 0, 0
        self.click = False
        self.op = 0

    def draw(self):
        self.back.draw(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
        self.image.draw(WIDTH / 2, HEIGHT - 200, 920, 190)
        self.button.opacify(self.op)
        self.button.draw(WIDTH / 2, 200, 500, 100)
        self.font.draw(WIDTH / 2 - 220, 200, '홈으로 돌아가기', (255, 255, 255))

    def update(self):
        pps = game_framework.pps
        if WIDTH / 2 - 250 < self.mx < WIDTH / 2 + 250 and 150 < self.my < 250:
            self.op += pps / 50
            if self.op > 1:
                self.op = 1
        else:
            self.op -= pps / 50
            if self.op < 0:
                self.op = 0

        if self.click:
            if WIDTH / 2 - 250 < self.mx < WIDTH / 2 + 250 and 150 < self.my < 250:
                game_framework.change_mode(home_mode)

            else:
                self.click = False

    def handle_event(self):
        pass
