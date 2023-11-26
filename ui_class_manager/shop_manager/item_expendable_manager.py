from mods import play_mode


def buy_expendables(self, i, j):
    if (i, j) == (0, 0):
        if play_mode.p.coin >= 100:
            play_mode.p.coin -= 100
            play_mode.weapon.pistol_ammo += 150
            self.pistol_ammo_size_x = 150
            self.pistol_ammo_size_y = 150

    elif (i, j) == (1, 0):
        if play_mode.p.coin >= 200:
            play_mode.p.coin -= 200
            play_mode.weapon.ar_ammo += 100
            self.ar_ammo_size_x = 150
            self.ar_ammo_size_y = 150

    elif (i, j) == (2, 0):
        if play_mode.p.coin >= 350:
            play_mode.p.coin -= 350
            play_mode.weapon.rifle_ammo += 70
            self.rifle_ammo_size_x = 150
            self.rifle_ammo_size_y = 150

    elif (i, j) == (3, 0):
        if play_mode.p.coin >= 500:
            play_mode.p.coin -= 500
            play_mode.weapon.sniper_ammo += 30
            self.sniper_ammo_size_x = 150
            self.sniper_ammo_size_y = 150
