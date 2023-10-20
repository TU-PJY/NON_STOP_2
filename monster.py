from func.monster_manager import *


class Monster:
    def __init__(self, p):
        load_monster(self)
        self.p = p
        self.list = []
        # 몬스터들의 정보를 담는 리스트, 인덱스 오류 방지를 위한 더미 대이터가 있음
        self.dead_list = []  # 몬스터 시체 정보를 담는 리스트

        self.spawn_point_right = WIDTH / 2 + 2200  # 초기 몬스터 스폰 위치. 플레이어가 움직이면 그에 따라 업데이트 된다.
        self.spawn_point_left = WIDTH / 2 - 2200

        self.spawn_time = 0  # 이 변수가 0이 될 때마다 몬스터가 스폰된다.
        self.type = 0  # 몬스터 타입

        self.x, self.y, self.mv_dir = 0, 0, 0
        self.hp, self.speed = 0, 0
        self.frame, self.frame_delay = 0, 0
        self.attack, self.hit, self.hit_type = False, False, 0
        self.damg = 0  # 대미지를 입는 몬스터의 인덱스

    def draw(self):
        if self.list:
            for i in range(len(self.list) - 1, -1, -1):
                draw_monster(self, i)

    def update(self):
        update_spawn_point(self)
        spawn_monster(self)

        for i in range(len(self.list) - 1, -1, -1):
            move_monster(self, i)
            frame_monster(self, i)
            update_monster_pos(self, i)
            delete_monster(self, i)

    def handle_events(self):
        pass
