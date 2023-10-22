# 맵 관련 함수 모음
from pico2d import *
from game_main.config import *


def load_land(self):
    self.image = load_image(land_image_directory)


def load_wall(self):
    self.image = load_image(wall_image_directory)


def load_background(self):
    self.image = load_image(bg_image_directory)
    self.image_back = load_image(bg_back_image_directory)


def draw_land(self):
    self.image.draw(self.x + self.p.efx, self.y + self.p.efy, 4096, 512)


def draw_wall(self):
    self.image.draw(self.x1 + self.p.efx, self.y + self.p.efy, 1280, 1920)
    self.image.draw(self.x2 + self.p.efx, self.y + self.p.efy, 1280, 1920)


def draw_background(self):
    self.image_back.draw(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
    self.image.draw(self.x + self.p.efx, self.y + self.p.efy, 4096, 1100)


def update_land(self):  # 이 함수에서 나머지 맵 객체의 업데이트를 결정한다.
    if self.p.mv_right:
        self.x -= self.p.speed
        if self.x + 2048 <= WIDTH / 2:
            self.p.mv_right = False
            self.x += self.p.speed

    elif self.p.mv_left:
        self.x += self.p.speed
        if self.x - 2048 >= WIDTH / 2:
            self.p.mv_left = False
            self.x -= self.p.speed

    self.p.p_to_wall_right = self.x + 2048
    self.p.p_to_wall_left = self.x - 2048


def update_wall(self):
    if self.p.mv_right:
        self.x1 -= self.p.speed
        self.x2 -= self.p.speed

    elif self.p.mv_left:
        self.x1 += self.p.speed
        self.x2 += self.p.speed


def update_background(self):
    if self.p.mv_right:
        self.x -= self.p.speed / 4

    elif self.p.mv_left:
        self.x += self.p.speed / 4
