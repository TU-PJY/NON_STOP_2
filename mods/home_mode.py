from pico2d import *

from config import *
from game_work import game_manager, game_framework
from home_class.home_ui_class import Button, Background, Playerimage, Monsterimage, Cursor, Data, Start, Start2, Bgm, \
    Start3


def handle_events():
    global cursor, data, button, start
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            if not data.mode == 'loading_mode' and not data.mode == 'title_mode':
                match data.mode:
                    case 'home':
                        button.op3 = 0
                        button.kacc = 16 - (HEIGHT - 960) / 200
                        button.ky = -500 + (HEIGHT - 960)
                        button.deg = 0
                        data.mode = 'exit_mode'
                    case 'ch_mode':
                        data.mode = 'home'
                    case 'exit_mode':
                        data.mode = 'home'
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:  # 튜토리얼 상태에서 space를 누르면 게임으로 진행
            if data.mode == 'loading_mode' and data.first_play == 1 and start.tutorial_out:
                data_list = [
                    {"ch": data.ch, "first_play": 0}
                ]
                with open('data//player_data.json', 'w') as f:
                    json.dump(data_list, f)

                data.first_play = 0
                start.tutorial = False
                start.tutorial_out = False

        elif event.type == SDL_MOUSEMOTION:
            if not data.mode == 'loading_mode' and not data.mode == 'title_mode':
                cursor.mx, cursor.my = event.x, HEIGHT - 1 - event.y

        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if not data.mode == 'loading_mode' and not data.mode == 'title_mode':
                button.click = True


def init():
    global button, cursor, data, bgm, start

    with open('data//player_data.json', 'rb') as f:
        data_list = json.load(f)
        for d in data_list:
            data = Data()
            data.__dict__.update(d)

    bgm = Bgm(data)
    cursor = Cursor(data)
    button = Button(data, cursor)
    bg = Background(data, cursor)
    pimage = Playerimage(cursor, data)
    mimage = Monsterimage(cursor)
    start = Start(data)

    if game_framework.ANIMATION:  # true일때만 객체 삽입
        start2 = Start2()

    if game_framework.START:  # 게임 첫 실행때만 객체 삽입
        start3 = Start3(data)
        pass

    game_manager.add_object(bgm)
    game_manager.add_object(data, 0)
    game_manager.add_object(bg, 6)
    game_manager.add_object(pimage, 7)
    game_manager.add_object(mimage, 7)
    game_manager.add_object(button, 7)

    if game_framework.ANIMATION:
        game_manager.add_object(start2, 7)

    if game_framework.START:
        game_manager.add_object(start3, 7)

    game_manager.add_object(cursor, 7)
    game_manager.add_object(start, 7)


def update():
    game_manager.update()


def draw():
    clear_canvas()
    game_manager.render()
    update_canvas()


def finish():
    game_manager.clear()
    pass


def pause():
    pass


def resume():
    pass
