from pico2d import *

from config import *
from game_work import game_framework
from mods import play_mode


def load_resource(self):
    self.font = load_font(font_directory, 40)
    self.font_small = load_font(font_directory, 20)
    self.back = load_image(ammo_ind_back_directory)
    self.reload_bar = load_image(reload_bar_directory)
    self.hp_back = load_image(hp_back_directory)
    self.hp_player = load_image(hp_player_directory)
    self.shop_icon = load_image(shop_icon_directory)
    self.coin_icon = load_image(coin_icon_directory)
    pass


def render_ammo_ind(self):
    pps = game_framework.pps

    cur = self.weapon.cur_ammo

    if self.weapon.gun_type == 'pistol' or self.weapon.gun_type == 'smg':
        num = self.weapon.pistol_ammo
    elif self.weapon.gun_type == 'ar':
        num = self.weapon.ar_ammo
    elif self.weapon.gun_type == 'rifle':
        num = self.weapon.rifle_ammo
    elif self.weapon.gun_type == 'sr':
        num = self.weapon.sniper_ammo

    x = 20
    y = 40

    ex = self.p.shake_x + self.p.shake_dx
    ey = self.p.shake_y - self.p.push_y / 2 + self.p.shake_dy
    get_y = 0

    if self.p.get_coin:
        self.get_y = 50
        self.p.get_coin = False

    if self.get_y > 0:
        self.get_y -= pps / 3
        if self.get_y < 0:
            self.get_y = 0

    if game_framework.MODE == 'play':
        if play_mode.weapon.weapon_type == 0:
            self.back.opacify(400)
            self.back.draw(60 + ex, 20 + ey, 810, 210)

            if self.weapon.reloading:
                self.reload_bar.draw(20 + ex, 90 + ey, 700 * (self.weapon.cur_reload_time / self.weapon.reload_time), 120)

            if self.weapon.cur_ammo > 0:
                self.font.draw(x + ex, y + ey, '%d | %d' % (cur, num), (self.r, self.g, self.b))
            else:
                self.font.draw(x + ex, y + ey, 'R | %d' % num, (self.r, self.g, self.b))

        self.hp_back.draw(WIDTH / 2 + ex, 20 + ey, 410, 30)
        self.font_small.draw(WIDTH / 2 - 200 + ex, 50 + ey, 'HP  %d' % self.p.hp, (255, 255, 255))
        self.hp_player.draw(WIDTH / 2 + ex + (self.p.hp / 200) / 2, 20 + ey, 400 * self.p.hp / 200, 25)

        self.font_small.draw(75 + ex, HEIGHT - 40 + ey, 'TAB', (255, 255, 255))
        self.shop_icon.draw(40 + ex, HEIGHT - 40 + ey, 50, 50)

        self.coin_icon.draw(WIDTH / 2 + 250 + ex, 30 + ey + self.get_y, 50, 50)
        self.font_small.draw(WIDTH / 2 + 280 + ex, 30 + ey + self.get_y, '%d' % play_mode.p.coin, (255, 255, 255))
    pass


def update_ammo_ind(self):
    if self.weapon.reload_need:  # 총알을 모두 소모하면 인디케이터가 붉은색으로 표시된다
        self.g, self.b = 0, 0
    else:
        self.r, self.g, self.b = 255, 255, 255
    pass
