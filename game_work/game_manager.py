# 게임 월드의 표현
game = [[], [], [], [], [], [], [], []]
spawn_time = 0


def add_object(o, depth=0):
    game[depth].append(o)  # 지정된 깊이의 레이어에 객체 추가


def update():
    for layer in game:
        for o in layer:
            o.update()


def render():
    for layer in game:
        for o in layer:
            o.draw()


def remove_object(o):
    for layer in game:
        if o in layer:
            layer.remove(o)
            return
    raise ValueError('remove err')
