import random

from config import *
from game_class.monster import Monster
from game_work import game_manager, game_framework
from mods import play_mode


def update_spawn_point(self):  # 스폰 지점 업데이트
    speed = game_framework.pps * self.p.speed
    if self.p.mv_right:
        self.spawn_point_right -= speed
        self.spawn_point_left -= speed

    elif self.p.mv_left:
        self.spawn_point_right += speed
        self.spawn_point_left += speed


def spawn_monster(self):  # 몬스터 스폰
    if self.spawn_enable:
        if self.spawn_time <= 0:
            self.point_dir = random.randint(0, 1)
            if self.point_dir == 0:
                self.spawn_point = self.spawn_point_left
            else:
                self.spawn_point = self.spawn_point_right

            self.frame = random.randint(0, 1)
            self.frame = self.frame + APT * FPA * game_framework.frame_time

            if self.rounds < 5:  # 라운드가 올라갈 수록 몬스터가 다양해진다
                self.type = 1

            elif 5 <= self.rounds <= 9:
                if self.type2_enable:
                    self.type = random.randint(1, 2)
                    self.type2_delay += 1
                else:
                    self.type = 1
                    self.type2_delay -= 1
                    if self.type2_delay == 0:
                        self.type2_enable = True

            elif 10 <= self.rounds <= 14:
                if self.type2_enable:
                    self.type = random.randint(1, 3)
                    self.type2_delay += 1
                else:
                    rand = [1, 3]
                    self.type = random.choice(rand)
                    self.type2_delay -= 1
                    if self.type2_delay == 0:
                        self.type2_enable = True

            elif 15 <= self.rounds:
                if self.type2_enable:
                    self.type = random.randint(1, 4)
                    self.type2_delay += 1
                else:
                    rand = [1, 3, 4]
                    self.type = random.choice(rand)
                    self.type2_delay -= 1
                    if self.type2_delay == 0:  # 스폰 제한 3회를 넘기면 type2를 다시 스폰할 수 있게 된다
                        self.type2_enable = True

            if self.type2_delay == 3:  # type2를 3번 스폰하면 다음 3회 스폰 동안에는 스폰을 제한한다
                self.type2_enable = False

            match self.type:
                case 1:
                    self.y, self.speed, self.hp = 260, 1.5, 200
                case 2:
                    self.y, self.speed, self.hp = 670, 1.1, 120
                case 3:
                    self.y, self.speed, self.hp, self.frame = 230, 0.9, 180, 0
                case 4:
                    self.y, self.speed, self.hp = 240, 0.5, 150

            m = Monster \
                (self.p, self.weapon, self.target, self.mp, self.spawn_point,
                 self.y, self.speed, self.hp, self.frame, self.type)

            game_manager.add_collision_pair('player:monster', None, m)
            game_manager.add_collision_pair('weapon:monster', None, m)
            game_manager.add_collision_pair('bullet:monster', None, m)
            game_manager.add_collision_pair('grenade:monster', None, m)
            game_manager.add_object(m, 2)
            self.spawn_num += 1
            self.spawn_remain -= 1
            if self.spawn_remain == 0:
                self.spawn_enable = False

            self.type = 0
            self.spawn_time = 800 - self.time_reduce  # 다음 스폰 간격 지정


def update_timer(self):  # 스폰 타이머 업데이트
    pps = game_framework.pps
    if self.spawn_time > 0:
        self.spawn_time -= pps / 3


def update_rounds(self):
    if not self.spawn_enable:
        if self.spawn_num == 0 and self.spawn_remain == 0:  # 둘 다 0이 되면
            play_mode.ig.rg = 0  # 라운드 인디케이터 색이 빨간색으로 변한다
            play_mode.ig.rb = 0
            self.rounds += 1  # 라운드 증가
            self.limit += 3  # 스폰 제한 횟수 3씩 증가
            self.kill_count = self.limit
            self.spawn_remain = self.limit  # 앞으로 스폰할 몬스터 수 갱신
            self.spawn_time = 1500  # 매 라운드 시작 시 어느 정도의 시간을 두고 스폰 시작
            if self.time_reduce < 690:  # 최소 스폰 간격은 100
                self.time_reduce += 15  # 매 라운드마다 스폰 간격이 15씩 줄어든다
            self.spawn_enable = True  # 다음 라운드로 넘어가 스폰을 다시 시작한다.

