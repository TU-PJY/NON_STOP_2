from pico2d import *

from config import *
from game_work import game_framework
from mods import play_mode


def load_resource(self):
    self.font = load_font(font_directory, 40)
    self.font_small = load_font(font_directory, 20)
    self.font_mini = load_font(font_directory, 15)
    self.back = load_image(ammo_ind_back_directory)
    self.reload_bar = load_image(reload_bar_directory)
    self.hp_back = load_image(hp_back_directory)
    self.hp_player = load_image(hp_player_directory)
    self.shop_icon = load_image(shop_icon_directory)
    self.coin_icon = load_image(coin_icon_directory)
    self.grenade_able_icon = load_image(grenable_able_icon_directory)
    self.grenade_unable_icon = load_image(grenable_unable_icon_directory)
    self.axe_image = load_image(axe_directory)
    self.katana_image = load_image(katana_directory)
    self.rapier_image = load_image(rapier_directory)
    self.knife_image = load_image(knife_right_directory)
    self.bat_image = load_image(bat_directory)

    self.image_ammo_pistol = load_image(ammo_pistol_icon_directory)
    self.image_ammo_ar = load_image(ammo_ar_icon_directory)
    self.image_ammo_rifle = load_image(ammo_rifle_icon_directory)
    self.image_ammo_sr = load_image(ammo_sr_icon_directory)

    self.medkit = load_image(icon_medkit_directory)
    self.medkit_unable = load_image(icon_medkit_unable_directory)

    self.hp_regen = load_image(hp_regen_directory)


