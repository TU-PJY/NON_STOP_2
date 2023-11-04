import random

from config import *
from game_class.monster import Monster
from game_work import game_manager, game_framework


def update_spawn_point(self):  # 스폰 지점 업데이트
    pps = PPS * game_framework.frame_time
    if self.p.mv_right:
        self.spawn_point_right -= self.p.speed * pps / 4
        self.spawn_point_left -= self.p.speed * pps / 4

    elif self.p.mv_left:
        self.spawn_point_right += self.p.speed * pps / 4
        self.spawn_point_left += self.p.speed * pps / 4


def spawn_monster(self):  # 몬스터 스폰
    if self.spawn_time <= 0:
        self.point_dir = random.randint(0, 1)
        if self.point_dir == 0:
            self.spawn_point = self.spawn_point_left
        else:
            self.spawn_point = self.spawn_point_right

        self.frame = random.randint(0, 1)
        self.frame = self.frame + APT * FPA * game_framework.frame_time
        self.type = random.randint(1, 4)

        if self.type == 1:
            self.y, self.speed, self.hp = 260, 2, 200

        elif self.type == 2:
            self.y, self.speed, self.hp = 670, 1, 180

        elif self.type == 3:
            self.y, self.speed, self.hp, self.frame = 230, 1, 150, 0

        elif self.type == 4:
            self.y, self.speed, self.hp = 240, 0.5, 130

        m = Monster \
            (self.p, self.weapon, self.target, self.mp, self.spawn_point,
             self.y, self.speed, self.hp, self.frame, self.type)

        game_manager.add_object(m, 2)
        self.spawn_time = 1500


def update_timer(self):  # 스폰 타이머 업데이트
    pps = PPS * game_framework.frame_time
    if self.spawn_time > 0:
        self.spawn_time -= pps / 3
