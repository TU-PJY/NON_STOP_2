from pico2d import load_image, load_wav

from config import *


def load_file(self):
    from game_class.monster import Monster
    if not Monster.type1:
        Monster.type1 = load_image(type1_directory)
        Monster.type1_damage = load_image(type1_damage_directory)
        Monster.type2 = load_image(type2_directory)
        Monster.type2_damage = load_image(type2_damage_directory)
        Monster.type3 = load_image(type3_directory)
        Monster.type3_damage = load_image(type3_damage_directory)
        Monster.type4 = load_image(type4_directory)
        Monster.type4_damage = load_image(type4_damage_directory)
        Monster.hp_front = load_image(hp_front_directory)
        Monster.hp_back = load_image(hp_back_directory)
        Monster.bow = load_wav(bow_sound_directory)