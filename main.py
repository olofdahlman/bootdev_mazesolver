# Main codeblock for bootdev guided maze solver project
# With the help of the boots AI, I managed to expand the sources for ubuntu dev packages to properly retrieve and install tcl, tk and lzma packages
# The sources are potentially drawn from non-open source libraries though - I do not believe they are, but I cannot be 100% certain
# This main file tkinter test does work but the tktiner_venv intrepreter was built during a previous tkinter test before the install issues were solved
from src.classes import *
win = Window(800, 600)
point1 = Point(1, 10)
point2 = Point(75, 150)
line1 = Line(point1, point2)  
point3 = Point(50, 50)
point4 = Point(100, 100)
point5 = Point(120, 120)
cell1 = Cell(point3, point4, win)
cell2 = Cell(point4, point5, win)
win.draw_line(line1, "black")  #These lines create a simple red line as a test
win.draw_cell(cell1, "blue")
win.draw_cell(cell2, "blue")
cell1.draw_move(cell2)  #This creates a line between the centerpoints of cells 1 and 2
win.wait_for_close()

