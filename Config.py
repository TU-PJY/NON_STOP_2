from tkinter import *

root = Tk()
HEIGHT = root.winfo_screenheight() # 현재 모니터 크기를 인식하여 자동으로 창 사이즈를 조정한다.
WIDTH = root.winfo_screenwidth()
JUMP_ACC = 5.0 #점프 가속도
JUMP_ACC_SPEED = 0.03125 #점프 가감속도 비율

commando_image_directory = 'res//commando.png'
land_image_directory = 'res//land.png'
bg_image_directory = 'res//bg.png'