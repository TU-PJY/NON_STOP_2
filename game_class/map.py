from game_class_manager.map_manager import *


# Player move -> Map class


class Map:  # 땅
    def __init__(self, p, wall, bg):
        load_land(self)
        self.p = p
        self.wall = wall
        self.bg = bg

        self.x, self.y = WIDTH / 2, -50  # Map 자신이 그리는것은 land
        self.playerToWallRight, self.playerToWallLeft = self.p.x + 2048, self.p.x - 2048

    def draw(self):
        draw_land(self)

    def update(self):  # 이 함수에서 땅 끝과 플레이어 좌표가 일치하면 모든 맵 클래스의 스크롤이 멈춘다.
        if game_framework.MODE == 'play':
            update_map(self)
            restore_map_pos(self)

    def handle_event(self, event):
        pass


class Wall:  # 벽
    def __init__(self, p):
        load_wall(self)
        self.p = p
        self.x2 = WIDTH / 2 + 2048 + 640
        self.x1 = WIDTH / 2 - 2048 - 640
        self.y = HEIGHT / 2

    def draw(self):
        draw_wall(self)

    def update(self):
        pass

    def handle_event(self, event):
        pass


class BackGround:  # 배경
    def __init__(self, p):
        load_background(self)
        self.x, self.y = WIDTH / 2, HEIGHT / 2 - 25
        self.p = p

    def draw(self):
        draw_background(self)

    def update(self):
        pass

    def handle_event(self, event):
        pass
