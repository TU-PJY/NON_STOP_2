from pico2d import *

from config import *
from game_work import game_framework
from mods import home_mode, gameover_mode, play_mode


class Playerdead:
    def __init__(self):
        self.front = load_image(front_directory)
        self.font = load_font(font_directory, 100)
        self.size = 0

        self.x1 = 0
        self.x2 = WIDTH
        self.acc = 0
        self.delay = 0

        self.front_size = WIDTH / 2

    def draw(self):
        self.front.draw(self.x1 + self.front_size / 2, HEIGHT / 2, self.front_size, HEIGHT)
        self.front.draw(self.x2 - self.front_size / 2, HEIGHT / 2, self.front_size, HEIGHT)

        self.font.draw(self.x1 + self.front_size - 450, HEIGHT / 2, 'GAME', (172, 162, 132))
        self.font.draw(self.x2 - self.front_size + 20, HEIGHT / 2, 'OVER', (172, 162, 132))

    def update(self):
        pps = game_framework.pps
        if self.delay < 600:
            self.delay += pps / 3

        if self.delay > 600:
            if self.front_size > 0:
                self.front_size -= self.acc * pps / 4
                self.acc += pps / 100

    def handle_event(self):
        pass


class Reward:
    def __init__(self, cursor):
        self.back = load_image(reward_bg_directory)
        self.image = load_image(reward_directory)
        self.button = load_image(ammo_ind_back_directory)
        self.font = load_font(font2_directory, 60)
        self.font2 = load_font(font_directory, 40)
        self.font3 = load_font(font_directory, 20)
        self.click = False
        self.op = 0
        self.cursor = cursor
        self.highscore = False  # 이전 최고 기록과 비교하여 현재 기록이 더 높으면 True가 되어 최고 기록을 갱신한다

        self.total_rounds = play_mode.tool.rounds

    def __getstate__(self):
        state = {'max_rounds': self.max_rounds}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def draw(self):
        self.back.draw(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
        self.image.draw(WIDTH / 2 + 40, HEIGHT - 200, 1000, 600)
        self.button.opacify(self.op)
        self.font2.draw(WIDTH / 2 - 270, HEIGHT / 2, 'TOTAL ROUNDS: %d' % self.total_rounds, (255, 255, 255))
        self.button.draw(WIDTH / 2, 200, 500, 100)
        self.font.draw(WIDTH / 2 - 220, 200, '홈으로 돌아가기', (255, 255, 255))

        if self.highscore:
            self.font3.draw(WIDTH / 2 - 270, HEIGHT / 2 - 50, 'HIGHSCORE!', (255, 255, 0))

        else:
            self.font3.draw(WIDTH / 2 - 270, HEIGHT / 2 - 50, 'HIGHSCORE: %d' % self.max_rounds, (255, 255, 255))

    def update(self):
        pps = game_framework.pps

        if self.max_rounds < self.total_rounds:  # 이전 최고 기록과 비교하여 최고 기록을 넘었다면 데이터 갱신
            self.highscore = True
            data = [
                {"max_rounds": self.total_rounds}
            ]
            with open('data//rounds_data.json', 'w') as f:
                json.dump(data, f)

        if gameover_mode.playerdead.front_size < 0:
            if WIDTH / 2 - 250 < self.cursor.mx < WIDTH / 2 + 250 and 150 < self.cursor.my < 250:
                self.op += pps / 50
                if self.op > 1:
                    self.op = 1
            else:
                self.op -= pps / 50
                if self.op < 0:
                    self.op = 0

            if self.click:
                if WIDTH / 2 - 250 < self.cursor.mx < WIDTH / 2 + 250 and 150 < self.cursor.my < 250:
                    game_framework.MODE = 'home'
                    game_framework.ANIMATION = False
                    game_framework.change_mode(home_mode)

                else:
                    self.click = False
        else:
            self.click = False

    def handle_event(self):
        pass


class Cursor:
    def __init__(self):
        self.image = load_image(cursor_directory)
        self.mx, self.my = 0, 0

    def draw(self):
        self.image.draw(self.mx + 35, self.my - 35, 70, 70)

    def update(self):
        pass
