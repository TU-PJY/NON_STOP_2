from pico2d import *
from Env_variable import *
import random


def load_monster(self):
    self.goblin = load_image(goblin_directory)


def draw_monster(self):
    for i in range(self.number):
        if self.list[i][2] == 0:
            if self.list[i][7]:
                self.goblin.clip_composite_draw(self.list[i][5] * 100, 0, 100, 100, 0, '',
                                                self.list[i][0] + self.p.efx, self.list[i][1] + self.p.efy, 200, 200)
            else:
                self.goblin.clip_composite_draw(0, 0, 100, 100, 0, '',
                                                self.list[i][0] + self.p.efx, self.list[i][1] + self.p.efy, 200, 200)
        else:
            if self.list[i][7]:
                self.goblin.clip_composite_draw(self.list[i][5] * 100, 0, 100, 100, 0, 'h',
                                                self.list[i][0] + self.p.efx, self.list[i][1] + self.p.efy, 200, 200)
            else:
                self.goblin.clip_composite_draw(0, 0, 100, 100, 0, 'h',
                                                self.list[i][0] + self.p.efx, self.list[i][1] + self.p.efy, 200, 200)


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
            self.move = True  # 이동 여부

            self.list.append([self.x, self.y, self.mv_dir, self.hp, self.speed, self.frame, self.frame_delay, self.move])
            self.number += 1
            self.spawn_time = 1000

        self.list_exist = True  # 몬스터가 생성되었으므로 다시 업데이트를 진행한다.

    else:
        self.spawn_time -= 1  # 스폰 타이머가 0이 될때까지 감소시킨다.


# [i][0] = x
# [i][1] = y
# [i][2] = mv_dir
# [i][3] = hp
# [i][4] = speed
# [i][5] = frame
# [i][6] = frame_delay
# [i][7] = move


def update_monster(self):
    if self.list_exist:
        for i in range(self.number):
            if self.list[i][3] <= 0:  # hp가 0이되면 죽는다
                del self.list[i]
                self.number -= 1
            if self.number == 0:  # 몬스터 수가 0이 되면 더 이상 업데이트 하지 않는다.
                self.list_exist = False
                break

            if self.p.x >= self.list[i][0]:  # mv_dir
                self.list[i][2] = 1
            else:
                self.list[i][2] = 0

            if not self.p.x - 80 <= self.list[i][0] <= self.p.x + 80:  # 공격 사거리 안에 들면 이동을 멈추고 공격한다
                self.list[i][7] = True
                if self.list[i][2] == 0:  # move
                    self.list[i][0] -= self.list[i][4]
                else:
                    self.list[i][0] += self.list[i][4]
            else:
                self.list[i][7] = False

            if self.list[i][6] == 0:  # frame_delay, frame
                self.list[i][5] = (self.list[i][5] + 1) % 2
                self.list[i][6] = 80
            else:
                self.list[i][6] -= 1

            if self.p.mv_right:  # monster pos update
                self.list[i][0] -= self.p.speed
            elif self.p.mv_left:
                self.list[i][0] += self.p.speed


def update_spawn_point(self):
    if self.p.mv_right:  # 플레이어가 움직이면 스폰 포인트 위치를 업데이트 해야한다.
        self.spawn_point_right -= self.p.speed
        self.spawn_point_left -= self.p.speed

    elif self.p.mv_left:
        self.spawn_point_right += self.p.speed
        self.spawn_point_left += self.p.speed
