# 환경 변수 파일 

from tkinter import *

# 현재 모니터 크기를 인식하여 자동으로 창 사이즈를 조정한다.
root = Tk()
HEIGHT = root.winfo_screenheight()
WIDTH = root.winfo_screenwidth()
# print(HEIGHT, WIDTH)

JUMP_ACC = 4.5  # 점프 가속도
LAND_SHAKE = 100  # 착지 시 맵이 눌리는 효과 수치

# 픽셀 비율
PIXEL_PER_METER = 150  # 1미터 = 150픽셀

# 게임 전체 속도
RUN_SPEED_KMPH = 25
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)  # 게임에서 사용하는 공유 PPS

# PPS USE RULE
# 1. 딜레이 및 타이머 감소 시 PPS * frame_time / 3 사용
# 2. 개체 이동 속도는 speed * PPS * frame_time / 4 사용
# 3. 그 외의 수치 변화는 알맞게 조정

# 오브젝트 프레임 속도
TIME_PER_ACTION = 2
APT = 1.0 / TIME_PER_ACTION
FPA = 8

RECOIL_REDUCE = 1  # 조준점 복구 지연 속도
FLAME_DISPLAY_TIME = 15  # 총구 화염 출력 시간
TARGET_DOT_DISPLAY_TIME = 10  # 조준점 내부에 빨간 점이 표시되는 시간

# 플레이어 이미지 파일 경로
player1_right_image_directory = 'res//player_image//player1_right.png'
player1_left_image_directory = 'res//player_image//player1_left.png'

player2_right_image_directory = 'res//player_image//player2_right.png'
player2_left_image_directory = 'res//player_image//player2_left.png'

player3_right_image_directory = 'res//player_image//player3_right.png'
player3_left_image_directory = 'res//player_image//player3_left.png'

player4_right_image_directory = 'res//player_image//player4_right.png'
player4_left_image_directory = 'res//player_image//player4_left.png'

player5_right_image_directory = 'res//player_image//player5_right.png'
player5_left_image_directory = 'res//player_image//player5_left.png'

player6_right_image_directory = 'res//player_image//player6_right.png'
player6_left_image_directory = 'res//player_image//player6_left.png'

player7_right_image_directory = 'res//player_image//player7_right.png'
player7_left_image_directory = 'res//player_image//player7_left.png'

player8_right_image_directory = 'res//player_image//player8_right.png'
player8_left_image_directory = 'res//player_image//player8_left.png'

# 배경 이미지 파일 경로
land_image_directory = 'res//map_image//land.png'
bg_image_directory = 'res//map_image//bg.png'
wall_image_directory = 'res//map_image//wall.png'
bg_back_image_directory = 'res//map_image//bg_back.png'

# 조준점 이미지 파일 경로 
target_up_directory = 'res//target_image//target_up.png'
target_down_directory = 'res//target_image//target_down.png'
target_right_directory = 'res//target_image//target_right.png'
target_left_directory = 'res//target_image//target_left.png'
target_x_directory = 'res//target_image//mode_melee.png'
target_melee_directory = 'res//target_image//target_melee.png'

scope_awp_directory = 'res//target_image//scope_awp.png'
scope_spring_directory = 'res//target_image//scope_spring.png'
scope_kar98_directory = 'res//target_image//scope_kar98.png'
scope_m24_directory = 'res//target_image//scope_m24.png'
scope_cheytac_directory = 'res//target_image//scope_cheytac.png'

# 총 이미지 파일 경로
# pistol
m1911_right_directory = 'res//gun_image//pistol//m1911_right.png'
m1911_left_directory = 'res//gun_image//pistol//m1911_left.png'
m92_right_directory = 'res//gun_image//pistol//m92_right.png'
m92_left_directory = 'res//gun_image//pistol//m92_left.png'
m500_right_directory = 'res//gun_image//pistol//m500_right.png'
m500_left_directory = 'res//gun_image//pistol//m500_left.png'
degle_right_directory = 'res//gun_image//pistol//degle_right.png'
degle_left_directory = 'res//gun_image//pistol//degle_left.png'
qhand_right_directory = 'res//gun_image//pistol//qhand_right.png'
qhand_left_directory = 'res//gun_image//pistol//qhand_left.png'
qhand_spin_right_directory = 'res//gun_image//pistol//qhand_spin_right.png'
qhand_spin_left_directory = 'res//gun_image//pistol//qhand_spin_left.png'

