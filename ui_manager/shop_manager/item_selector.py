from pico2d import draw_rectangle

from mods import play_mode


def click_button(self):
    if self.select_mode == 0:
        # 페이지 이동 버튼 클릭
        if self.page_right_x - 40 < self.mx < self.page_right_x + 40 and \
                self.page_right_y - 50 < self.my < self.page_right_y + 50:
            if self.page < 2:
                self.page += 1

        elif self.page_left_x - 40 < self.mx < self.page_left_x + 40 and \
                self.page_left_y - 50 < self.my < self.page_left_y + 50:
            if self.page > 1:
                self.page -= 1

    # 카테고리 버튼 클릭
    for i in range(len(self.cat_x)):
        for j in range(len(self.cat_y)):
            if self.cat_x[i] - 100 < self.mx < self.cat_x[i] + 100 and \
                    self.cat_y[j] - 20 < self.my < self.cat_y[j] + 60:
                if i == 0:
                    self.select_mode = 0  # gun
                elif i == 1:
                    self.select_mode = 1  # melee
                elif i == 2:
                    self.select_mode = 2  # exp

    # 아이템 버튼 클릭
    for i in range(len(self.button_x)):
        for j in range(len(self.button_y)):
            if self.button_x[i] - 75 < self.mx < self.button_x[i] + 75 and \
                    self.button_y[j] - 50 < self.my < self.button_y[j] + 50:

                if self.select_mode == 0:
                    play_mode.weapon.zoom = False  # 다른 총 선택 시 스코프 모드 해제
                    play_mode.target.draw_scope = False
                    play_mode.weapon.pen_enable = False

                    if self.page == 1:
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
                        elif (i, j) == (4, 0):
                            play_mode.weapon.gun = 'QHAND'
                            play_mode.weapon.limit_ammo = 12

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

                        if j == 0:  # 총기 타입마다 재장전 소요 시간이 다르다
                            play_mode.weapon.gun_type = 'pistol'
                            play_mode.weapon.reload_time = 150
                        elif j == 1:
                            play_mode.weapon.gun_type = 'smg'
                            play_mode.weapon.reload_time = 200
                        elif j == 2:
                            play_mode.weapon.gun_type = 'ar'
                            play_mode.weapon.reload_time = 250
                        elif j == 3:
                            play_mode.weapon.gun_type = 'rifle'
                            play_mode.weapon.reload_time = 250

                    elif self.page == 2:  # sr의 경우 각 총마다 최대 관통 횟수가 다르다
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

                        if j == 0:
                            play_mode.weapon.gun_type = 'sr'
                            play_mode.weapon.reload_time = 350

                    # 총기 교체 시 잔탄을 모두 반환한 후 재장전 상태로 변경
                    # 이전에 사용하던 총기 타입에 맞는 탄약 개수에 반환한다
                    if play_mode.weapon.prev_gun_type == 'pistol' or play_mode.weapon.prev_gun_type == 'smg':
                        play_mode.weapon.pistol_ammo += play_mode.weapon.cur_ammo

                    elif play_mode.weapon.prev_gun_type == 'ar':
                        play_mode.weapon.ar_ammo += play_mode.weapon.cur_ammo

                    elif play_mode.weapon.prev_gun_type == 'rifle':
                        play_mode.weapon.rifle_ammo += play_mode.weapon.cur_ammo

                    elif play_mode.weapon.prev_gun_type == 'sr':
                        play_mode.weapon.sniper_ammo += play_mode.weapon.cur_ammo

                    play_mode.weapon.prev_gun_type = play_mode.weapon.gun_type
                    play_mode.weapon.cur_ammo = 0
                    play_mode.weapon.reload_need = True  # 재장전 필요 상태로 초기화

                elif self.select_mode == 1:
                    if play_mode.weapon.weapon_type == 1:
                        play_mode.p.rotate = 0  # 무기 사용 중 무기 변경 시 무기 정보를 초기화 한다
                    play_mode.weapon.melee_deg = 0
                    play_mode.weapon.melee_x = 0
                    play_mode.weapon.swing = False
                    play_mode.weapon.swing_down = False
                    play_mode.weapon.swing_up = False
                    play_mode.weapon.wield = False

                    # 카타나 스킬 사용 중이었다면 플레이어 이동 속도를 복구
                    if play_mode.weapon.skill_enable and play_mode.weapon.melee == 'KATANA':
                        play_mode.p.speed = play_mode.p.temp_speed
                    # AXE 스킬 사용 중이었다면 가속도 초기화
                    if play_mode.weapon.skill_enable and play_mode.weapon.prev_melee == 'AXE':
                        play_mode.p.jump_acc = 0

                    play_mode.weapon.skill_enable = False

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

                    play_mode.weapon.prev_melee = play_mode.weapon.melee

    self.click = False
