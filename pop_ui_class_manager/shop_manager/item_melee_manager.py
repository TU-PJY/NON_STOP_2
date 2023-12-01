from mods import play_mode


def init_equip_list_melee():
    for i in range(5):
        for j in range(1):
            play_mode.weapon.equip_list_melee[i][j] = False


def buy_melee(i, j):
    buy = False

    if (i, j) == (0, 0):
        pass

    elif (i, j) == (1, 0):
        if play_mode.p.coin >= 3000:
            play_mode.p.coin -= 3000
            buy = True

    elif (i, j) == (2, 0):
        if play_mode.p.coin >= 10000:
            play_mode.p.coin -= 10000
            buy = True

    elif (i, j) == (3, 0):
        if play_mode.p.coin >= 25000:
            play_mode.p.coin -= 25000
            buy = True

    elif (i, j) == (4, 0):
        if play_mode.p.coin >= 55000:
            play_mode.p.coin -= 55000
            buy = True

    if buy:
        play_mode.weapon.buy_list_melee[i][j] = True


def equip_melee(self, i, j):
    if (i, j) == (0, 0):
        play_mode.weapon.melee = 'KNIFE'

    elif (i, j) == (1, 0):
        play_mode.weapon.melee = 'BAT'

    elif (i, j) == (2, 0):
        play_mode.weapon.melee = 'RAPIER'

    elif (i, j) == (3, 0):
        play_mode.weapon.melee = 'KATANA'

    elif (i, j) == (4, 0):
        play_mode.weapon.melee = 'AXE'

    init_equip_list_melee()
    play_mode.weapon.equip_list_melee[i][j] = True

    self.data_change = True


def update_melee_item(self):
    if self.data_change:  # 장착하고 있는 근접무기라면 무시
        if not play_mode.weapon.prev_melee == play_mode.weapon.melee:
            if play_mode.weapon.weapon_type == 1:
                play_mode.p.rotate = 0  # 무기 사용 중 무기 변경 시 무기 정보를 초기화 한다
            play_mode.weapon.melee_deg = 0
            play_mode.weapon.melee_x = 0
            play_mode.weapon.swing = False
            play_mode.weapon.swing_down = False
            play_mode.weapon.swing_up = False
            play_mode.weapon.wield = False

            # 카타나 스킬 사용 중이었다면 플레이어 이동 속도를 복구
            if play_mode.weapon.skill_enable and play_mode.weapon.prev_melee == 'KATANA':
                play_mode.p.speed = play_mode.p.temp_speed

            # AXE 스킬 사용 중이었다면 가속도 초기화
            if play_mode.weapon.skill_enable and play_mode.weapon.prev_melee == 'AXE':
                play_mode.p.jump_acc = 0

            play_mode.weapon.skill_enable = False  # 나머지 무기들의 경우도 스킬 초기화

            play_mode.weapon.prev_melee = play_mode.weapon.melee  # 이전 사용 근접 무기 갱신

            self.eq_size_x = 250  # 아이템 장착 피드백을 재생한다
            self.eq_size_y = 200

    if self.select_mode == 0 or self.select_mode == 1:
        self.ind_sel_on = False  # 더 이상 선택한 아이템이 표시되지 않는다.
