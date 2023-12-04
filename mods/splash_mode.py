from pico2d import *
from config import *
from game_work import game_manager, game_framework
from mods import home_mode


class Image:
    def __init__(self):
        self.logo = load_image(logo_directory)
        self.bg = load_image(bg_image_directory)
        self.center = load_image(splash_center_directory)
        self.right = load_image(player4_left_image_directory)
        self.left = load_image(player5_right_image_directory)
        self.gun = load_image(awp_right_directory)
        self.rapier = load_image(rapier_directory)
        self.pistol = load_image(m500_left_directory)
        self.font = load_font(font_splash_directory, 30)
        self.font2 = load_font(font2_directory, 20)

    def draw(self):
        self.bg.draw(400, 20)
        self.right.draw(600, 60, 600, 600)
        self.left.draw(200, 60, 600, 600)
        self.pistol.rotate_draw(math.radians(-45), 580, 35, 400, 200)
        self.rapier.rotate_draw(math.radians(45), 250, 30, 550, 125)
        self.center.draw(400, 60, 600, 600)
        self.gun.rotate_draw(math.radians(-10), 370, 32, 600, 200)

        self.logo.draw(410, 230, 400, 200)

        self.font2.draw(10, 270, 'Powered by', (0, 0, 0))
        self.font2.draw(130, 272, 'Pico2D', (0, 0, 0))

    def update(self):
        pass


class Back:
    def __init__(self):
        self.image = load_image(front_directory)

    def draw(self):
        self.image.draw(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)

    def update(self):
        pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def init():
    global delay, image, back, delete_enable, resize_enable
    delete_enable = True
    resize_enable = True
    delay = 0
    back = Back()
    image = Image()

    game_manager.add_object(back, 7)
    game_manager.add_object(image, 7)


def update():
    global delay, delete_enable, resize_enable
    pps = game_framework.pps
    game_manager.update()
    delay += pps / 4

    if delay >= 800 and delete_enable:  # 화면 사이즈 변경 전 스플래쉬 이미지 삭제
        game_manager.remove_object(image)
        delete_enable = False

    if delay >= 850 and resize_enable:  # 화면 사이즈 변경
        set_position_canvas(0, 0, WIDTH, HEIGHT)
        resize_canvas(WIDTH, HEIGHT)
        resize_enable = False

    if delay >= 900:  # 홈 모드 진입
        game_framework.change_mode(home_mode)


def draw():
    clear_canvas()
    game_manager.render()
    update_canvas()


def finish():
    global back
    game_manager.remove_object(back)


def pause():
    pass


def resume():
    pass
