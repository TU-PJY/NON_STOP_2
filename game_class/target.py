from class_manager.target_manager import *


# MOUSEBUTTON -> Gun class -> Target class


class Target:
    def __init__(self, p, weapon):
        load_target(self)
        self.p = p
        self.weapon = weapon

        self.dis, self.recoil = 0, 0
        self.dis2 = 0
        self.reduce_delay = 0

        self.tx, self.ty = 0, 0  # 조준점 범위 내에서 랜점으로 생성되는 좌표
        self.target_dot_display_time = 0

    def draw(self):
        if game_framework.MODE == 'play':
            draw_target(self)

    def update(self):
        if game_framework.MODE == 'play':
            make_target_point(self)
            update_target(self)

    def handle_event(self, event):
        pass
