from pico2d import *

from config import *
from game_work import game_framework
from mods import splash_mode as start_mode

open_canvas(800, 300)
# open_canvas(WIDTH, HEIGHT)
hide_cursor()
hide_lattice()

game_framework.run(start_mode)

close_canvas()