m500_spin_right_directory = 'res//gun_image//pistol//m500_spin_right.png'
m500_spin_left_directory = 'res//gun_image//pistol//m500_spin_left.png'

# smg
aks74_right_directory = 'res//gun_image//smg//aks74_right.png'
aks74_left_directory = 'res//gun_image//smg//aks74_left.png'
ump_right_directory = 'res//gun_image//smg//ump_right.png'
ump_left_directory = 'res//gun_image//smg//ump_left.png'
vector_right_directpry = 'res//gun_image//smg//vector_right.png'
vector_left_directpry = 'res//gun_image//smg//vector_left.png'
thompson_right_directory = 'res//gun_image//smg//thompson_right.png'
thompson_left_directory = 'res//gun_image//smg//thompson_left.png'
p90_right_directory = 'res//gun_image//smg//p90_right.png'
p90_left_directory = 'res//gun_image//smg//p90_left.png'

# ar
scar_h_right_directory = 'res//gun_image//ar//SCAR_H_right.png'
scar_h_left_directory = 'res//gun_image//ar//SCAR_H_left.png'
m16_right_directory = 'res//gun_image//ar//m16_right.png'
m16_left_directory = 'res//gun_image//ar//m16_left.png'
mp44_right_directory = 'res//gun_image//ar//mp44_right.png'
mp44_left_directory = 'res//gun_image//ar//mp44_left.png'
aug_right_directory = 'res//gun_image//ar//aug_right.png'
aug_left_directory = 'res//gun_image//ar//aug_left.png'
groza_right_directory = 'res//gun_image//ar//groza_right.png'
groza_left_directory = 'res//gun_image//ar//groza_left.png'

# rifle
m1_right_directory = 'res//gun_image//rifle//m1_right.png'
m1_left_directory = 'res//gun_image//rifle//m1_left.png'
win_right_directory = 'res//gun_image//rifle//winchester_right.png'
win_spin_right_directory = 'res//gun_image//rifle//winchester_right_spin.png'
win_left_directory = 'res//gun_image//rifle//winchester_left.png'
win_spin_left_directory = 'res//gun_image//rifle//winchester_left_spin.png'
mini14_right_directory = 'res//gun_image//rifle//mini14_right.png'
mini14_left_directory = 'res//gun_image//rifle//mini14_left.png'
fal_right_directory = 'res//gun_image//rifle//fal_right.png'
fal_left_directory = 'res//gun_image//rifle//fal_left.png'
lvoas_right_directory = 'res//gun_image//rifle//lvoas_right.png'
lvoas_left_directory = 'res//gun_image//rifle//lvoas_left.png'

# sr
spring_right_directory = 'res//gun_image//sr//spring_right.png'
spring_left_directory = 'res//gun_image//sr//spring_left.png'
kar98_right_directory = 'res//gun_image//sr//kar98_right.png'
kar98_left_directory = 'res//gun_image//sr//kar98_left.png'
m24_right_directory = 'res//gun_image//sr//m24_right.png'
m24_left_directory = 'res//gun_image//sr//m24_left.png'
awp_right_directory = 'res//gun_image//sr//awp_right.png'
awp_left_directory = 'res//gun_image//sr//awp_left.png'
cheytac_right_directory = 'res//gun_image//sr//cheytac_right.png'
cheytac_left_directory = 'res//gun_image//sr//cheytac_left.png'

# 불꽃 이미지 파일 경로
flame_right_directory = 'res//gun_image//misc//flame_right.png'
flame_left_directory = 'res//gun_image//misc//flame_left.png'

