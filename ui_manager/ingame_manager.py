from pico2d import *

from config import *
from game_work import game_framework
from mods import play_mode


def load_resource(self):
    self.font = load_font(font_directory, 40)
    self.back = load_image(ammo_ind_back_directory)
    self.reload_bar = load_image(reload_bar_directory)
    pass


def render_ammo_ind(self):
    cur = self.weapon.cur_ammo

    if self.weapon.gun_type == 'pistol' or self.weapon.gun_type == 'smg':
        num = self.weapon.pistol_ammo
    elif self.weapon.gun_type == 'ar':
        num = self.weapon.ar_ammo
    elif self.weapon.gun_type == 'rifle':
        num = self.weapon.rifle_ammo
    elif self.weapon.gun_type == 'sr':
        num = self.weapon.sniper_ammo

    x = 20 + self.p.shake_x + self.p.shake_dx
    y = 40 + self.p.shake_y - self.p.push_y + self.p.shake_dy

    if game_framework.MODE == 'play' and play_mode.weapon.weapon_type == 0:
        self.back.opacify(400)
        self.back.draw\
            (60 + self.p.shake_x + self.p.shake_dx, 20 + self.p.shake_y - self.p.push_y + self.p.shake_dy, 810, 210)

        if self.weapon.reloading:
            self.reload_bar.draw(20, 90, 700 * (self.weapon.cur_reload_time / self.weapon.reload_time), 120)

        if self.weapon.cur_ammo > 0:
            self.font.draw(x, y, '%d | %d' % (cur, num), (self.r, self.g, self.b))
        else:
            self.font.draw(x, y, 'R | %d' % num, (self.r, self.g, self.b))
    pass


def update_ammo_ind(self):
    if self.weapon.reload_need:  # 총알을 모두 소모하면 인디케이터가 붉은색으로 표시된다
        self.g, self.b = 0, 0
    else:
        self.r, self.g, self.b = 255, 255, 255
    pass
