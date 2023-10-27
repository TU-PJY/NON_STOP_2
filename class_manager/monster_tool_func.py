from game_class.monster import Monster
from game_work import game_manager
import random


def update_spawn_point(self):  # 스폰 지점 업데이트
    if self.p.mv_right:
        self.spawn_point_right -= self.p.speed
        self.spawn_point_left -= self.p.speed

    elif self.p.mv_left:
        self.spawn_point_right += self.p.speed
        self.spawn_point_left += self.p.speed


def spawn_monster(self):  # 몬스터 스폰
    if self.spawn_time == 0:
        self.point_dir = random.randint(0, 1)
        if self.point_dir == 0:
            self.spawn_point = self.spawn_point_left
        else:
            self.spawn_point = self.spawn_point_right

        self.frame = random.randint(0, 1)
        self.fdelay = random.randint(0, 70)
        self.type = random.randint(1, 3)

        if self.type == 1:
            self.y, self.speed, self.hp = 260, 2, 150

        elif self.type == 2:
            self.y, self.speed, self.hp = 650, 1, 70

        elif self.type == 3:
            self.y, self.speed, self.hp, self.frame = 230, 1, 100, 0

        m = Monster \
            (self.p, self.weapon, self.target, self.mp, self.spawn_point,
             self.y, self.speed, self.hp, self.frame, self.fdelay, self.type)

        game_manager.add_object(m, 2)
        self.spawn_time = 1000


def update_timer(self):  # 스폰 타이머 업데이트
    if self.spawn_time > 0:
        self.spawn_time -= 1