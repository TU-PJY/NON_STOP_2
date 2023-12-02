from mods import play_mode


def init_equip_list_gun():
    for i in range(5):
        for j in range(4):
            play_mode.weapon.equip_list_gun1[i][j] = False

    for i in range(5):
        for j in range(1):
            play_mode.weapon.equip_list_gun2[i][j] = False


def buy_gun_page1(i, j):
    buy = False

    if (i, j) == (0, 0):  # 기본 총이므로 구입 여부 확인은 하지 않음
        pass

    elif (i, j) == (1, 0):
        if play_mode.p.coin >= 300:  # 해당 총을 구입 하지 않았을 때
            play_mode.p.coin -= 300  # 가격 만큼 코인이 차감된다
            buy = True

    elif (i, j) == (2, 0):
        if play_mode.p.coin >= 600:
            play_mode.p.coin -= 600
            buy = True

    elif (i, j) == (3, 0):
        if play_mode.p.coin >= 800:
            play_mode.p.coin -= 800
            buy = True

    elif (i, j) == (4, 0):
        if play_mode.p.coin >= 1200:
            play_mode.p.coin -= 1200
            buy = True

    elif (i, j) == (0, 1):
        if play_mode.p.coin >= 1500:
            play_mode.p.coin -= 1500
            buy = True

    elif (i, j) == (1, 1):
        if play_mode.p.coin >= 2000:
            play_mode.p.coin -= 2000
            buy = True

    elif (i, j) == (2, 1):
        if play_mode.p.coin >= 2500:
            play_mode.p.coin -= 2500
            buy = True

    elif (i, j) == (3, 1):
        if play_mode.p.coin >= 3000:
            play_mode.p.coin -= 3000
            buy = True

    elif (i, j) == (4, 1):
        if play_mode.p.coin >= 4000:
            play_mode.p.coin -= 4000
            buy = True

    elif (i, j) == (0, 2):
        if play_mode.p.coin >= 5000:
            play_mode.p.coin -= 5000
            buy = True

    elif (i, j) == (1, 2):
        if play_mode.p.coin >= 7000:
            play_mode.p.coin -= 7000
            buy = True

    elif (i, j) == (2, 2):
        if play_mode.p.coin >= 9000:
            play_mode.p.coin -= 9000
            buy = True

    elif (i, j) == (3, 2):
        if play_mode.p.coin >= 11000:
            play_mode.p.coin -= 11000
            buy = True

    elif (i, j) == (4, 2):
        if play_mode.p.coin >= 13000:
            play_mode.p.coin -= 13000
            buy = True

    elif (i, j) == (0, 3):
        if play_mode.p.coin >= 15000:
            play_mode.p.coin -= 15000
            buy = True

    elif (i, j) == (1, 3):
        if play_mode.p.coin >= 20000:
            play_mode.p.coin -= 20000
            buy = True

    elif (i, j) == (2, 3):
        if play_mode.p.coin >= 25000:
            play_mode.p.coin -= 25000
            buy = True

    elif (i, j) == (3, 3):
        if play_mode.p.coin >= 30000:
            play_mode.p.coin -= 30000
            buy = True

    elif (i, j) == (4, 3):
        if play_mode.p.coin >= 35000:
            play_mode.p.coin -= 35000
            buy = True

    if buy:
        play_mode.weapon.buy_list_gun[i][j] = True


def buy_gun_page2(i, j):
    buy = False
    if (i, j) == (0, 0):
        if play_mode.p.coin >= 45000:
            play_mode.p.coin -= 45000
            buy = True

    if (i, j) == (1, 0):
        if play_mode.p.coin >= 55000:
            play_mode.p.coin -= 55000
            buy = True

    if (i, j) == (2, 0):
        if play_mode.p.coin >= 65000:
            play_mode.p.coin -= 65000
            buy = True

    if (i, j) == (3, 0):
        if play_mode.p.coin >= 75000:
            play_mode.p.coin -= 75000
            buy = True

    if (i, j) == (4, 0):
        if play_mode.p.coin >= 100000:
            play_mode.p.coin -= 100000
            buy = True

    if buy:
        play_mode.weapon.buy_list_gun2[i][j] = True


