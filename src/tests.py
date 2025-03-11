#File for unit tests for the maze solver - use "python tests.py" if you're running it in the terminal
from classes import *
import unittest

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )


    def test_maze_create_cells_uneven(self):
        num_cols = 4
        num_rows = 50
        maze = Maze(1, 1, num_rows, num_cols, 2, 10)
        self.assertEqual(
            len(maze._cells), num_cols
        )
        self.assertEqual(
            len(maze._cells[0]), num_rows
        )
    
    def test_maze_create_entrance_exit(self):
        num_cols = 12
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(maze._cells[0][0].has_top_wall, False)
        self.assertEqual(maze._cells[maze._num_cols - 1][maze._num_rows - 1].has_bottom_wall, False)

    def test_break_walls_r(self):
        num_cols = 12
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_cols, 10, 10, None, 0)
        rand_cell = maze._cells[random.randrange(num_cols) - 1][random.randrange(num_rows) - 1]
        self.assertEqual(rand_cell.visited, False)
        breaks = False
        if rand_cell.has_top_wall or rand_cell.has_right_wall or rand_cell.has_bottom_wall or rand_cell.has_left_wall == False:
            breaks = True
        self.assertEqual(breaks, True)

    def test_reset_visited_r(self):
        num_cols = 12
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_cols, 10, 10, None, 0)
        rand_cell = maze._cells[random.randrange(num_cols) - 1][random.randrange(num_rows) - 1]
        self.assertEqual(rand_cell.visited, False)



if __name__ == "__main__":
    unittest.main()
