from game_class.monster import Monster
from config import *
import random
from game_work import game_manager


class Manager:
    def __init__(self, p, weapon, target):
        self.p = p
        self.weapon = weapon
        self.target = target
        self.frame = 0
        self.fdelay = 0
        self.spawn_time = 0
        self.spawn_point = 0
        self.spawn_point_right = WIDTH / 2 + 2100  # 초기 몬스터 스폰 위치. 플레이어가 움직이면 그에 따라 업데이트 된다.
        self.spawn_point_left = WIDTH / 2 - 2100
        self.point_dir = 0
        self.type = 0

        self.y, self.speed, self.hp = 0, 0, 0

    def draw(self):
        pass

    def update(self):
        if self.p.mv_right:
            self.spawn_point_right -= self.p.speed
            self.spawn_point_left -= self.p.speed

        elif self.p.mv_left:
            self.spawn_point_right += self.p.speed
            self.spawn_point_left += self.p.speed

        if self.spawn_time == 0:
            self.point_dir = random.randint(0, 1)
            if self.point_dir == 0:
                self.spawn_point = self.spawn_point_left
            else:
                self.spawn_point = self.spawn_point_right

            self.frame = random.randint(0, 1)
            self.fdelay = random.randint(0, 70)

            self.type = random.randint(1, 2)

            if self.type == 1:
                self.y, self.speed, self.hp = 250, 2, 100

            elif self.type == 2:
                self.y, self.speed, self.hp = 650, 1, 70

            m = Monster\
                (self.p, self.weapon, self.target, self.spawn_point,
                 self.y, self.speed, self.hp, self.frame, self.fdelay, self.type)

            game_manager.add_object(m, 2)
            self.spawn_time = 1000

        elif self.spawn_time > 0:
            self.spawn_time -= 1

    def handle_events(self):
        pass