def equip_gun_page1(self, i, j):
    if (i, j) == (0, 0):
        play_mode.weapon.gun = 'M1911'
        play_mode.weapon.limit_ammo = 7

    elif (i, j) == (1, 0):
        play_mode.weapon.gun = 'M92'
        play_mode.weapon.limit_ammo = 15

    elif (i, j) == (2, 0):
        play_mode.weapon.gun = 'DEGLE'
        play_mode.weapon.limit_ammo = 8

    elif (i, j) == (3, 0):
        play_mode.weapon.gun = 'M500'
        play_mode.weapon.limit_ammo = 6
        play_mode.weapon.revolver_count = 6
        play_mode.weapon.revolver_shell_out = False  # 최초 재장전 시에는 탄피를 배출하지 않는다

    elif (i, j) == (4, 0):
        play_mode.weapon.gun = 'QHAND'
        play_mode.weapon.limit_ammo = 12
        play_mode.weapon.revolver_count = 12
        play_mode.weapon.revolver_shell_out = False  # 최초 재장전 시에는 탄피를 배출하지 않는다

    elif (i, j) == (0, 1):
        play_mode.weapon.gun = 'AKS74'
        play_mode.weapon.limit_ammo = 30

    elif (i, j) == (1, 1):
        play_mode.weapon.gun = 'UMP'
        play_mode.weapon.limit_ammo = 25

    elif (i, j) == (2, 1):
        play_mode.weapon.gun = 'VECTOR'
        play_mode.weapon.limit_ammo = 25

    elif (i, j) == (3, 1):
        play_mode.weapon.gun = 'THOMPSON'
        play_mode.weapon.limit_ammo = 30

    elif (i, j) == (4, 1):
        play_mode.weapon.gun = 'P90'
        play_mode.weapon.limit_ammo = 50

    elif (i, j) == (0, 2):
        play_mode.weapon.gun = 'SCAR_H'
        play_mode.weapon.limit_ammo = 25

    elif (i, j) == (1, 2):
        play_mode.weapon.gun = 'M16'
        play_mode.weapon.limit_ammo = 30

    elif (i, j) == (2, 2):
        play_mode.weapon.gun = 'MP44'
        play_mode.weapon.limit_ammo = 20

    elif (i, j) == (3, 2):
        play_mode.weapon.gun = 'AUG'
        play_mode.weapon.limit_ammo = 30

    elif (i, j) == (4, 2):
        play_mode.weapon.gun = 'GROZA'
        play_mode.weapon.limit_ammo = 40

    elif (i, j) == (0, 3):
        play_mode.weapon.gun = 'M1'
        play_mode.weapon.limit_ammo = 8

    elif (i, j) == (1, 3):
        play_mode.weapon.gun = 'WIN'
        play_mode.weapon.limit_ammo = 10

    elif (i, j) == (2, 3):
        play_mode.weapon.gun = 'MINI14'
        play_mode.weapon.limit_ammo = 30

    elif (i, j) == (3, 3):
        play_mode.weapon.gun = 'FAL'
        play_mode.weapon.limit_ammo = 20

    elif (i, j) == (4, 3):
        play_mode.weapon.gun = 'LVOAS'
        play_mode.weapon.limit_ammo = 20

    if j == 0:  # 총기 타입마다 사용 탄약, 재장전 소요 시간이 다르다
        play_mode.weapon.gun_type = 'pistol'
        play_mode.weapon.reload_time = 250
    elif j == 1:
        play_mode.weapon.gun_type = 'smg'
        play_mode.weapon.reload_time = 300
    elif j == 2:
        play_mode.weapon.gun_type = 'ar'
        play_mode.weapon.reload_time = 350
    elif j == 3:
        if play_mode.weapon.gun == 'MINI14':  # MINI14는 소총탄을 사용한다
            play_mode.weapon.gun_type = 'ar'
            play_mode.weapon.reload_time = 350

        elif play_mode.weapon.gun == 'WIN':
            play_mode.weapon.gun_type = 'rifle'
            play_mode.weapon.reload_time = 150

        else:
            play_mode.weapon.gun_type = 'rifle'
            play_mode.weapon.reload_time = 250

    init_equip_list_gun()  # 장착 중인 아이템 리스트 해제
    play_mode.weapon.equip_list_gun1[i][j] = True  # 갱신

    play_mode.weapon.eq_page = 1  # 표시할 특정 페이지 갱신
    self.eq_page = play_mode.weapon.eq_page
    self.data_change = True


