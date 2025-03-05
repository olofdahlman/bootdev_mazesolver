# Main codeblock for bootdev guided maze solver project
# With the help of the boots AI, I managed to expand the sources for ubuntu dev packages to properly retrieve and install tcl, tk and lzma packages
# The sources are potentially drawn from non-open source libraries though - I do not believe they are, but I cannot be 100% certain
# This main file tkinter test does work but the tktiner_venv intrepreter was built during a previous tkinter test before the install issues were solved
from src.classes import *
win = Window(800, 600)
point1 = Point(1, 1)
point2 = Point(300, 300)
line = Line(point1, point2)  
win.draw_line(line, "red")  #These lines create a simple red line as a test
win.wait_for_close()

