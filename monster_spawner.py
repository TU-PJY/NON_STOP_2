import target
import weapon
from monster import Monster
from Env_variable import *
import random
import game_manager


class Manager:
    def __init__(self, p, weapon, target):
        self.p = p
        self.weapon = weapon
        self.target = target
        self.spawn_time = 0
        self.spawn_point = 0
        self.spawn_point_right = WIDTH / 2 + 2200  # 초기 몬스터 스폰 위치. 플레이어가 움직이면 그에 따라 업데이트 된다.
        self.spawn_point_left = WIDTH / 2 - 2200
        self.point_dir = 0
        self.random_type = 0

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
                m = Monster(self.p, weapon, target, self.spawn_point, 250, 2, 100, 1)
            else:
                self.spawn_point = self.spawn_point_right
                m = Monster(self.p, weapon, target, self.spawn_point, 250, 2, 100, 1)

            game_manager.add_object(m, 2)
            self.spawn_time = 1000

        elif self.spawn_time > 0:
            self.spawn_time -= 1

    def handle_events(self):
        pass
