from pico2d import *

WIDTH, HEIGHT = 1200, 600
JUMP_ACC = 9
JUMP_ACC_SPEED = 0.125

class Commando:
    global WIDTH, HEIGHT, JUMP_ACC, JUMP_ACC_SPEED
    def __init__(self):
        self.image = load_image('commando.png')
        self.x, self.y, self.Dir = WIDTH / 2, 90, 1
        self.mv_right = False
        self.mv_left = False
        self.mv_jump = False
        self.jump_dir = 1 #1: up, #0: down
        self.jump_acc = JUMP_ACC

    def draw(self):
        if self.Dir == 1:
            self.image.clip_draw(0, 0, 100, 100, self.x, self.y, 70, 70)
        elif self.Dir == 0:
            self.image.clip_composite_draw(0, 0, 100, 100, 0, 'h', self.x, self.y, 70, 70)

    def move(self):
        if self.mv_right == True: #좌우 이동 
            self.x += 4
        if self.mv_left == True:
            self.x -= 4

        if self.mv_jump == True: #점프 
            if self.jump_dir == 1:
                self.y += self.jump_acc
                self.jump_acc -= JUMP_ACC_SPEED
                if self.jump_acc == -(JUMP_ACC + JUMP_ACC_SPEED): #점프 후 착지하면
                    self.mv_jump = False
                    self.jump_acc = JUMP_ACC
                
               
                
                

def handle_events():
    global running
    global mx, my
    global commando
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, HEIGHT - 1 - event.y
            if mx > commando.x:
                commando.Dir = 1
            elif mx < commando.x:
                commando.Dir = 0    

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_d:
                commando.mv_right = True

            elif event.key == SDLK_a:
                commando.mv_left = True

            elif event.key == SDLK_SPACE and commando.mv_jump == False:
                commando.mv_jump = True


        elif event.type == SDL_KEYUP:
            if event.key == SDLK_d:
                commando.mv_right = False 

            if event.key == SDLK_a:
                commando.mv_left = False        


def set_game():
    global running
    global commando
    running = True
    commando = Commando()

def update_game():
    commando.move()


def render():
    commando.draw()
    pass


open_canvas(WIDTH, HEIGHT)
set_game()

while running:
    clear_canvas()
    handle_events()
    render()
    update_game()
    update_canvas()

close_canvas()
