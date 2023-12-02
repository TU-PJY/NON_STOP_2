from pico2d import load_image, load_wav

from config import *


def load_gun_image(self):
    self.flame_right = load_image(flame_right_directory)
    self.flame_left = load_image(flame_left_directory)

    self.m1911_right = load_image(m1911_right_directory)
    self.m1911_left = load_image(m1911_left_directory)
    self.m92_right = load_image(m92_right_directory)
    self.m92_left = load_image(m92_left_directory)
    self.m500_right = load_image(m500_right_directory)
    self.m500_left = load_image(m500_left_directory)
    self.degle_right = load_image(degle_right_directory)
    self.degle_left = load_image(degle_left_directory)
    self.qhand_right = load_image(qhand_right_directory)
    self.qhand_left = load_image(qhand_left_directory)
    self.qhand_spin_right = load_image(qhand_spin_right_directory)
    self.qhand_spin_left = load_image(qhand_spin_left_directory)

    self.aks74_right = load_image(aks74_right_directory)
    self.aks74_left = load_image(aks74_left_directory)
    self.ump_right = load_image(ump_right_directory)
    self.ump_left = load_image(ump_left_directory)
    self.vector_right = load_image(vector_right_directpry)
    self.vector_left = load_image(vector_left_directpry)
    self.thompson_right = load_image(thompson_right_directory)
    self.thompson_left = load_image(thompson_left_directory)
    self.p90_right = load_image(p90_right_directory)
    self.p90_left = load_image(p90_left_directory)

    self.scar_right = load_image(scar_h_right_directory)
    self.scar_left = load_image(scar_h_left_directory)
    self.m16_right = load_image(m16_right_directory)
    self.m16_left = load_image(m16_left_directory)
    self.mp44_right = load_image(mp44_right_directory)
    self.mp44_left = load_image(mp44_left_directory)
    self.aug_right = load_image(aug_right_directory)
    self.aug_left = load_image(aug_left_directory)
    self.groza_right = load_image(groza_right_directory)
    self.groza_left = load_image(groza_left_directory)

    self.m1_right = load_image(m1_right_directory)
    self.m1_left = load_image(m1_left_directory)
    self.win_right = load_image(win_right_directory)
    self.win_left = load_image(win_left_directory)
    self.win_spin_right = load_image(win_spin_right_directory)
    self.win_spin_left = load_image(win_spin_left_directory)
    self.mini14_right = load_image(mini14_right_directory)
    self.mini14_left = load_image(mini14_left_directory)
    self.fal_right = load_image(fal_right_directory)
    self.fal_left = load_image(fal_left_directory)
    self.lvoas_right = load_image(lvoas_right_directory)
    self.lvoas_left = load_image(lvoas_left_directory)

    self.awp_right = load_image(awp_right_directory)
    self.awp_left = load_image(awp_left_directory)
    self.spring_right = load_image(spring_right_directory)
    self.spring_left = load_image(spring_left_directory)
    self.kar98_right = load_image(kar98_right_directory)
    self.kar98_left = load_image(kar98_left_directory)
    self.m24_right = load_image(m24_right_directory)
    self.m24_left = load_image(m24_left_directory)
    self.cheytac_right = load_image(cheytac_right_directory)
    self.cheytac_left = load_image(cheytac_left_directory)


def load_melee_image(self):
    self.knife_right = load_image(knife_right_directory)
    self.knife_left = load_image(knife_left_directory)
    self.bat = load_image(bat_directory)
    self.bat_swing = load_image(bat_swing_directory)
    self.rapier = load_image(rapier_directory)
    self.rapid = load_image(rapid_directory)
    self.katana = load_image(katana_directory)
    self.katana_swing = load_image(katana_swing_directory)
    self.axe = load_image(axe_directory)


def load_gun_sound(self):
    # pistol
    self.pistol_reload = load_wav(pistol_reload_directory)
    self.revolver_reload = load_wav(revolver_reload_directory)

    # smg
    self.p90_shoot = load_wav(p90_shoot_directory)
    self.vector_shoot = load_wav(vector_shoot_directory)
    self.thompson_shoot = load_wav(thompson_shoot_directory)
    self.aks74_shoot = load_wav(aks74_shoot_directory)
    self.ump_shoot = load_wav(ump_shoot_directory)

    self.smg_reload = load_wav(smg_reload_directory)

    # ar
    self.scar_shoot = load_wav(scar_shoot_directory)
    self.m16_shoot = load_wav(m16_shoot_directory)
    self.mp44_shoot = load_wav(mp44_shoot_directory)
    self.aug_shoot = load_wav(aug_shoot_directory)
    self.groza_shoot = load_wav(groza_shoot_directory)

    self.ar_reload = load_wav(ar_reload_directory)

    # rifle
    self.m1_shoot = load_wav(m1_shoot_directory)
    self.win_shoot = load_wav(win_shoot_directory)
    self.win_spin = load_wav(win_spin_directory)
    self.win_reload = load_wav(win_reload_directory)

    self.mini14_shoot = load_wav(mini14_shoot_directory)
    self.fal_shoot = load_wav(fal_shoot_directory)
    self.lvoas_shoot = load_wav(lvoas_shoot_directory)

    # etc
    self.throw_sound = load_wav(throw_directoy)
    self.explode_sound = load_wav(explode_sound_directory)
