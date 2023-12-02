from config import *
from game_class.weapon import *
from game_work import game_manager, game_framework
from mods import play_mode
from pop_ui_class.shop import Shop, Back3


def return_time():
    # 상점모드에서 소요된 시간을 다시 수류탄 사용 쿨타임에 반환
    play_mode.weapon.throw_delay = get_time() - play_mode.weapon.temp_time
    play_mode.weapon.skill_delay_rapier = get_time() - play_mode.weapon.skill_temp_rapier
    play_mode.weapon.skill_delay_katana = get_time() - play_mode.weapon.skill_temp_katana
    play_mode.weapon.skill_delay_axe = get_time() - play_mode.weapon.skill_temp_axe
    play_mode.p.medkit_delay = get_time() - play_mode.p.medkit_delay_temp


def handle_events():
    global exit_enable, shop, p, weapon
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYUP and event.key == SDLK_TAB:  # 모드 전환 직후 의도하지 않은 pop_mode 방지
            exit_enable = True
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE or event.key == SDLK_TAB:  # to play_mode
                if exit_enable:
                    return_time()
                    back3 = Back3()
                    game_manager.add_object(back3, 7)
                    game_framework.MODE = 'play'
                    game_framework.pop_mode()

            elif event.key == SDLK_d and shop.select_mode == 0:
                if shop.page < 2:
                    shop.page += 1

            elif event.key == SDLK_a and shop.select_mode == 0:
                if shop.page > 1:
                    shop.page -= 1

            elif event.key == SDLK_e:
                if shop.select_mode < 2:
                    shop.select_mode += 1

            elif event.key == SDLK_q:
                if shop.select_mode > 0:
                    shop.select_mode -= 1

            elif event.key == SDLK_LSHIFT:
                pass

            elif event.key == SDLK_r:
                pass

            if not event.key == SDLK_LCTRL:
                play_mode.p.handle_event(event)  # 상점 페이지 이동 키 사용 시 플레이어 상태 오류 방지

        elif event.type == SDL_MOUSEMOTION:
            shop.mx, shop.my = event.x, HEIGHT - 1 - event.y

        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            shop.click = True  # true일 시 상점창이 반응한다

        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_RIGHT:
            shop.right_click = True  # true일 시 상점창이 반응한다

        else:
            play_mode.p.handle_event(event)  # 이동키를 누른 상태로 모드 전환 시 동작 오류 방지
            play_mode.weapon.handle_event(event)  # 마우스 버튼을 누른 채로 모드 전환 시 동작 오류 방지


def init():
    global exit_enable, shop
    exit_enable = False
    shop = Shop()
    game_manager.add_object(shop, 7)


def update():
    game_manager.update()


def draw():
    clear_canvas()
    game_manager.render()
    update_canvas()


def finish():
    game_manager.remove_object(shop)
    pass


def pause():
    pass


def resume():
    pass
