from pico2d import *

from config import *
from game_work import game_framework
from mods import play_mode as start_mode

open_canvas(WIDTH, HEIGHT)
hide_cursor()
hide_lattice()

game_framework.run(start_mode)

close_canvas()
