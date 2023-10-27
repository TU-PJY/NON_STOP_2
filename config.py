# 환경 변수 파일 
from tkinter import *

# 현재 모니터 크기를 인식하여 자동으로 창 사이즈를 조정한다.
root = Tk()
HEIGHT = root.winfo_screenheight()
WIDTH = root.winfo_screenwidth()

JUMP_ACC = 5  # 점프 가속도
ACC_DELAY = 19  # 점프 가속도 변화 딜레이
LAND_SHAKE = 100  # 착지 시 맵이 눌리는 효과 수치
LAND_SHAKE_REDUCE = 2  # 맵이 눌린 뒤의 복구 속도

SCENE = ('intro', 'game_main', 'game')  # 씬 리스트. 각 씬마다 표시되는 화면이 달라진다.
GAME_SCENE = SCENE[2]

RECOIL_REDUCE = 1  # 조준점 복구 지연 속도
FLAME_DISPLAY_TIME = 10  # 총구 화염 출력 시간
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
target_melee_directory = 'res//target_image//mode_melee.png'

# 총 이미지 파일 경로 
scar_h_right_directory = 'res//gun_image//SCAR_H_right.png'
scar_h_left_directory = 'res//gun_image//SCAR_H_left.png'

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
arrow_right_directory = 'res//monster_image//arrow_right.png'
arrow_left_directory = 'res//monster_image//arrow_left.png'
