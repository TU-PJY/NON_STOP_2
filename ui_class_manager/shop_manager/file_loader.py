from pico2d import *

from config import *


def load_shop_resource(self):
    self.window = load_image(shop_window_directory)
    self.back = load_image(pause_bg_directory)
    self.button = load_image(shop_button_directory)
    self.button_gun = load_image(button_gun_directory)
    self.button_melee = load_image(button_melee_directory)
    self.button_exp = load_image(button_exp_directory)
    self.button_page_left = load_image(button_page_directory)
    self.button_page_right = load_image(button_page_directory)
    self.font = load_font(font_directory, 30)
    self.font_small = load_font(font_directory, 20)
    self.info = load_font(font2_directory, 20)
    self.info_back = load_image(info_back_directory)

    self.cursor = load_image(cursor_directory)

    self.coin_icon = load_image(coin_icon_directory)

    self.ind_equip = load_image(ind_equiped_directory)
    self.ind_select = load_image(ind_selected_directory)

    self.ind_lock = load_image(ind_lock_directory)

    self.image_m1911 = load_image(m1911_right_directory)
    self.image_m92 = load_image(m92_right_directory)
    self.image_m500 = load_image(m500_right_directory)
    self.image_degle = load_image(degle_right_directory)
    self.image_qhand = load_image(qhand_right_directory)

    self.image_aks74 = load_image(aks74_right_directory)
    self.image_ump = load_image(ump_right_directory)
    self.image_vector = load_image(vector_right_directpry)
    self.image_thompson = load_image(thompson_right_directory)
    self.image_p90 = load_image(p90_right_directory)

    self.image_scar = load_image(scar_h_right_directory)
    self.image_m16 = load_image(m16_right_directory)
    self.image_mp44 = load_image(mp44_right_directory)
    self.image_aug = load_image(aug_right_directory)
    self.image_groza = load_image(groza_right_directory)

    self.image_m1 = load_image(m1_right_directory)
    self.image_win = load_image(win_right_directory)
    self.image_mini14 = load_image(mini14_right_directory)
    self.image_fal = load_image(fal_right_directory)
    self.image_lvoas = load_image(lvoas_right_directory)

    self.image_spring = load_image(spring_right_directory)
    self.image_kar98 = load_image(kar98_right_directory)
    self.image_m24 = load_image(m24_right_directory)
    self.image_awp = load_image(awp_right_directory)
    self.image_cheytac = load_image(cheytac_right_directory)

    self.image_knife = load_image(knife_right_directory)
    self.image_bat = load_image(bat_directory)
    self.image_rapier = load_image(rapier_directory)
    self.image_katana = load_image(katana_directory)
    self.image_axe = load_image(axe_directory)

    self.image_ammo_pistol = load_image(ammo_pistol_icon_directory)
    self.image_ammo_ar = load_image(ammo_ar_icon_directory)
    self.image_ammo_rifle = load_image(ammo_rifle_icon_directory)
    self.image_ammo_sr = load_image(ammo_sr_icon_directory)

    self.medkit = load_image(icon_medkit_directory)
    self.hpup = load_image(icon_hp_upgrade_directory)
    self.regenup = load_image(icon_regen_upgrade_directory)
    self.grenup = load_image(icon_grenade_upgrade_directory)
    self.doublejump = load_image(icon_double_jump_directory)
    self.speedup = load_image(icon_speed_upgrade_directory)
