from class_manager.monster_tool_func import *
from config import *


# 몬스터 스폰 클래스


class Tool:
    def __init__(self, p, weapon, target, mp):
        self.p = p
        self.weapon = weapon
        self.target = target
        self.mp = mp
        self.frame = 0
        self.spawn_time = 0
        self.spawn_point = 0
        self.spawn_point_right = WIDTH / 2 + 2200  # 초기 몬스터 스폰 위치. 플레이어가 움직이면 그에 따라 업데이트 된다.
        self.spawn_point_left = WIDTH / 2 - 2200
        self.point_dir = 0
        self.type = 0

        self.y, self.speed, self.hp = 0, 0, 0

    def draw(self):
        pass

    def update(self):
        if game_framework.MODE == 'play':
            calc_pps()
            update_spawn_point(self)
            spawn_monster(self)
            update_timer(self)

    def handle_events(self):
        pass
