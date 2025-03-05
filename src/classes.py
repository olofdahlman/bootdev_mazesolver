#Here go all the different classes for the maze solver
from tkinter import Tk, BOTH, Canvas

#Main class that creates the graphical user interface (GUI) for the solver and creates a canvas widget inside of it for drawing of maze lines
class Window:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.__root = Tk()
        self.__root.title("Maze solver DRG")
        self.__canvas = Canvas(self.__root)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()

    def close(self):
        self.__running = False
        
    def draw_line(self, Line, fill_colour):
        Line.draw(self.__canvas, fill_colour)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, Canvas, fill_colour):
        Canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_colour, width=2)

