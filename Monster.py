from Func.Monster_func import *


class Monster:
    def __init__(self, p, target):
        load_monster(self)
        self.p = p
        self.target = target
        self.list = []  # 몬스터들의 정보를 담는 리스트
        self.dead_list = []  # 몬스터 시체 정보를 담는 리스트

        self.spawn_point_right = WIDTH / 2 + 2200  # 초기 몬스터 스폰 위치. 플레이어가 움직이면 그에 따라 업데이트 된다.
        self.spawn_point_left = WIDTH / 2 - 2200

        self.number = 0  # 몬스터 수
        self.spawn_time = 0  # 이 변수가 0이 될 때마다 몬스터가 스폰된다.

        self.x = 0
        self.y = 0
        self.mv_dir = 0
        self.hp = 0
        self.speed = 0
        self.frame = 0
        self.frame_delay = 0
        self.move = False

        self.list_exist = False

    def draw(self):
        draw_monster(self)

    def update(self):
        spawn_monster(self)
        update_spawn_point(self)
        update_monster(self)

    def handle_events(self):
        pass



