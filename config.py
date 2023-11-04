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
target_dot_directory = 'res//target_image//target_dot.png'
target_x_directory = 'res//target_image//mode_melee.png'
target_melee_directory = 'res//target_image//target_melee.png'

# 총 이미지 파일 경로 
scar_h_right_directory = 'res//gun_image//SCAR_H_right.png'
scar_h_left_directory = 'res//gun_image//SCAR_H_left.png'
m16_right_directory = 'res//gun_image//m16_right.png'
m16_left_directory = 'res//gun_image//m16_left.png'
mp44_right_directory = 'res//gun_image//mp44_right.png'
mp44_left_directory = 'res//gun_image//mp44_left.png'

# 불꽃 이미지 파일 경로
flame_right_directory = 'res//gun_image//flame_right.png'
flame_left_directory = 'res//gun_image//flame_left.png'

# 근접무기 이미지 경로
knife_right_directory = 'res//melee_image//knife_right.png'
knife_left_directory = 'res//melee_image//knife_left.png'

# 몬스터 이미지 파일 경로
type1_directory = 'res//monster_image//goblin_small.png'
type2_directory = 'res//monster_image//ghost_small.png'
type3_directory = 'res//monster_image//slime.png'
type4_directory = 'res//monster_image//apple.png'

# Prop 이미지 파일 경로
arrow_right_directory = 'res//prop//arrow_right.png'
arrow_left_directory = 'res//prop//arrow_left.png'

# ui 이미지 파일 경로
shop_window_directory = 'res//ui//shop_window.png'
pause_bg_directory = 'res//ui//pause_bg.png'
shop_button_directory = 'res//ui//shop_button.png'

# 폰트 경로
font_directory = 'bump-it-up.ttf'
