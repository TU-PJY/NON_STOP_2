from mods import play_mode


def buy_expendables(self, i, j):
    if (i, j) == (0, 0):
        if play_mode.p.coin >= 100:
            play_mode.p.coin -= 100
            play_mode.weapon.pistol_ammo += 150

    elif (i, j) == (1, 0):
        if play_mode.p.coin >= 200:
            play_mode.p.coin -= 200
            play_mode.weapon.ar_ammo += 100

    elif (i, j) == (2, 0):
        if play_mode.p.coin >= 350:
            play_mode.p.coin -= 350
            play_mode.weapon.rifle_ammo += 70

    elif (i, j) == (3, 0):
        if play_mode.p.coin >= 500:
            play_mode.p.coin -= 500
            play_mode.weapon.sniper_ammo += 30

    self.size_list[i][j] = 150  # 구입 피드백 재생
