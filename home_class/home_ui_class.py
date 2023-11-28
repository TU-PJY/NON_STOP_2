from pico2d import *
from config import *
from game_work import game_framework


class Button:
    def __init__(self):
        self.button1 = load_image(ammo_ind_back_directory)
        self.button2 = load_image(ammo_ind_back_directory)
        self.button3 = load_image(ammo_ind_back_directory)
        self.mx, self.my = 0, 0
        self.op1, self.op2, self.op3 = 0, 0, 0
        self.click = False

    def draw(self):
        self.button1.opacify(self.op1)
        self.button2.opacify(self.op2)
        self.button3.opacify(self.op3)

        self.button1.draw(160, HEIGHT / 2 - 100, 300, 80)
        self.button2.draw(160, HEIGHT / 2 - 210, 300, 80)
        self.button3.draw(160, HEIGHT / 2 - 320, 300, 80)

    def update(self):
        pps = game_framework.pps
        if 10 < self.mx < 310 and HEIGHT / 2 - 100 - 40 < self.my < HEIGHT / 2 - 100 + 40:
            self.op1 += pps / 50
            if self.op1 > 1:
                self.op1 = 1
        else:
            self.op1 -= pps / 50
            if self.op1 < 0:
                self.op1 = 0

        if 10 < self.mx < 310 and HEIGHT / 2 - 210 - 40 < self.my < HEIGHT / 2 - 210 + 40:
            self.op2 += pps / 50
            if self.op2 > 1:
                self.op2 = 1
        else:
            self.op2 -= pps / 50
            if self.op2 < 0:
                self.op2 = 0

        if 10 < self.mx < 310 and HEIGHT / 2 - 320 - 40 < self.my < HEIGHT / 2 - 320 + 40:
            self.op3 += pps / 50
            if self.op3 > 1:
                self.op3 = 1
        else:
            self.op3 -= pps / 50
            if self.op3 < 0:
                self.op3 = 0

    def handle_event(self):
        pass