# 근접무기 이미지 경로
knife_right_directory = 'res//melee_image//knife_right.png'
knife_left_directory = 'res//melee_image//knife_left.png'
bat_directory = 'res//melee_image//bat.png'
bat_swing_directory = 'res//melee_image//bat_swing.png'
rapier_directory = 'res//melee_image//rapier.png'
rapid_directory = 'res//melee_image//effect//rapid.png'
katana_directory = 'res//melee_image//katana.png'
katana_swing_directory = 'res//melee_image//katana_swing.png'
axe_directory = 'res//melee_image//axe.png'
axe_swing_directory = 'res//melee_image//axe_swing.png'

# 몬스터 이미지 파일 경로
type1_directory = 'res//monster_image//goblin_small.png'
type1_damage_directory = 'res//monster_image//feedback//goblin_small_damage.png'
type2_directory = 'res//monster_image//ghost_small.png'
type2_damage_directory = 'res//monster_image//feedback//ghost_small_damage.png'
type3_directory = 'res//monster_image//slime.png'
type3_damage_directory = 'res//monster_image//feedback//slime_damage.png'
type4_directory = 'res//monster_image//apple.png'
type4_damage_directory = 'res//monster_image//feedback//apple_damage.png'
hit_feeeback_directory = 'res//monster_image//feedback//hit.png'

# Prop 이미지 파일 경로
arrow_right_directory = 'res//prop//arrow_right.png'
arrow_left_directory = 'res//prop//arrow_left.png'
shell_directory = 'res//prop//catridge.png'
katana_slice_directory = 'res//melee_image//katana_slice.png'
player1_slice_right_directory = 'res//player_image//player1_slice_right.png'
player1_slice_left_directory = 'res//player_image//player1_slice_left.png'
slice_effect_directory = 'res//melee_image//effect//slice_effect.png'
player_damage_directory = 'res//player_image//player_damage.png'
explode_directory = 'res//prop//explode.png'
grenade_directory = 'res//prop//grenade.png'
splash_directory = 'res//prop//splash.png'

goblin_dead_directory = 'res//prop//goblin_dead.png'
apple_dead_directory = 'res//prop//apple_dead.png'
ghost_dead_directory = 'res//prop//ghost_dead.png'

player_heal_directory = 'res//player_image//player_heal.png'

dead_bg_directory = 'res//prop//dead_bg.png'
you_dead_directory = 'res//prop//you_dead.png'
front_directory = 'res//prop//front.png'

clip_directory = 'res//prop//clip.png'

# ui 이미지 파일 경로
shop_window_directory = 'res//ui//shop_window.png'
pause_bg_directory = 'res//ui//pause_bg.png'
shop_button_directory = 'res//ui//shop_button.png'
button_gun_directory = 'res//ui//button_gun.png'
button_melee_directory = 'res//ui//button_melee.png'
button_exp_directory = 'res//ui//button_exp.png'
button_page_directory = 'res//ui//page_button.png'
cursor_directory = 'res//ui//cursor.png'
grenable_able_icon_directory = 'res//ui//grenade_able_icon.png'
grenable_unable_icon_directory = 'res//ui//grenade_unable_icon.png'

info_back_directory = 'res//ui//info_back.png'

hp_back_directory = 'res//ui//hp_back.png'
hp_front_directory = 'res//ui//hp_front.png'
hp_player_directory = 'res//ui//hp_player.png'
shop_icon_directory = 'res//ui//shop_icon.png'
coin_icon_directory = 'res//ui//coin.png'

ammo_ind_back_directory = 'res//ui//ammo_ind_back.png'
reload_bar_directory = 'res//ui//reload_bar.png'

ammo_pistol_icon_directory = 'res//ui//ammo_pistol.png'
ammo_ar_icon_directory = 'res//ui//ammo_ar.png'
ammo_rifle_icon_directory = 'res//ui//ammo_rifle.png'
ammo_sr_icon_directory = 'res//ui//ammo_sr.png'

ind_selected_directory = 'res//ui//item_selected.png'
ind_equiped_directory = 'res//ui//item_equiped.png'

ind_lock_directory = 'res//ui//lock.png'

icon_medkit_directory = 'res//ui//icon_medkit.png'
icon_medkit_unable_directory = 'res//ui//icon_medkit_unable.png'

