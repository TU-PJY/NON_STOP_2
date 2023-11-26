from mods import play_mode


def buy_expendables(self, i, j):
    match(i, j):
        case (0, 0):
            if play_mode.p.coin >= 100:
                play_mode.p.coin -= 100
                play_mode.weapon.pistol_ammo += 150
        case (1, 0):
            if play_mode.p.coin >= 200:
                play_mode.p.coin -= 200
                play_mode.weapon.ar_ammo += 100
        case (2, 0):
            if play_mode.p.coin >= 350:
                play_mode.p.coin -= 350
                play_mode.weapon.rifle_ammo += 70
        case (3, 0):
            if play_mode.p.coin >= 500:
                play_mode.p.coin -= 500
                play_mode.weapon.sniper_ammo += 30
        case (4, 0):
            if play_mode.p.coin >= 400:
                play_mode.p.coin -= 400
                play_mode.p.medkit_count += 1

    # 예외적으로 업그레이드도 이 함수에서 관리
        case(0, 1):
            if play_mode.p.coin >= play_mode.p.hp_cost and play_mode.p.hp_count < 3:
                play_mode.p.coin -= play_mode.p.hp_cost
                play_mode.p.hp += 50
                play_mode.p.cur_hp = play_mode.p.hp  # 체력 업그레이드 시 체력 회복
                play_mode.p.hp_count += 1
                play_mode.p.hp_cost *= 3
        case (1, 1):
            if play_mode.p.coin >= play_mode.p.regen_cost and play_mode.p.regen_count < 3:
                play_mode.p.coin -= play_mode.p.regen_cost
                play_mode.p.regen_delay -= 100
                play_mode.p.regen_count += 1
                play_mode.p.regen_cost *= 3
        case (2, 1):
            if play_mode.p.coin >= play_mode.p.speed_cost and play_mode.p.speed_count < 3:
                play_mode.p.coin -= play_mode.p.speed_cost
                play_mode.p.speed += 0.1
                play_mode.p.speed_count += 1
                play_mode.p.speed_cost *= 3
        case (3, 1):
            if play_mode.p.coin >= 3000 and play_mode.p.double_jump < 1:
                play_mode.p.coin -= 3000
                play_mode.p.jump_level += 1
                play_mode.p.double_jump += 1
        case (4, 1):
            if play_mode.p.coin >= play_mode.p.gren_cost and play_mode.p.gren_count < 2:
                play_mode.p.coin -= play_mode.p.gren_cost
                play_mode.weapon.gren_level += 1
                play_mode.p.gren_count += 1
                play_mode.p.gren_cost *= 4
                play_mode.p.gren_use_cost *= 2

    self.size_list[i][j] = 150  # 구입 피드백 재생
