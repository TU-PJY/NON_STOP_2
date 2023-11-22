from mods import play_mode


def equip_item(self):  # 우클릭 시 좌클릭한 아이템과 동일할 시 해당 아이템 장착
    for i in range(len(self.button_x)):
        for j in range(len(self.button_y)):
            if self.button_x[i] - 75 < self.mx < self.button_x[i] + 75 and \
                    self.button_y[j] - 50 < self.my < self.button_y[j] + 50:

                if self.select_mode == 0:
                    if self.page == 1:  # 기본무기이므로 처음부터 사용 가능
                        if (i, j) == (0, 0) and self.select_gun == 'M1911':
                            play_mode.weapon.gun = 'M1911'
                            play_mode.weapon.limit_ammo = 7
                            self.change = True

                        elif (i, j) == (1, 0) and self.select_gun == 'M92':
                            if not play_mode.weapon.buy_list_gun[1]:
                                if play_mode.p.coin >= 300:  # 해당 총을 구입 하지 않았을 때
                                    play_mode.p.coin -= 300  # 가격 만큼 코인이 차감된다
                                    play_mode.weapon.buy_list_gun[1] = True  # 구입 사실을 저장한다
                            if play_mode.weapon.buy_list_gun[1]:  # 구입 후에는 코인이 차감되지 않는다
                                play_mode.weapon.gun = 'M92'
                                play_mode.weapon.limit_ammo = 15
                                self.change = True

                        elif (i, j) == (2, 0) and self.select_gun == 'DEGLE':
                            if not play_mode.weapon.buy_list_gun[2]:
                                if play_mode.p.coin >= 600:
                                    play_mode.p.coin -= 600
                                    play_mode.weapon.buy_list_gun[2] = True
                            if play_mode.weapon.buy_list_gun[2]:
                                play_mode.weapon.gun = 'DEGLE'
                                play_mode.weapon.limit_ammo = 8
                                self.change = True

                        elif (i, j) == (3, 0) and self.select_gun == 'M500':
                            if not play_mode.weapon.buy_list_gun[3]:
                                if play_mode.p.coin >= 800:
                                    play_mode.p.coin -= 800
                                    play_mode.weapon.buy_list_gun[3] = True
                            if play_mode.weapon.buy_list_gun[3]:
                                play_mode.weapon.gun = 'M500'
                                play_mode.weapon.limit_ammo = 6
                                self.change = True

                        elif (i, j) == (4, 0) and self.select_gun == 'QHAND':
                            if not play_mode.weapon.buy_list_gun[4]:
                                if play_mode.p.coin >= 1500:
                                    play_mode.p.coin -= 1500
                                    play_mode.weapon.buy_list_gun[4] = True
                            if play_mode.weapon.buy_list_gun[4]:
                                play_mode.weapon.gun = 'QHAND'
                                play_mode.weapon.limit_ammo = 12
                                self.change = True

                        elif (i, j) == (0, 1) and self.select_gun == 'AKS74':
                            if not play_mode.weapon.buy_list_gun[5]:
                                if play_mode.p.coin >= 2000:
                                    play_mode.p.coin -= 2000
                                    play_mode.weapon.buy_list_gun[5] = True
                            if play_mode.weapon.buy_list_gun[5]:
                                play_mode.weapon.gun = 'AKS74'
                                play_mode.weapon.limit_ammo = 30
                                self.change = True

                        elif (i, j) == (1, 1) and self.select_gun == 'UMP':
                            if not play_mode.weapon.buy_list_gun[6]:
                                if play_mode.p.coin >= 2500:
                                    play_mode.p.coin -= 2500
                                    play_mode.weapon.buy_list_gun[6] = True
                            if play_mode.weapon.buy_list_gun[6]:
                                play_mode.weapon.gun = 'UMP'
                                play_mode.weapon.limit_ammo = 25
                                self.change = True

                        elif (i, j) == (2, 1) and self.select_gun == 'VECTOR':
                            if not play_mode.weapon.buy_list_gun[7]:
                                if play_mode.p.coin >= 3000:
                                    play_mode.p.coin -= 3000
                                    play_mode.weapon.buy_list_gun[7] = True
                            if play_mode.weapon.buy_list_gun[7]:
                                play_mode.weapon.gun = 'VECTOR'
                                play_mode.weapon.limit_ammo = 25
                                self.change = True

                        elif (i, j) == (3, 1) and self.select_gun == 'THOMPSON':
                            if not play_mode.weapon.buy_list_gun[8]:
                                if play_mode.p.coin >= 3500:
                                    play_mode.p.coin -= 3500
                                    play_mode.weapon.buy_list_gun[8] = True
                            if play_mode.weapon.buy_list_gun[8]:
                                play_mode.weapon.gun = 'THOMPSON'
                                play_mode.weapon.limit_ammo = 30
                                self.change = True

                        elif (i, j) == (4, 1) and self.select_gun == 'P90':
                            if not play_mode.weapon.buy_list_gun[9]:
                                if play_mode.p.coin >= 4000:
                                    play_mode.p.coin -= 4000
                                    play_mode.weapon.buy_list_gun[9] = True
                            if play_mode.weapon.buy_list_gun[9]:
                                play_mode.weapon.gun = 'P90'
                                play_mode.weapon.limit_ammo = 50
                                self.change = True

                        elif (i, j) == (0, 2) and self.select_gun == 'SCAR_H':
                            if not play_mode.weapon.buy_list_gun[10]:
                                if play_mode.p.coin >= 5000:
                                    play_mode.p.coin -= 5000
                                    play_mode.weapon.buy_list_gun[10] = True
                            if play_mode.weapon.buy_list_gun[10]:
                                play_mode.weapon.gun = 'SCAR_H'
                                play_mode.weapon.limit_ammo = 25
                                self.change = True

                        elif (i, j) == (1, 2) and self.select_gun == 'M16':
                            if not play_mode.weapon.buy_list_gun[11]:
                                if play_mode.p.coin >= 6000:
                                    play_mode.p.coin -= 6000
                                    play_mode.weapon.buy_list_gun[11] = True
                            if play_mode.weapon.buy_list_gun[11]:
                                play_mode.weapon.gun = 'M16'
                                play_mode.weapon.limit_ammo = 30
                                self.change = True

                        elif (i, j) == (2, 2) and self.select_gun == 'MP44':
                            if not play_mode.weapon.buy_list_gun[12]:
                                if play_mode.p.coin >= 7000:
                                    play_mode.p.coin -= 7000
                                    play_mode.weapon.buy_list_gun[12] = True
                            if play_mode.weapon.buy_list_gun[12]:
                                play_mode.weapon.gun = 'MP44'
                                play_mode.weapon.limit_ammo = 20
                                self.change = True

                        elif (i, j) == (3, 2) and self.select_gun == 'AUG':
                            if not play_mode.weapon.buy_list_gun[13]:
                                if play_mode.p.coin >= 8000:
                                    play_mode.p.coin -= 8000
                                    play_mode.weapon.buy_list_gun[13] = True
                            if play_mode.weapon.buy_list_gun[13]:
                                play_mode.weapon.gun = 'AUG'
                                play_mode.weapon.limit_ammo = 30
                                self.change = True

                        elif (i, j) == (4, 2) and self.select_gun == 'GROZA':
                            if not play_mode.weapon.buy_list_gun[14]:
                                if play_mode.p.coin >= 9000:
                                    play_mode.p.coin -= 9000
                                    play_mode.weapon.buy_list_gun[14] = True
                            if play_mode.weapon.buy_list_gun[14]:
                                play_mode.weapon.gun = 'GROZA'
                                play_mode.weapon.limit_ammo = 40
                                self.change = True

                        elif (i, j) == (0, 3) and self.select_gun == 'M1':
                            if not play_mode.weapon.buy_list_gun[15]:
                                if play_mode.p.coin >= 11000:
                                    play_mode.p.coin -= 11000
                                    play_mode.weapon.buy_list_gun[15] = True
                            if play_mode.weapon.buy_list_gun[15]:
                                play_mode.weapon.gun = 'M1'
                                play_mode.weapon.limit_ammo = 8
                                self.change = True

                        elif (i, j) == (1, 3) and self.select_gun == 'WIN':
                            if not play_mode.weapon.buy_list_gun[16]:
                                if play_mode.p.coin >= 13000:
                                    play_mode.p.coin -= 13000
                                    play_mode.weapon.buy_list_gun[16] = True
                            if play_mode.weapon.buy_list_gun[16]:
                                play_mode.weapon.gun = 'WIN'
                                play_mode.weapon.limit_ammo = 10
                                self.change = True

                        elif (i, j) == (2, 3) and self.select_gun == 'MINI14':
                            if not play_mode.weapon.buy_list_gun[17]:
                                if play_mode.p.coin >= 15000:
                                    play_mode.p.coin -= 15000
                                    play_mode.weapon.buy_list_gun[17] = True
                            if play_mode.weapon.buy_list_gun[17]:
                                play_mode.weapon.gun = 'MINI14'
                                play_mode.weapon.limit_ammo = 30
                                self.change = True

                        elif (i, j) == (3, 3) and self.select_gun == 'FAL':
                            if not play_mode.weapon.buy_list_gun[18]:
                                if play_mode.p.coin >= 17000:
                                    play_mode.p.coin -= 17000
                                    play_mode.weapon.buy_list_gun[18] = True
                            if play_mode.weapon.buy_list_gun[18]:
                                play_mode.weapon.gun = 'FAL'
                                play_mode.weapon.limit_ammo = 20
                                self.change = True

                        elif (i, j) == (4, 3) and self.select_gun == 'LVOAS':
                            if not play_mode.weapon.buy_list_gun[19]:
                                if play_mode.p.coin >= 19000:
                                    play_mode.p.coin -= 19000
                                    play_mode.weapon.buy_list_gun[19] = True
                            if play_mode.weapon.buy_list_gun[19]:
                                play_mode.weapon.gun = 'LVOAS'
                                play_mode.weapon.limit_ammo = 20
                                self.change = True

                        if self.change:
                            if j == 0:  # 총기 타입마다 사용 탄약, 재장전 소요 시간이 다르다
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

                            play_mode.weapon.eq_page = 1  # 표시할 특정 페이지 갱신
                            self.eq_page = play_mode.weapon.eq_page

                    elif self.page == 2:  # sr의 경우 각 총마다 최대 관통 횟수가 다르다
                        if (i, j) == (0, 0) and self.select_gun == 'SPRING':
                            if not play_mode.weapon.buy_list_gun[20]:
                                if play_mode.p.coin >= 23000:
                                    play_mode.p.coin -= 23000
                                    play_mode.weapon.buy_list_gun[20] = True
                            if play_mode.weapon.buy_list_gun[20]:
                                play_mode.weapon.gun = 'SPRING'
                                play_mode.weapon.pen_limit = 2
                                play_mode.weapon.limit_ammo = 5
                                self.change = True

                        if (i, j) == (1, 0) and self.select_gun == 'KAR98':
                            if not play_mode.weapon.buy_list_gun[21]:
                                if play_mode.p.coin >= 28000:
                                    play_mode.p.coin -= 28000
                                    play_mode.weapon.buy_list_gun[21] = True
                            if play_mode.weapon.buy_list_gun[21]:
                                play_mode.weapon.gun = 'KAR98'
                                play_mode.weapon.pen_limit = 3
                                play_mode.weapon.limit_ammo = 5
                                self.change = True

                        if (i, j) == (2, 0) and self.select_gun == 'M24':
                            if not play_mode.weapon.buy_list_gun[22]:
                                if play_mode.p.coin >= 33000:
                                    play_mode.p.coin -= 33000
                                    play_mode.weapon.buy_list_gun[22] = True
                            if play_mode.weapon.buy_list_gun[22]:
                                play_mode.weapon.gun = 'M24'
                                play_mode.weapon.pen_limit = 4
                                play_mode.weapon.limit_ammo = 5
                                self.change = True

                        if (i, j) == (3, 0) and self.select_gun == 'AWP':
                            if not play_mode.weapon.buy_list_gun[23]:
                                if play_mode.p.coin >= 38000:
                                    play_mode.p.coin -= 38000
                                    play_mode.weapon.buy_list_gun[23] = True
                            if play_mode.weapon.buy_list_gun[23]:
                                play_mode.weapon.gun = 'AWP'
                                play_mode.weapon.pen_limit = 6
                                play_mode.weapon.limit_ammo = 5
                                self.change = True

                        if (i, j) == (4, 0) and self.select_gun == 'CHEYTAC':
                            if not play_mode.weapon.buy_list_gun[24]:
                                if play_mode.p.coin >= 43000:
                                    play_mode.p.coin -= 43000
                                    play_mode.weapon.buy_list_gun[24] = True
                            if play_mode.weapon.buy_list_gun[24]:
                                play_mode.weapon.gun = 'CHEYTAC'
                                play_mode.weapon.pen_limit = 8
                                play_mode.weapon.limit_ammo = 7
                                self.change = True

                        if self.change:
                            if j == 0:  # sr 타입
                                play_mode.weapon.gun_type = 'sr'
                                play_mode.weapon.reload_time = 350

                            play_mode.weapon.eq_page = 2
                            self.eq_page = play_mode.weapon.eq_page

                    # 총기 교체 시 잔탄을 모두 반환한 후 재장전 상태로 변경
                    # 이전에 사용하던 총기 타입에 맞는 탄약 개수에 반환한다
                    # 만약 현재 장착하고 있는 총기라면 무시한다.
                    if self.change:
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
                            play_mode.weapon.reloading = False
                            play_mode.weapon.reload_need = True  # 재장전 필요 상태로 초기화

                            self.eq_size_x = 250  # 아이템 장착 피드백을 재생한다
                            self.eq_size_y = 200
                            self.change = False

                elif self.select_mode == 1:
                    if (i, j) == (0, 0) and self.select_melee == 'KNIFE':
                        play_mode.weapon.melee = 'KNIFE'
                        self.change = True

                    elif (i, j) == (1, 0) and self.select_melee == 'BAT':
                        if not play_mode.weapon.buy_list_melee[1]:
                            if play_mode.p.coin >= 5000:
                                play_mode.p.coin -= 5000
                                play_mode.weapon.buy_list_melee[1] = True
                        if play_mode.weapon.buy_list_melee[1]:
                            play_mode.weapon.melee = 'BAT'
                            self.change = True

                    elif (i, j) == (2, 0) and self.select_melee == 'RAPIER':
                        if not play_mode.weapon.buy_list_melee[2]:
                            if play_mode.p.coin >= 15000:
                                play_mode.p.coin -= 15000
                                play_mode.weapon.buy_list_melee[2] = True
                        if play_mode.weapon.buy_list_melee[2]:
                            play_mode.weapon.melee = 'RAPIER'
                            self.change = True

                    elif (i, j) == (3, 0) and self.select_melee == 'KATANA':
                        if not play_mode.weapon.buy_list_melee[3]:
                            if play_mode.p.coin >= 30000:
                                play_mode.p.coin -= 30000
                                play_mode.weapon.buy_list_melee[3] = True
                        if play_mode.weapon.buy_list_melee[3]:
                            play_mode.weapon.melee = 'KATANA'
                            self.change = True

                    elif (i, j) == (4, 0) and self.select_melee == 'AXE':
                        if not play_mode.weapon.buy_list_melee[4]:
                            if play_mode.p.coin >= 50000:
                                play_mode.p.coin -= 50000
                                play_mode.weapon.buy_list_melee[4] = True
                        if play_mode.weapon.buy_list_melee[4]:
                            play_mode.weapon.melee = 'AXE'
                            self.change = True

                    # 장착하고 있는 근접무기라면 무시
                    if self.change:
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
                        self.selected_item = False   # 더 이상 선택한 아이템이 표시되지 않는다.

    self.right_click = False
