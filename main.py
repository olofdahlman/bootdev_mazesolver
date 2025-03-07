# Main codeblock for bootdev guided maze solver project
# With the help of the boots AI, I managed to expand the sources for ubuntu dev packages to properly retrieve and install tcl, tk and lzma packages
# The sources are potentially drawn from non-open source libraries though - I do not believe they are, but I cannot be 100% certain
# This main file tkinter test does work but the tktiner_venv intrepreter was built during a previous tkinter test before the install issues were solved
from src.classes import *

def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

    win.wait_for_close()


main()

