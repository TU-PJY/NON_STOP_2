# 환경 변수 파일 
from tkinter import *

# 현재 모니터 크기를 인식하여 자동으로 창 사이즈를 조정한다.
root = Tk()
HEIGHT = root.winfo_screenheight()
WIDTH = root.winfo_screenwidth()

print(WIDTH, HEIGHT)

JUMP_ACC = 5.0  # 점프 가속도
ACC_DELAY = 25  # 점프 가속도 변화 딜레이
LAND_SHAKE = 50  # 착지 시 맵이 눌리는 효과 수치
LAND_SHAKE_REDUCE = 0.5  # 맵이 눌린 뒤의 복구 속도

SCENE = ('intro', 'main', 'game')  # 씬 리스트. 각 씬마다 표시되는 화면이 달라진다.
GAME_SCENE = SCENE[2]

RECOIL_REDUCE = 3  # 조준점 복구 지연 속도
FLAME_DISPLAY_TIME = 20  # 총구 화염 출력 시간

# 플레이어 이미지 파일 경로
commando_image_directory = 'res//commando.png'
commando_left_image_directory = 'res//commando_left.png'

# 배경 이미지 파일 경로
land_image_directory = 'res//land.png'
bg_image_directory = 'res//bg.png'
wall_image_directory = 'res//wall.png'

# 조준점 이미지 파일 경로 
target_up_directory = 'res//target_up.png'
target_down_directory = 'res//target_down.png'
target_right_directory = 'res//target_right.png'
target_left_directory = 'res//target_left.png'

# 총 이미지 파일 경로 
scar_h_right_directory = 'res//SCAR_H_right.png'
scar_h_left_directory = 'res//SCAR_H_left.png'

# 불꽃 이미지 파일 경로
flame_right_directory = 'res//flame_right.png'
flame_left_directory = 'res//flame_left.png'
