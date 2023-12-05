from mods import play_mode


def buy_expendables(self, i, j):
    from pop_ui_class.shop import Shop

    buy = False

    match (i, j):
        case (0, 0):
            if play_mode.p.coin >= 100:
                play_mode.p.coin -= 100
                play_mode.weapon.pistol_ammo += 150
                Shop.buy_ammo.play()
                buy = True
        case (1, 0):
            if play_mode.p.coin >= 300:
                play_mode.p.coin -= 300
                play_mode.weapon.ar_ammo += 100
                Shop.buy_ammo.play()
                buy = True
        case (2, 0):
            if play_mode.p.coin >= 600:
                play_mode.p.coin -= 600
                play_mode.weapon.rifle_ammo += 70
                Shop.buy_ammo.play()
                buy = True
        case (3, 0):
            if play_mode.p.coin >= 2000:
                play_mode.p.coin -= 2000
                play_mode.weapon.sniper_ammo += 20
                Shop.buy_ammo.play()
                buy = True
        case (4, 0):
            if play_mode.p.coin >= play_mode.p.medkit_cost:
                play_mode.p.coin -= play_mode.p.medkit_cost
                play_mode.p.medkit_count += 1
                play_mode.p.medkit_cost += 500
                Shop.buy_medkit.play()
                buy = True

        # 예외적으로 업그레이드도 이 함수에서 관리
        case (0, 1):
            if play_mode.p.coin >= play_mode.p.hp_cost and play_mode.p.hp_count < 3:
                play_mode.p.coin -= play_mode.p.hp_cost
                play_mode.p.hp += 50
                play_mode.p.cur_hp = play_mode.p.hp  # 체력 업그레이드 시 체력 회복
                play_mode.p.hp_count += 1
                play_mode.p.hp_cost *= 4
                Shop.buy_upgrade.play()
                buy = True
        case (1, 1):
            if play_mode.p.coin >= play_mode.p.regen_cost and play_mode.p.regen_count < 3:
                play_mode.p.coin -= play_mode.p.regen_cost
                play_mode.p.regen_delay -= 80
                play_mode.p.regen_count += 1
                play_mode.p.regen_cost *= 4
                Shop.buy_upgrade.play()
                buy = True
        case (2, 1):
            if play_mode.p.coin >= play_mode.p.speed_cost and play_mode.p.speed_count < 3:
                play_mode.p.coin -= play_mode.p.speed_cost
                play_mode.p.speed += 0.1
                play_mode.p.speed_count += 1
                play_mode.p.speed_cost *= 4
                Shop.buy_upgrade.play()
                buy = True
        case (3, 1):
            if play_mode.p.coin >= 6000 and play_mode.p.double_jump < 1:
                play_mode.p.coin -= 6000
                play_mode.p.jump_level += 1
                play_mode.p.double_jump += 1
                Shop.buy_upgrade.play()
                buy = True
        case (4, 1):
            if play_mode.p.coin >= play_mode.p.gren_cost and play_mode.p.gren_count < 2:
                play_mode.p.coin -= play_mode.p.gren_cost
                play_mode.weapon.gren_level += 1
                play_mode.p.gren_count += 1
                play_mode.p.gren_cost *= 10
                Shop.buy_upgrade.play()
                buy = True

    if buy:
        self.size_list[i][j] = 150  # 구입 피드백 재생
    else:
        Shop.cant_buy.play()
