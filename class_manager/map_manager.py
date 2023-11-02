# 맵 관련 함수 모음
from pico2d import *
from config import *
from game_work import game_framework


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


def update_map(self, pps):  # 맵 업데이트
    pps = pps * game_framework.frame_time

    if self.x + 2048 <= self.p.x:  # 맵 끝으로 갈 경우 벽에 막힌다
        self.p.mv_right = False

    if self.x - 2048 >= self.p.x:
        self.p.mv_left = False

    if self.p.mv_right:
        pps = pps * -1
    elif self.p.mv_left:
        pps = pps
    else:
        pps = 0

    self.x += pps * self.p.speed * 70
    self.wall.x1 += pps * self.p.speed * 70
    self.wall.x2 += pps * self.p.speed * 70
    self.bg.x += (pps * self.p.speed * 70) / 4
    self.playerToWallRight += pps * self.p.speed * 70
    self.playerToWallLeft += pps * self.p.speed * 70
