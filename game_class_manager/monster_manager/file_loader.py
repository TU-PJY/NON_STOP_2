from pico2d import *

from config import *


def load_monster(self):
    if self.type == 1:
        self.type1 = load_image(type1_directory)
        self.type1_damage = load_image(type1_damage_directory)
    elif self.type == 2:
        self.type2 = load_image(type2_directory)
        self.type2_damage = load_image(type2_damage_directory)
    elif self.type == 3:
        self.type3 = load_image(type3_directory)
        self.type3_damage = load_image(type3_damage_directory)
    elif self.type == 4:
        self.type4 = load_image(type4_directory)
        self.type4_damage = load_image(type4_damage_directory)

    # 체력바 이미지
    self.hp_back = load_image(hp_back_directory)
    self.hp_front = load_image(hp_front_directory)
