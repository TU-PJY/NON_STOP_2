from pico2d import *
from Env_variable import *
import random
from enum import Enum


class d(Enum):  # 열겨형
    x = 0
    y = 1
    dir = 2
    hp = 3
    spd = 4
    f = 5
    fd = 6
    atk = 7
    hit = 8
    type = 9


def load_monster(self):
    self.goblin = load_image(goblin_directory)


def spawn_monster(self):
    global random_dir
    if self.spawn_time == 0:  # 스폰 타이머가 0이 되면 몬스터를 랜덤으로 스폰한다.
        self.type = 1

        if self.type == 1:  # 일단 몬스터 스폰부터 확인 중
            random_dir = random.randint(0, 1)  # 왼쪽 또는 오른쪽에서 스폰된다
            if random_dir == 1:
                self.x = self.spawn_point_right
            else:
                self.x = self.spawn_point_left

            self.y = 240
            self.mv_dir = 0
            self.hp = 100
            self.speed = 2
            self.frame = random.randint(0, 1)  # 프레임이 개체마다 다르게 표시된다
            self.frame_delay = random.randint(1, 80)

            self.attack = False  # 공격 여부
            self.hit = False

            self.list.append([self.x, self.y, self.mv_dir, self.hp,
                              self.speed, self.frame, self.frame_delay, self.attack, self.hit, self.type])

            self.number += 1
            self.spawn_time = 1000
            self.list_exist = True
    else:
        self.spawn_time -= 1  # 스폰 타이머가 0이 될때까지 감소시킨다.


def draw_monster(self, i):
    if not self.list_exist:
        return

    if self.list[i][d.type.value] == 1:
        if self.list[i][d.dir.value] == 0:
            if self.list[i][d.atk.value]:  # 공격 상태
                self.goblin.clip_composite_draw(self.list[i][d.f.value] * 100, 0, 100, 100, 0, '',
                                                self.list[i][d.x.value] + self.p.efx,
                                                self.list[i][d.y.value] + self.p.efy, 250, 250)
            else:
                self.goblin.clip_composite_draw(0, 0, 100, 100, 0, '',
                                                self.list[i][d.x.value] + self.p.efx,
                                                self.list[i][d.y.value] + self.p.efy, 250, 250)
        else:
            if self.list[i][d.dir.value]:  # 공격 상태
                self.goblin.clip_composite_draw(self.list[i][d.f.value] * 100, 0, 100, 100, 0, 'h',
                                                self.list[i][d.x.value] + self.p.efx,
                                                self.list[i][d.y.value] + self.p.efy, 250, 250)
            else:
                self.goblin.clip_composite_draw(0, 0, 100, 100, 0, 'h',
                                                self.list[i][d.x.value] + self.p.efx,
                                                self.list[i][d.y.value] + self.p.efy, 250, 250)


def frame_monster(self, i):  # 몬스터 애니메이션
    if not self.list_exist:
        return

    if self.list[i][d.fd.value] == 0:
        self.list[i][d.f.value] = (self.list[i][d.f.value] + 1) % 2
        self.list[i][d.fd.value] = 80
    else:
        self.list[i][d.fd.value] -= 1


def move_monster(self, i):
    if not self.list_exist:
        return

    if self.p.x >= self.list[i][d.x.value]:  # dir
        self.list[i][d.dir.value] = 1
    else:
        self.list[i][d.dir.value] = 0

    if not self.p.x - 80 <= self.list[i][d.x.value] <= self.p.x + 80:  # 공격 사거리 안에 들면 이동을 멈추고 공격한다
        self.list[i][d.atk.value] = False  # 몬스터 공격 여부, True일 시 공격한다.
        if self.list[i][d.dir.value] == 0:  # move
            self.list[i][d.x.value] -= self.list[i][d.spd.value]  # 왼쪽 이동
        else:
            self.list[i][d.x.value] += self.list[i][d.spd.value]  # 오른쪽 이동
    else:
        self.list[i][d.atk.value] = True


def delete_monster(self):  # 몬스터 삭제
    if self.list[self.hit_idx][d.hp.value] <= 0:
        del self.list[self.hit_idx]
        self.number -= 1
        if self.number == 0:
            self.list_exist = False


def update_monster_pos(self, i):  # 플레이어 이동 시 출력 위치 업데이트
    if not self.list_exist:
        return

    if self.p.mv_right:  # monster pos update
        self.list[i][d.x.value] -= self.p.speed
    elif self.p.mv_left:
        self.list[i][d.x.value] += self.p.speed


def update_spawn_point(self):
    if self.p.mv_right:  # 플레이어가 움직이면 스폰 포인트 위치를 업데이트 해야한다.
        self.spawn_point_right -= self.p.speed
        self.spawn_point_left -= self.p.speed

    elif self.p.mv_left:
        self.spawn_point_right += self.p.speed
        self.spawn_point_left += self.p.speed
