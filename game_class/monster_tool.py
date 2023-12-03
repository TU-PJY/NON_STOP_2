from config import *
from game_class_manager.monster_tool_func import *


# 몬스터 스폰 클래스


class Tool:
    def __init__(self, p, weapon, target, mp):
        self.p = p
        self.weapon = weapon
        self.target = target
        self.mp = mp
        self.frame = 0
        self.spawn_time = 1000
        self.spawn_point = 0
        self.spawn_point_right = WIDTH / 2 + 2200  # 초기 몬스터 스폰 위치. 플레이어가 움직이면 그에 따라 업데이트 된다.
        self.spawn_point_left = WIDTH / 2 - 2200
        self.point_dir = 0
        self.type = 0
        self.spawn_enable = True  # 해당 변수가 true일때만 스폰
        self.rounds = 1  # 라운드 수
        self.spawn_remain = 3  # 앞으로 스폰할 몬스터 수, 이 변수와 아래의 변수가 동일하지 않으면 라운드가 넘어가지 않는다.
        self.spawn_num = 0  # 스폰된 몬스터 수
        self.limit = 3  # 첫 라운드는 3마리 제한부터 시작하여, 이후 3마리씩 최대 스폰 수가 증가한다.
        self.kill_count = 3  # 라운드 별 처치 필요 횟수 출력 용, 처치할 때마다 감소

        self.time_reduce = 0  # 라운드가 증가헐수록 몬스터 스폰 간격이 점점 좁아진다.

        self.y, self.speed, self.hp = 0, 0, 0

        self.type2_enable = True
        self.type2_delay = 0

    def draw(self):
        pass

    def update(self):
        if game_framework.MODE == 'play':
            update_spawn_point(self)
            spawn_monster(self)
            update_timer(self)
            update_rounds(self)

    def handle_events(self):
        pass
