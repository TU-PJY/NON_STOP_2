from game_class.map import Map, BackGround, Wall
from game_class.monster_tool import Tool
from game_class.player import *
from game_class.prop import Start
from game_class.target import *
from game_class.weapon import *
from game_work import game_manager, game_framework
from mods import shop_mode, pause_mode
from pop_ui_class.ingame import Ingame


def save_cooltime():
    # 수류탄 쿨타임이 남아있다면 수류탄 쿨타임이 얼마나 남았는지를 저장
    weapon.temp_time = weapon.throw_delay_time
    # 각 근접무기의 스킬 사용 쿨타임을 저장한다
    weapon.skill_temp_rapier = weapon.skill_delay_time_rapier
    weapon.skill_temp_katana = weapon.skill_delay_time_katana
    weapon.skill_temp_axe = weapon.skill_delay_time_axe
    # 응급처치키트 사용 쿨타임을 저장한다
    p.medkit_delay_temp = p.medkit_delay_time


def handle_events():
    global p, weapon
    global mx, my

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            if p.cur_hp > 0:
                game_framework.MODE = 'pause'
                p.play_bgm.set_volume(12)
                save_cooltime()
                game_framework.push_mode(pause_mode)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_TAB:  # to_shop_mode
            if p.cur_hp > 0:
                save_cooltime()
                game_framework.MODE = 'shop'
                game_framework.push_mode(shop_mode)

        elif event.type == SDL_MOUSEMOTION:
            if p.cur_hp > 0:
                p.mx, p.my = event.x, HEIGHT - 1 - event.y

        else:
            p.handle_event(event)
            weapon.handle_event(event)


def init():
    global game, p, mp, bg, wall, weapon, target, tool, shop, ig
    game = []

    with open('data//player_data.json', 'rb') as f:
        data_list = json.load(f)
        for d in data_list:
            p = Player()
            p.__dict__.update(d)

    wall = Wall(p)
    bg = BackGround(p)
    mp = Map(p, wall, bg)
    weapon = Weapon(p, mp)
    target = Target(p, weapon)
    tool = Tool(p, weapon, target, mp)
    ig = Ingame(weapon, p)  # 인게임 ui
    s = Start()

    game_manager.add_collision_pair('player:monster', p, None)
    game_manager.add_collision_pair('weapon:monster', target, None)
    game_manager.add_collision_pair('player:arrow', p, None)
    game_manager.add_collision_pair('player:coin', p, None)

    game_manager.add_object(tool, 0)  # monster tool은 맨 아래 레이어에서 구동된다.
    game_manager.add_object(bg, 1)  # 몬스터는 2번 레이어에 추가된다
    game_manager.add_object(p, 3)
    game_manager.add_object(weapon, 3)
    game_manager.add_object(mp, 5)
    game_manager.add_object(wall, 6)
    game_manager.add_object(target, 7)
    game_manager.add_object(ig, 7)
    game_manager.add_object(s, 7)


def update():
    game_manager.update()
    game_manager.handle_collisions()


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


def weapon():
    return None
