# 환경 변수 파일 

from tkinter import *

# 현재 모니터 크기를 인식하여 자동으로 창 사이즈를 조정한다.
root = Tk()
HEIGHT = root.winfo_screenheight()
WIDTH = root.winfo_screenwidth()

JUMP_ACC = 5  # 점프 가속도
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
FLAME_DISPLAY_TIME = 12  # 총구 화염 출력 시간
TARGET_DOT_DISPLAY_TIME = 10  # 조준점 내부에 빨간 점이 표시되는 시간

# 플레이어 이미지 파일 경로
player1_right_image_directory = 'res//player_image//player1_right.png'
player1_left_image_directory = 'res//player_image//player1_left.png'

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

# ui 이미지 파일 경로
shop_window_directory = 'res//ui//shop_window.png'
pause_bg_directory = 'res//ui//pause_bg.png'
shop_button_directory = 'res//ui//shop_button.png'
button_gun_directory = 'res//ui//button_gun.png'
button_melee_directory = 'res//ui//button_melee.png'
button_exp_directory = 'res//ui//button_exp.png'
button_page_directory = 'res//ui//page_button.png'
cursor_directory = 'res//ui//cursor.png'

ammo_ind_back_directory = 'res//ui//ammo_ind_back.png'
reload_bar_directory = 'res//ui//reload_bar.png'

# 몬스터 체력바 이미지 파일 경로
hp_back_directory = 'res//ui//hp_back.png'
hp_front_directory = 'res//ui//hp_front.png'

# 폰트 경로
font_directory = 'res//font//bump-it-up.ttf'
