# 맵 관련 함수 모음
from pico2d import *

from config import *
from game_work import game_framework
from mods import play_mode


def load_land(self):
    self.image = load_image(land_image_directory)


def load_wall(self):
    self.image = load_image(wall_image_directory)


def load_background(self):
    self.image = load_image(bg_image_directory)
    self.image_back = load_image(bg_back_image_directory)


def draw_land(self):
    x = self.x + self.p.ex
    y = self.y + self.p.ey
    self.image.draw(x, y, 4096, 512)


def draw_wall(self):
    x1 = self.x1 + self.p.ex
    x2 = self.x2 + self.p.ex
    y = self.y + self.p.ey
    self.image.draw(x1, y, 1280, 1920)
    self.image.draw(x1, y + 1920, 1280, 1920)
    self.image.draw(x1 - 1280, y, 1280, 1920)

    self.image.draw(x2, y, 1280, 1920)
    self.image.draw(x2, y + 1920, 1280, 1920)
    self.image.draw(x2 + 1280, y, 1280, 1920)


def draw_background(self):
    x = self.x + self.p.ex
    y = self.y + self.p.ey
    self.image_back.draw(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
    self.image.draw(x, y, 4096, 1100)


def update_map(self):  # 맵 업데이트
    speed = game_framework.pps * self.p.speed
    if self.p.mv_right:
        speed *= -1
    elif self.p.mv_left:
        speed = speed
    else:
        speed = 0

    if not play_mode.weapon.hit_ground:
        self.x += speed
        self.wall.x1 += speed
        self.wall.x2 += speed
        self.bg.x += speed / 2
        self.playerToWallRight += speed
        self.playerToWallLeft += speed


def restore_map_pos(self):
    speed = game_framework.pps * self.p.speed
    if self.x + 2048 <= self.p.x:  # 맵 끝으로 갈 경우 벽에 막힌다
        self.p.mv_right = False

        self.x += speed  # 플레이어를 벽 위치로 보정한다
        self.wall.x1 += speed
        self.wall.x2 += speed
        self.bg.x += speed / 2
        self.playerToWallRight += speed
        self.playerToWallLeft += speed

        if play_mode.weapon.skill_enable:  # katana 스킬 사용할 경우 스킬 상태 해제
            play_mode.weapon.skill_enable = False
            self.p.speed = self.p.temp_speed
            self.p.rotate = 0

    elif self.x - 2048 >= self.p.x:
        self.p.mv_left = False

        self.x -= speed
        self.wall.x1 -= speed
        self.wall.x2 -= speed
        self.bg.x -= speed / 2
        self.playerToWallRight -= speed
        self.playerToWallLeft -= speed

        if play_mode.weapon.skill_enable and play_mode.weapon.melee == 'KATANA':
            play_mode.weapon.skill_enable = False
            self.p.speed = self.p.temp_speed
            self.p.rotate = 0
