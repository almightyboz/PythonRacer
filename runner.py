from die import Die
from python_racer import PythonRacer
from reset_screen import *

players = ["a", "b"]

die = Die()
game = PythonRacer(players, die)
reset_screen()
print die.roll()
print game.positions
# print game.board_visualization()
# equv of sleep(1)
print "yo"
game.finished_game()
