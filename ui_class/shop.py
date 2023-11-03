from config import *
from pico2d import *


class Shop:
    def __init__(self):
        self.window = load_image(shop_window_directory)
        self.back = load_image(pause_bg_directory)
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.window_y = -500

    def draw(self):
        self.back.draw(self.x, self.y, WIDTH, HEIGHT)
        self.back.opacify(80)
        self.window.draw(self.x, self.window_y, 800, 500)
        pass

    def update(self):
        if self.window_y <= HEIGHT / 2:
            self.window_y += 50
        if self.window_y >= HEIGHT / 2:
            self.window_y = HEIGHT / 2
        pass

    def handle_event(self):
        pass
