from mods import play_mode


def buy_item(self):
    for i in range(len(self.button_x)):
        for j in range(len(self.button_y)):
            if self.button_x[i] - 75 < self.mx < self.button_x[i] + 75 and \
                    self.button_y[j] - 50 < self.my < self.button_y[j] + 50:

                if self.select_mode == 2:  # 각 종류의 탄약을 구입한다.
                    if (i, j) == (0, 0) and self.select_item == 'pistol_ammo':
                        if play_mode.p.coin >= 100:
                            play_mode.p.coin -= 100
                            play_mode.weapon.pistol_ammo += 100
                    elif (i, j) == (1, 0) and self.select_item == 'ar_ammo':
                        if play_mode.p.coin >= 200:
                            play_mode.p.coin -= 200
                            play_mode.weapon.ar_ammo += 100
                    elif (i, j) == (2, 0) and self.select_item == 'rifle_ammo':
                        if play_mode.p.coin >= 300:
                            play_mode.p.coin -= 300
                            play_mode.weapon.rifle_ammo += 100
                    elif (i, j) == (3, 0) and self.select_item == 'sniper_ammo':
                        if play_mode.p.coin >= 400:
                            play_mode.p.coin -= 400
                            play_mode.weapon.sniper_ammo += 50
    self.right_click = False
