from pop_ui_class_manager.ingame_manager import *


class Ingame:
    def __init__(self, weapon, p):
        self.weapon = weapon
        self.p = p
        self.x = 0
        self.y = 0
        self.r = 255  # 폰트 색상 rgb
        self.g = 255
        self.b = 255

        self.rg, self.rb = 255, 255  # 라운드 수 색상
        load_resource(self)

        self.get_y = 0  # 코인 획득 피드백을 위한 추가 좌표

        self.ky = 0  # 몬스터 처치 시 피드백 재생

    def update(self):
        update_ammo_ind(self)
        update_round_ind(self)

    def draw(self):
        render_ingame_ui(self)

    def handle_event(self):
        pass
