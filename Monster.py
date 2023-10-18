class Monster:
    def __init__(self, p, target):
        self.p, self.target = p, target
        self.list = []
        self.number = 0  # 몬스터 수
        self.type = 0
        self.hp = 0
        self.speed = 0
        self.x, y = 0, 0

        self.spawn_time = 300  # 이 변수가 0이 될 때마다 몬스터가 스폰된다.

        self.simulate = False  # 사망 시 True가 되어 바닥 및 벽에 튕기는 물리 시뮬레이션 사용
        self.right = False  # True일 경우 우측으로 날아감, False일 경우 왼쪽으로 날아감.
        self.up, self.fall = False, False  # 물리 시뮬레이션 실행 시 사용하는 올라감 및 떨어짐 여부

    def draw(self):
        pass

    def update(self):
        pass

    def handle_events(self):
        pass