icon_grenade_upgrade_directory = 'res//ui//icon_grenade_upgrade.png'
icon_hp_upgrade_directory = 'res//ui//icon_hp_upgrade.png'
icon_regen_upgrade_directory = 'res//ui//icon_regeneration_upgrade.png'
icon_speed_upgrade_directory = 'res//ui//icon_speed_upgrade.png'
icon_double_jump_directory = 'res//ui//icon_double_jump.png'

hp_regen_directory = 'res//ui//hp_regen.png'

reward_directory = 'res//ui//reward.png'
reward_bg_directory = 'res//ui//reward_bg.png'
logo_directory = 'res//ui//logo.png'
ch_selected_directory = 'res//ui//ch_selected.png'
button_exit_mode_directory = 'res//ui//button_exit_mode.png'
button_home_mode_directory = 'res//ui//button_home_mode.png'
warning_directory = 'res//ui//warning.png'

mata_logo_directory = 'res//ui//mata_logo.png'

tutorial_directory = 'res//ui//tutorial.png'
tutorial_setting_directory = 'res//ui//tutorial_setting.png'

# 폰트 경로
font_directory = 'res//font//bump-it-up.ttf'
font2_directory = 'res//font//KORAIL2007.ttf'
font_splash_directory = 'res//font//Ubuntu-Title.ttf'

# 사운드 경로
# pistol
m1911_shoot_directory = 'res//sounds//pistol//m1911_shoot.ogg'
m92_shoot_directory = 'res//sounds//pistol//m92_shoot.ogg'
m500_shoot_directory = 'res//sounds//pistol//m500_shoot.ogg'
qhand_shoot_directory = 'res//sounds//pistol//qhand_shoot.ogg'
degle_shoot_directory = 'res//sounds//pistol//degle_shoot.ogg'

pistol_reload_directory = 'res//sounds//pistol//pistol_reload.ogg'
revolver_reload_directory = 'res//sounds//pistol//revolver_reload.ogg'

# smg
p90_shoot_directory = 'res//sounds//smg//p90_shoot.ogg'
vector_shoot_directory = 'res//sounds//smg//vector_shoot.ogg'
thompson_shoot_directory = 'res//sounds//smg//thompson_shoot.ogg'
aks74_shoot_directory = 'res//sounds//smg//aks74_shoot.ogg'
ump_shoot_directory = 'res//sounds//smg//ump_shoot.ogg'

smg_reload_directory = 'res//sounds//smg//smg_reload.ogg'

# ar
scar_shoot_directory = 'res//sounds//ar//scar_shoot.ogg'
m16_shoot_directory = 'res//sounds//ar//m16_shoot.ogg'
mp44_shoot_directory = 'res//sounds//ar//mp44_shoot.ogg'
aug_shoot_directory = 'res//sounds//ar//aug_shoot.ogg'
groza_shoot_directory = 'res//sounds//ar//groza_shoot.ogg'

ar_reload_directory = 'res//sounds//ar//ar_reload.ogg'

# rifle
m1_shoot_directory = 'res//sounds//rifle//m1_shoot.ogg'
win_shoot_directory = 'res//sounds//rifle//win_shoot.ogg'
win_spin_directory = 'res//sounds//rifle//win_spin.ogg'
win_reload_directory = 'res//sounds//rifle//win_reload.ogg'
mini14_shoot_directory = 'res//sounds//rifle//mini14_shoot.ogg'
fal_shoot_directory = 'res//sounds//rifle//fal_shoot.ogg'
lvoas_shoot_directory = 'res//sounds//rifle//lvoas_shoot.ogg'

rifle_reload_directory = 'res//sounds//rifle//rifle_reload.ogg'
m1_reload_directory = 'res//sounds//rifle//m1_reload.ogg'
m1_clip_sound_directory = 'res//sounds//rifle//m1_clip.ogg'
m1_clip_hit_directory = 'res//sounds//rifle//m1_clip_hit.ogg'
m1_reload_middle_directory = 'res//sounds//rifle//m1_reload_middle.ogg'

