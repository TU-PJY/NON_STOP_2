from pico2d import *
from Env_variable import *
import random


#     x = 0
#     y = 1
#     dir = 2
#     hp = 3
#     spd = 4
#     f = 5
#     fd = 6
#     atk = 7
#     hit = 8
#     type = 9


def load_monster(self):
    self.type_1 = load_image(goblin_directory)


def spawn_monster(self):
    global random_dir
    if self.spawn_time == 0:  # 스폰 타이머가 0이 되면 몬스터를 랜덤으로 스폰한다.
        self.type = 1

        if self.type == 1:  # 일단 몬스터 스폰부터 확인 중
            random_dir = random.randint(0, 1)  # 왼쪽 또는 오른쪽에서 스폰된다
            self.x = self.spawn_point_right if random_dir == 1 else self.spawn_point_left
            self.y, self.mv_dir, self.hp, self.speed = 250, 0, 100, 2
            self.frame = random.randint(0, 1)  # 프레임이 개체마다 다르게 표시된다
            self.frame_delay = random.randint(1, 80)
            self.attack, self.hit = False, False  # 공격 여부

            self.list.append([self.x, self.y, self.mv_dir, self.hp, self.speed, self.frame, self.frame_delay,
                              self.attack, self.hit, self.type])

            self.spawn_time = 1000
            print(self.list, self.number)
    else:
        self.spawn_time -= 1  # 스폰 타이머가 0이 될때까지 감소시킨다.


def draw_monster(self, i):
    global frame, x, y, dir, attack, monster_type
    x, y, dir, frame, attack = self.list[i][0], self.list[i][1], self.list[i][2], self.list[i][5], self.list[i][7]
    monster_type = self.list[i][9]

    if monster_type == 1:
        if dir == 0:
            if attack:  # 공격 상태
                self.type_1.clip_composite_draw(0, 0, 100, 100, 0, '', x + self.p.efx, y + self.p.efy, 250, 250)
            else:
                self.type_1.clip_composite_draw(frame * 100, 0, 100, 100, 0, '', x + self.p.efx, y + self.p.efy,
                                                250, 250)
        elif dir == 1:
            if attack:  # 공격 상태
                self.type_1.clip_composite_draw(0, 0, 100, 100, 0, 'h', x + self.p.efx, y + self.p.efy, 250, 250)
            else:
                self.type_1.clip_composite_draw(frame * 100, 0, 100, 100, 0, 'h', x + self.p.efx, y + self.p.efy,
                                                250, 250)


def frame_monster(self, i):  # 몬스터 애니메이션
    global frame, delay
    frame, delay = self.list[i][5], self.list[i][6]

    if delay == 0:  # delay = 0일 시 다음 프레임 재생
        self.list[i][5], self.list[i][6] = (frame + 1) % 2, 80
    else:
        self.list[i][6] -= 1


def move_monster(self, i):
    global dir, speed, x, y, attack, monster_type
    x, y, dir, speed, monster_type = self.list[i][0], self.list[i][1], self.list[i][2], self.list[i][4], self.list[i][9]
    attack = self.list[i][7]

    self.list[i][2] = 1 if self.p.x >= x else 0  # 몬스터는 항상 플레이어를 바라본다.

    if monster_type == 1:  # type_1
        self.list[i][7] = True if self.p.x - 80 <= x <= self.p.x + 80 else False  # 공격 사거리 안에 들면 이동 중지
        if not attack:
            if dir == 0:  # 아니면 이동
                self.list[i][0] -= speed  # 왼쪽 이동
            else:
                self.list[i][0] += speed  # 오른쪽 이동


def delete_monster(self, i):  # 몬스터 삭제
    if self.list[i][3] <= 0:  # 체력이 0되면
        del self.list[i]  # 삭제


def update_monster_pos(self, i):  # 플레이어 이동 시 출력 위치 업데이트
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
