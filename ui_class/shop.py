from config import *
from pico2d import *

from game_work import game_framework


class Shop:
    def __init__(self):
        self.window = load_image(shop_window_directory)
        self.back = load_image(pause_bg_directory)
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.window_y = -500
        self.font = load_font(font_directory, 50)

    def draw(self):
        self.back.draw(self.x, self.y, WIDTH, HEIGHT)
        self.back.opacify(80)
        self.window.draw(self.x, self.window_y, 800, 500)
        self.font.draw(50, HEIGHT - 50, "SHOP", (255, 255, 255))
        pass

    def update(self):
        pps = PPS * game_framework.frame_time
        if self.window_y <= HEIGHT / 2:
            self.window_y += 10 * pps / 4
        if self.window_y >= HEIGHT / 2:
            self.window_y = HEIGHT / 2
        pass

    def handle_event(self):
        pass
