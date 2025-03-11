#Here go all the different classes for the maze solver
from tkinter import Tk, BOTH, Canvas
import time, random

#Main class that creates the graphical user interface (GUI) for the solver and creates a canvas widget inside of it for drawing of maze lines
class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(
        self,
        p1,
        p2,
    ):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )
    
    def draw_center_line(self, canvas, fill_color="blue"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1

        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_length2 + to_cell._x1
        y_center2 = half_length2 + to_cell._y1

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self._win.draw_line(line, fill_color)

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            self._seed = random.seed(seed)
        self._solve_path = {}
        self._solve_path_found = False

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.025)

    def _break_entrance_and_exit(self):     #Opens the entrance and exit walls
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):         #Creates the path through the maze
        self._cells[i][j].visited = True

        while True:                #This section checks if the prospective next cell is within bounds and if it hasen't been visited for all neighbours
            adjacent_cells = []
            if self._num_cols - 1 > i:
                if self._cells[i + 1][j].visited == False:
                    adjacent_cells.append([i + 1, j])
            if 0 < i:
                if self._cells[i - 1][j].visited == False:
                    adjacent_cells.append([i - 1, j])
            if self._num_rows - 1 > j:
                if self._cells[i][j + 1].visited == False:
                    adjacent_cells.append([i, j + 1])
            if 0 < j:
                if self._cells[i][j - 1].visited == False:
                    adjacent_cells.append([i, j - 1])

            if not adjacent_cells:          #The cell lists updates every iteration and if there are none to add, this cell eliminates itself
                self._draw_cell(i, j)
                return

            random_num = random.randrange(len(adjacent_cells))
            random_dir = adjacent_cells[random_num]     #Randomly select an adjacent cell to visit

            if i + 1 == random_dir[0]:              #depending on which neighbour was visited, destroy the wall separating them
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            if i - 1 == random_dir[0]:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            if j + 1 == random_dir[1]:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            if j - 1 == random_dir[1]:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_walls_r(random_dir[0], random_dir[1])       #Recursively call the method untill all cells have been visited, which ends the method call
                
    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        i = 0
        j = 0
        self._solve_r(i, j)
        if self._solve_path_found:
            path_solved = []
            path_solved.append([self._num_cols, self._num_rows])    #Immediately append the maze exit - has to be found if solve_path_found is True
            while self._solve_path:
                for cell in self._solve_path:   #This part is intended to iterate over the dictionary untill it finds the preceeding cell
                    a = cell[:1]                #This will not work because the path can run right next to itself while still having a wall - add a wall-checking part
                    b = cell[1:]
                    if (a + 1 == path_solved[-1][0] or a - 1 == path_solved[-1][0]) ^ (b + 1 == path_solved[-1][1] or b - 1 == path_solved[-1][1]):
                        path_solved.append(self._solve_path[cell])
                        del self._solve_path[cell]
            


        else:
            return False
        

    def _solve_r(self, i, j):       #This function should use the method-specific variables path_found and path to log the path travelled and if the end has been found
        self._cells[i][j].visited = True
        if i == self._num_cols and j == self._num_rows:
            self._solve_path_found = True       #If the end path is found, this will ensure the program stops checking and the path can processed in solve method

        while not self._solve_path_found:
            adjacent_cells = []
            string = f"{i}" + f"{j}"    #Creating a unique key id from the two integers - due to the maze setup, they SHOULD be unique
            self._solve_path.update({string : [i, j]})  #Use the unique key to store the corresponding cell list coordinate - the key allows them to be sorted later
            if self._num_cols - 1 > i:                     #Could potentially just create a mirrored maze list by creating new cell class objects?
                if self._cells[i + 1][j].visited == False and self._cells[i][j].has_right_wall == False:
                    adjacent_cells.append([i + 1, j])
            if 0 < i:
                if self._cells[i - 1][j].visited == False and self._cells[i][j].has_left_wall == False:
                    adjacent_cells.append([i - 1, j])
            if self._num_rows - 1 > j:
                if self._cells[i][j + 1].visited == False and self._cells[i][j].has_top_wall == False:
                    adjacent_cells.append([i, j + 1])
            if 0 < j:
                if self._cells[i][j - 1].visited == False and self._cells[i][j].has_bottom_wall == False:
                    adjacent_cells.append([i, j - 1])

            if not adjacent_cells:      #Designed so that dead-end cells self-filter themselves out of the final path
                del self._solve_path[string]
                
                return
            
            random_num = random.randrange(len(adjacent_cells))
            random_dir = adjacent_cells[random_num]
            self._solve_r(random_dir[0], random_dir[1])     #Same random cell selection and recursive method call as in the wall breaking method




  