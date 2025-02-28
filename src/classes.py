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
        
