from pico2d import *
from config import *
from game_work import game_framework, game_manager
import math


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

    def draw(self):
        self.back.draw(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
        self.image.draw(WIDTH / 2, HEIGHT / 2 + 200, 920, 190)

    def update(self):
        pass

    def handle_event(self):
        pass