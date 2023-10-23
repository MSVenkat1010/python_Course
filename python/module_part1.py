# game.py
# import the draw module
import draw

def play_game():
    ...

def main():
    result = play_game()
    draw.draw_game(result)

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()

"""
# game.py
# import the draw module
from draw import draw_game

def main():
    result = play_game()
    draw_game(result)

# game.py
# import the draw module
from draw import *

def main():
    result = play_game()
    draw_game(result)
#alternate import
    
sys.path.append("/foo")
This executes game.py, and enables the script to load modules from the foo directory, as well as the local directory.

You may also use the sys.path.append function. Execute it before running the import command:
"""