from pico2d import *

from config import *


def load_shop_resource(self):
    from pop_ui_class.shop import Shop

    if not Shop.button_sound:
        Shop.button_sound = load_wav(button_click_directory)
        Shop.cant_buy = load_wav(cant_buy_directory)
        Shop.select_gun = load_wav(select_gun_directory)
        Shop.select_melee = load_wav(select_melee_directory)
        Shop.buy_ammo = load_wav(buy_ammo_directory)
        Shop.buy_medkit = load_wav(buy_medkit_directory)
        Shop.buy_upgrade = load_wav(upgrade_sound_directory)
        Shop.buy_sound = load_wav(buy_sound_directory)

        Shop.window = load_image(shop_window_directory)
        Shop.back = load_image(pause_bg_directory)
        Shop.button = load_image(shop_button_directory)
        Shop.button_gun = load_image(button_gun_directory)
        Shop.button_melee = load_image(button_melee_directory)
        Shop.button_exp = load_image(button_exp_directory)
        Shop.button_page_left = load_image(button_page_directory)
        Shop.button_page_right = load_image(button_page_directory)
        Shop.font = load_font(font_directory, 30)
        Shop.font_small = load_font(font_directory, 20)
        Shop.info = load_font(font2_directory, 20)
        Shop.info_back = load_image(info_back_directory)

        Shop.cursor = load_image(cursor_directory)

        Shop.coin_icon = load_image(coin_icon_directory)

        Shop.ind_equip = load_image(ind_equiped_directory)
        Shop.ind_select = load_image(ind_selected_directory)

        Shop.ind_lock = load_image(ind_lock_directory)

        Shop.image_m1911 = load_image(m1911_right_directory)
        Shop.image_m92 = load_image(m92_right_directory)
        Shop.image_m500 = load_image(m500_right_directory)
        Shop.image_degle = load_image(degle_right_directory)
        Shop.image_qhand = load_image(qhand_right_directory)

        Shop.image_aks74 = load_image(aks74_right_directory)
        Shop.image_ump = load_image(ump_right_directory)
        Shop.image_vector = load_image(vector_right_directpry)
        Shop.image_thompson = load_image(thompson_right_directory)
        Shop.image_p90 = load_image(p90_right_directory)

        Shop.image_scar = load_image(scar_h_right_directory)
        Shop.image_m16 = load_image(m16_right_directory)
        Shop.image_mp44 = load_image(mp44_right_directory)
        Shop.image_aug = load_image(aug_right_directory)
        Shop.image_groza = load_image(groza_right_directory)

        Shop.image_m1 = load_image(m1_right_directory)
        Shop.image_win = load_image(win_right_directory)
        Shop.image_mini14 = load_image(mini14_right_directory)
        Shop.image_fal = load_image(fal_right_directory)
        Shop.image_lvoas = load_image(lvoas_right_directory)

        Shop.image_spring = load_image(spring_right_directory)
        Shop.image_kar98 = load_image(kar98_right_directory)
        Shop.image_m24 = load_image(m24_right_directory)
        Shop.image_awp = load_image(awp_right_directory)
        Shop.image_cheytac = load_image(cheytac_right_directory)

        Shop.image_knife = load_image(knife_right_directory)
        Shop.image_bat = load_image(bat_directory)
        Shop.image_rapier = load_image(rapier_directory)
        Shop.image_katana = load_image(katana_directory)
        Shop.image_axe = load_image(axe_directory)

        Shop.image_ammo_pistol = load_image(ammo_pistol_icon_directory)
        Shop.image_ammo_ar = load_image(ammo_ar_icon_directory)
        Shop.image_ammo_rifle = load_image(ammo_rifle_icon_directory)
        Shop.image_ammo_sr = load_image(ammo_sr_icon_directory)

        Shop.medkit = load_image(icon_medkit_directory)
        Shop.hpup = load_image(icon_hp_upgrade_directory)
        Shop.regenup = load_image(icon_regen_upgrade_directory)
        Shop.grenup = load_image(icon_grenade_upgrade_directory)
        Shop.doublejump = load_image(icon_double_jump_directory)
        Shop.speedup = load_image(icon_speed_upgrade_directory)
