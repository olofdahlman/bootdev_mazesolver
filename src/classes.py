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
    
    def draw_cell(self, Cell, fill_colour):
        Cell.draw(self.__canvas, fill_colour)


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


class Cell:
    def __init__(self, point1, point2, window):  #Supply two point class entries (the points of two opposite corners) and a window class entity onto which the cell can be drawn
        self.left_exists = True
        self.right_exists = True
        self.top_exists = True
        self.bottom_exists = True
        self.__x1 = point1.x
        self.__y1 = point1.y    #Upper left point
        self.__x2 = point2.x
        self.__y2 = point2.y    #Lower right point
        self.__win = window
    
    def draw(self, Canvas, fill_colour):
        if self.left_exists:
            Canvas.create_line(self.__x1, self.__y1, self.__x1, self.__y2, fill=fill_colour, width=2) #The idea is that things are drawn from the top left of the window towards the bottom right
        if self.top_exists:
            Canvas.create_line(self.__x1, self.__y1, self.__x2, self.__y1, fill=fill_colour, width=2)
        if self.right_exists:
            Canvas.create_line(self.__x2, self.__y1, self.__x2, self.__y2, fill=fill_colour, width=2)
        if self.bottom_exists:
            Canvas.create_line(self.__x2, self.__y2, self.__x1, self.__y2, fill=fill_colour, width=2)

    def draw_move(self, to_cell, undo=False):
        if undo:
            fill_colour = "gray"
        else:
            fill_colour = "red"
        
        cell_center_x = (self.__x2 + self.__x1)/2
        cell_center_y = (self.__y2 + self.__y1)/2
        cell_center = Point(cell_center_x, cell_center_y)

        to_cell_center_x = (to_cell.__x2 + to_cell.__x1)/2
        to_cell_center_y = (to_cell.__y2 + to_cell.__y1)/2
        to_cell_center = Point(to_cell_center_x, to_cell_center_y)

        cell_to_cell_line = Line(cell_center, to_cell_center)
        self.__win.draw_line(cell_to_cell_line, fill_colour)