def equip_gun_page2(self, i, j):
    if (i, j) == (0, 0):
        play_mode.weapon.gun = 'SPRING'
        play_mode.weapon.pen_limit = 2
        play_mode.weapon.limit_ammo = 5

    if (i, j) == (1, 0):
        play_mode.weapon.gun = 'KAR98'
        play_mode.weapon.pen_limit = 3
        play_mode.weapon.limit_ammo = 5

    if (i, j) == (2, 0):
        play_mode.weapon.gun = 'M24'
        play_mode.weapon.pen_limit = 4
        play_mode.weapon.limit_ammo = 5

    if (i, j) == (3, 0):
        play_mode.weapon.gun = 'AWP'
        play_mode.weapon.pen_limit = 6
        play_mode.weapon.limit_ammo = 5

    if (i, j) == (4, 0):
        play_mode.weapon.gun = 'CHEYTAC'
        play_mode.weapon.pen_limit = 8
        play_mode.weapon.limit_ammo = 7

    if j == 0:  # sr 타입
        play_mode.weapon.gun_type = 'sr'
        play_mode.weapon.reload_time = 350

    init_equip_list_gun()  # 장착 중인 아이템 리스트 해제
    play_mode.weapon.equip_list_gun2[i][j] = True  # 갱신

    play_mode.weapon.eq_page = 2
    self.eq_page = play_mode.weapon.eq_page
    self.data_change = True


# 총기 교체 시 잔탄을 모두 반환한 후 재장전 상태로 변경
# 이전에 사용하던 총기 타입에 맞는 탄약 개수에 반환한다
# 만약 현재 장착하고 있는 총기라면 무시한다.
def update_gun_item(self):
    if self.data_change:
        if not play_mode.weapon.prev_gun == play_mode.weapon.gun:
            if play_mode.weapon.prev_gun_type == 'pistol' or play_mode.weapon.prev_gun_type == 'smg':
                play_mode.weapon.pistol_ammo += play_mode.weapon.cur_ammo

            elif play_mode.weapon.prev_gun_type == 'ar':
                play_mode.weapon.ar_ammo += play_mode.weapon.cur_ammo

            elif play_mode.weapon.prev_gun_type == 'rifle':
                play_mode.weapon.rifle_ammo += play_mode.weapon.cur_ammo

            elif play_mode.weapon.prev_gun_type == 'sr':
                play_mode.weapon.sniper_ammo += play_mode.weapon.cur_ammo

            play_mode.weapon.zoom = False  # 스코프 모드 해제
            play_mode.target.draw_scope = False
            play_mode.weapon.pen_enable = False

            play_mode.weapon.prev_gun = play_mode.weapon.gun  # 이전 사용 총 갱신
            play_mode.weapon.prev_gun_type = play_mode.weapon.gun_type

            play_mode.weapon.cur_ammo = 0
            play_mode.weapon.cur_reload_time = 0
            play_mode.weapon.reloading = False  # 재장전 중이었다면 재장전 소요 시간 초기화
            play_mode.weapon.reload_need = True  # 재장전 필요 상태로 초기화
            play_mode.weapon.play_sound = True  # 재장전 사운드를 출력 할 수 있도록 한다

            self.eq_size_x = 250  # 아이템 장착 피드백을 재생한다
            self.eq_size_y = 200
            self.data_change = False
