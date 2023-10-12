from tkinter import *

# 현재 모니터 크기를 인식하여 자동으로 창 사이즈를 조정한다.
root = Tk()
HEIGHT = root.winfo_screenheight()
WIDTH = root.winfo_screenwidth()
print(WIDTH, HEIGHT)

JUMP_ACC = 5.0  # 점프 가속도
JUMP_ACC_SPEED = 0.03125  # 점프 가속도 변화량

SCENE = ('intro', 'main', 'game')  # 씬 리스트. 각 씬마다 표시되는 화면이 달라진다.
GAME_SCENE = SCENE[2]

# 이미지 파일 경로
commando_image_directory = 'res//commando.png'
land_image_directory = 'res//land.png'
bg_image_directory = 'res//bg.png'
wall_image_directory = 'res//wall.png'
