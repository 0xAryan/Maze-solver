import unittest
from maze import Maze

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

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test__break_entrance_and_exit(self):
        m = Maze(0, 0, 6, 8, 100, 100)
        m._create_cells()
        m._break_entrance_and_exit()
        self.assertEqual(m._cells[0][0].has_top_wall, False)
        self.assertEqual(m._cells[7][5].has_bottom_wall, False)


if __name__ == "__main__":
    unittest.main()

