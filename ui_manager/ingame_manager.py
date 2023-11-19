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
    self.grenade_able_icon = load_image(grenable_able_icon_directory)
    self.grenade_unable_icon = load_image(grenable_unable_icon_directory)
    pass


def render_ammo_ind(self):
    pps = game_framework.pps
    # 현재 장탄 수
    cur = self.weapon.cur_ammo

    # 총기 타입에 맞는 탄약 개수 출력
    if self.weapon.gun_type == 'pistol' or self.weapon.gun_type == 'smg':
        num = self.weapon.pistol_ammo
    elif self.weapon.gun_type == 'ar':
        num = self.weapon.ar_ammo
    elif self.weapon.gun_type == 'rifle':
        num = self.weapon.rifle_ammo
    elif self.weapon.gun_type == 'sr':
        num = self.weapon.sniper_ammo

    # 화면 흔들림
    ex = self.p.shake_x + self.p.shake_dx + self.p.shake_ex
    ey = self.p.shake_y - self.p.push_y / 2 + self.p.shake_dy + self.p.shake_ey

    # 코인을 얻을 시 코인 인디케이터가 위로 올라갔다가 내려가는 피드백이 재생된다
    if self.p.get_coin:
        self.get_y = 50
        self.p.get_coin = False
    # 코인을 얻을 시 코인 인디케이터가 위로 올라갔다가 내려가는 피드백이 재생된다
    if self.get_y > 0:
        self.get_y -= pps / 3
        if self.get_y < 0:
            self.get_y = 0

    if game_framework.MODE == 'play':
        if play_mode.weapon.weapon_type == 0:
            # 탄약 인디케이터 배경 출력
            self.back.opacify(400)
            self.back.draw(60 + ex, 20 + ey, 810, 210)

            # 재장전 시 재장전 피드백 표시
            if self.weapon.reloading:
                self.reload_bar.draw(20 + ex, 90 + ey, 700 * (self.weapon.cur_reload_time / self.weapon.reload_time), 120)

            # 탄창에 있는 탄약을 모두 소모 시 재장전이 필요함을 알림
            if self.weapon.cur_ammo > 0:
                self.font.draw(20 + ex, 40 + ey, '%d | %d' % (cur, num), (self.r, self.g, self.b))
            else:
                self.font.draw(20 + ex, 40 + ey, 'R | %d' % num, (self.r, self.g, self.b))

        # 수류탄을 던질 수 있게되면 밝은 아이콘으로 표시, 아니면 어두운 아이콘으로 표시
        if self.weapon.throwable:
            self.grenade_able_icon.draw(500 + ex, 50 + ey, 100, 100)
        else:
            self.font_small.draw(550 + ex, 45 + ey, '%d' % (30 - self.weapon.throw_delay_time), (255, 255, 255))
            self.grenade_unable_icon.draw(500 + ex, 50 + ey, 100, 100)

        # 플레이어 hp 출력
        self.hp_back.draw(WIDTH / 2 + ex, 20 + ey, 410, 30)
        self.font_small.draw(WIDTH / 2 - 200 + ex, 50 + ey, 'HP  %d' % self.p.hp, (255, 255, 255))
        self.hp_player.draw(WIDTH / 2 + ex + (self.p.hp / 200) / 2, 20 + ey, 400 * self.p.hp / 200, 25)

        # 상점 아이콘 출력
        self.font_small.draw(75 + ex, HEIGHT - 40 + ey, 'TAB', (255, 255, 255))
        self.shop_icon.draw(40 + ex, HEIGHT - 40 + ey, 50, 50)

        # 코인 인디케이터 출력
        self.coin_icon.draw(WIDTH / 2 + 250 + ex, 30 + ey + self.get_y, 50, 50)
        self.font_small.draw(WIDTH / 2 + 280 + ex, 30 + ey + self.get_y, '%d' % play_mode.p.coin, (255, 255, 255))
    pass


def update_ammo_ind(self):
    if self.weapon.reload_need:  # 총알을 모두 소모하면 인디케이터가 붉은색으로 표시된다
        self.g, self.b = 0, 0
    else:
        self.r, self.g, self.b = 255, 255, 255
    pass