def render_ingame_ui(self):
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

    # 몬스터 킬 피드백
    if self.ky > 0:
        self.ky -= pps / 4
        if self.ky < 0:
            self.ky = 0

    if game_framework.MODE == 'play':
        # 탄약 인디케이터 배경 출력
        self.back.opacify(400)
        self.back.draw(60 + ex, 20 + ey, 810, 210)

        if play_mode.weapon.weapon_type == 0:
            # 재장전 시 재장전 피드백 표시
            if self.weapon.reloading:
                self.reload_bar.draw(20 + ex, 90 + ey, 700 * (self.weapon.cur_reload_time / self.weapon.reload_time),
                                     120)

            # 탄창에 있는 탄약을 모두 소모 시 재장전이 필요함을 알림
            if self.weapon.cur_ammo > 0:
                self.font.draw(20 + ex, 40 + ey, '%d | %d' % (cur, num), (self.r, self.g, self.b))
            else:
                self.font.draw(20 + ex, 40 + ey, 'R | %d' % num, (self.r, self.g, self.b))

            if self.weapon.gun_type == 'pistol' or self.weapon.gun_type == 'smg':  # 각 총기가 사용하는 탄약을 보여준다
                self.image_ammo_pistol.rotate_draw(math.radians(32.2), 370 + ex, 40 + ey, 100, 100)
            elif self.weapon.gun_type == 'ar':
                self.image_ammo_ar.rotate_draw(math.radians(32.2), 370 + ex, 40 + ey, 100, 100)
            elif self.weapon.gun_type == 'rifle':
                self.image_ammo_rifle.rotate_draw(math.radians(32.2), 370 + ex, 40 + ey, 100, 100)
            elif self.weapon.gun_type == 'sr':
                self.image_ammo_sr.rotate_draw(math.radians(32.2), 370 + ex, 40 + ey, 100, 100)

        # 수류탄을 던질 수 있게되면 밝은 아이콘으로 표시, 아니면 어두운 아이콘으로 표시
        if self.weapon.throwable:
            self.coin_icon.draw(555 + ex, 45 + ey, 30, 30)
            self.grenade_able_icon.draw(500 + ex, 50 + ey, 100, 100)
            self.font_mini.draw(540 + ex, 80 + ey, 'L SHIFT', (255, 255, 255))
        else:
            self.font_small.draw(550 + ex, 45 + ey, '%d' % (120 - self.weapon.throw_delay_time), (255, 255, 255))
            self.grenade_unable_icon.draw(500 + ex, 50 + ey, 100, 100)

        # 플레이어 hp 출력
        self.hp_back.draw(WIDTH / 2 + ex, 15 + ey, 410, 50)
        self.font_small.draw(WIDTH / 2 - 200 + ex, 50 + ey, 'HP  %d | %d' % (self.p.cur_hp, self.p.hp), (255, 255, 255))
        self.hp_player.draw(
            WIDTH / 2 + ex - 200 + (400 * self.p.cur_hp / self.p.hp) / 2,
            20 + ey, 400 * (self.p.cur_hp / self.p.hp), 25)
        self.hp_regen.draw(
            WIDTH / 2 + ex - 200 + (400 * self.p.regen_timer / self.p.regen_delay) / 2,
            6 + ey, 400 * (self.p.regen_timer / self.p.regen_delay), 5)

        # 상점 아이콘 출력
        self.font_small.draw(75 + ex, HEIGHT - 40 + ey, 'TAB', (255, 255, 255))
        self.shop_icon.draw(40 + ex, HEIGHT - 40 + ey, 50, 50)

        # 코인 인디케이터 출력
        self.coin_icon.draw(WIDTH / 2 + 250 + ex, 30 + ey + self.get_y, 50, 50)
        self.font_small.draw(WIDTH / 2 + 280 + ex, 30 + ey + self.get_y, '%d' % play_mode.p.coin, (255, 255, 255))

        # 응급처치키드 출력
        if self.p.usable_medkit:
            if self.p.medkit_count == 0:
                self.medkit_unable.rotate_draw(math.radians(32.05), WIDTH / 2 + 490 + ex, 32 + ey, 70, 70)
                self.font_small.draw(WIDTH / 2 + 525 + ex, 30 + ey, '%d' % self.p.medkit_count, (255, 0, 0))
            else:
                self.font_mini.draw(WIDTH / 2 + 450 + ex, 65 + ey, 'LCTRL', (255, 255, 255))
                self.medkit.rotate_draw(math.radians(32.1), WIDTH / 2 + 490 + ex, 32 + ey, 70, 70)
                self.font_small.draw(WIDTH / 2 + 525 + ex, 30 + ey, '%d' % self.p.medkit_count, (255, 255, 0))
        else:
            self.medkit_unable.rotate_draw(math.radians(32.05), WIDTH / 2 + 490 + ex, 32 + ey, 70, 70)
            self.font_small.draw(WIDTH / 2 + 525 + ex, 30 + ey, '%d' % (10 - self.p.medkit_delay_time), (255, 255, 255))

        # 라운드 수 출력
        self.font.draw(WIDTH / 2 - 130 + ex, HEIGHT - 50 + ey, 'ROUND %d' % play_mode.tool.rounds,
                       (255, int(self.rg), int(self.rb)))

        self.font_small.draw \
            (WIDTH / 2 + 200 + ex, HEIGHT - 59 + ey + self.ky, \
             '%d | %d' % (play_mode.tool.limit - play_mode.tool.kill_count, play_mode.tool.limit), (255, 255, 255))

        #  근접 무기 스킬 사용 쿨타입 표시
        if self.weapon.weapon_type == 1:
            if self.weapon.melee == 'KNIFE':
                self.knife_image.draw(85 + ex, 55 + ey, 150, 100)

            elif self.weapon.melee == 'BAT':
                self.bat_image.rotate_draw(math.radians(-90), 45 + ex, 55 + ey, 50, 400)

            elif self.weapon.melee == 'RAPIER':
                self.rapier_image.draw(45 + ex, 55 + ey, 350, 100)
                if not self.weapon.skill_usable_rapier:
                    self.font.draw(330 + ex, 50 + ey, '%d' % (20 - self.weapon.skill_delay_time_rapier), (255, 255, 255))
                else:
                    self.font_small.draw(260 + ex, 50 + ey, 'R Button', (255, 255, 255))

            elif self.weapon.melee == 'KATANA':
                self.katana_image.rotate_draw(math.radians(-90), 45 + ex, 55 + ey, 60, 410)
                if not self.weapon.skill_usable_katana:
                    self.font.draw(330 + ex, 50 + ey, '%d' % (60 - self.weapon.skill_delay_time_katana), (255, 255, 255))
                else:
                    self.font_small.draw(260 + ex, 50 + ey, 'R Button', (255, 255, 255))

            elif self.weapon.melee == 'AXE':
                self.axe_image.rotate_draw(math.radians(-90), 80 + ex, 70 + ey, 200, 410)
                if not self.weapon.skill_usable_axe:
                    self.font.draw(330 + ex, 50 + ey, '%d' % (60 - self.weapon.skill_delay_time_axe), (255, 255, 255))
                else:
                    self.font_small.draw(260 + ex, 50 + ey, 'R Button', (255, 255, 255))


def update_ammo_ind(self):
    if self.weapon.reload_need:  # 총알을 모두 소모하면 인디케이터가 붉은색으로 표시된다
        self.g, self.b = 0, 0
    else:
        self.r, self.g, self.b = 255, 255, 255


def update_round_ind(self):
    pps = game_framework.pps
    if self.rg < 255:
        self.rg += pps / 3
    if self.rb < 255:
        self.rb += pps / 3

    if self.rg > 255:
        self.rg = 255
    if self.rb > 255:
        self.rb = 255