# sr
spring_shoot_directory = 'res//sounds//sr//spring_shoot.ogg'
spring_bolt_directory = 'res//sounds//sr//spring_bolt.ogg'
kar98_shoot_directory = 'res//sounds//sr//kar98_shoot.ogg'
kar98_bolt_directory = 'res//sounds//sr//kar98_bolt.ogg'
m24_shoot_directory = 'res//sounds//sr//m24_shoot.ogg'
m24_bolt_directory = 'res//sounds//sr//m24_bolt.ogg'
awp_shoot_directory = 'res//sounds//sr//awp_shoot.ogg'
awp_bolt_directory = 'res//sounds//sr//awp_bolt.ogg'
cheytac_shoot_directory = 'res//sounds//sr//cheytac_shoot.ogg'
cheytac_bolt_directory = 'res//sounds//sr//cheytac_bolt.ogg'
sr_reload_directory = 'res//sounds//sr//sr_reload.ogg'

# melee
knife_wield_directory = 'res//sounds//melee//knife_wield.ogg'
katana_wield_directory = 'res//sounds//melee//katana_wield.ogg'
katana_skill_sound_directory = 'res//sounds//melee//katana_slice.ogg'
bat_wield_directory = 'res//sounds//melee//axe_wield.ogg'
rapier_wield_directory = 'res//sounds//melee//rapier_wield.ogg'
rapier_rapid_directory = 'res//sounds//melee//rapier_rapid.ogg'
axe_wield_directory = 'res//sounds//melee//axe_wield.ogg'
axe_up_directory = 'res//sounds//melee//axe_up.ogg'
axe_hit_directory = 'res//sounds//melee//axe_hit.ogg'
melee_hit_directory = 'res//sounds//melee//melee_hit.ogg'
melee_hit2_directory = 'res//sounds//melee//melee_hit2.ogg'

# etc
shell_hit_directory = 'res//sounds//etc//shell_hit.ogg'
walk_directory = 'res//sounds//etc//walk.ogg'
land_directory = 'res//sounds//etc//land.ogg'
jump_directory = 'res//sounds//etc//jump.ogg'
damage_directory = 'res//sounds//etc//damage.ogg'
explode_sound_directory = 'res//sounds//etc//explode.ogg'
gren_hit_directory = 'res//sounds//etc//grenade_hit.ogg'
throw_directoy = 'res//sounds//etc//throw.ogg'
flesh_directory = 'res//sounds//etc//flesh.ogg'
arrow_wall_directory = 'res//sounds//etc//arrow_wall.ogg'
bow_sound_directory = 'res//sounds//etc//bow_shoot.ogg'
pickup_directory = 'res//sounds//etc//pickup.ogg'
dead_sound_directory = 'res//sounds//etc//dead.ogg'
weapon_change_sound_directory = 'res//sounds//etc//weapon_change.ogg'
medkit_sound_directory = 'res//sounds//etc//medkit.ogg'

title_sound1_directory = 'res//sounds//etc//title_sound1.ogg'
title_sound2_directory = 'res//sounds//etc//title_sound2.ogg'

# bgm
home_bgm_directory = 'res//sounds//bgm//home_bgm.mp3'
play_bgm_directory = 'res//sounds//bgm//play_bgm1.mp3'
play_bgm2_directory = 'res//sounds//bgm//play_bgm2.mp3'

# button
button_click_directory = 'res//sounds//button//button_click.ogg'
ch_change_directory = 'res//sounds//button//ch_change.ogg'
cant_buy_directory = 'res//sounds//button//cant_buy.ogg'
buy_ammo_directory = 'res//sounds//button//buy_ammo.ogg'
buy_medkit_directory = 'res//sounds//button//buy_medkit.ogg'
upgrade_sound_directory = 'res//sounds//button//upgrade.ogg'
select_gun_directory = 'res//sounds//button//select_gun.ogg'
select_melee_directory = 'res//sounds//button//select_melee.ogg'
buy_sound_directory = 'res//sounds//button//buy.ogg'

# splash
splash_center_directory = 'res//splash_image//splash_center.png'
