from graphics import Point
from cell import Cell
import time
import random

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None,
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.seed = seed
        if self.seed is not None:
            random.seed(seed)
        self._cells = []
        self._create_cells()


    def _create_cells(self):
        for i in range(self.num_cols):
            col_list = []
            for j in range(self.num_rows):
                col_list.append(Cell(self.win))
            self._cells.append(col_list)
        
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)



    def _draw_cell(self, i, j):
        if self.win is None:
            return
        x1 = (i * self.cell_size_x) + self.x1
        y1 = (j * self.cell_size_y) + self.y1
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        # time.sleep(0.05)

    def _break_entrance_and_exit(self):
        if len(self._cells):
            self._cells[0][0].has_top_wall = False
            self._draw_cell(0, 0)
            self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
            self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            l = []
            if j+1 in range(self.num_rows) and self._cells[i][j+1].visited == False:
                l.append(Point(i, j+1))
            if j-1 in range(self.num_rows) and self._cells[i][j-1].visited == False:
                l.append(Point(i, j-1))
            if i+1 in range(self.num_cols) and self._cells[i+1][j].visited == False:
                l.append(Point(i+1, j))
            if i-1 in range(self.num_cols) and self._cells[i-1][j].visited == False:
                l.append(Point(i-1, j))
        
            if len(l) == 0:
                self._draw_cell(i, j)
                return
            
            next_cell = random.choice(l)

            if next_cell.x == i:
                if next_cell.y == j+1:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i][j+1].has_top_wall = False
                else:
                    self._cells[i][j].has_top_wall = False
                    self._cells[i][j-1].has_bottom_wall = False

            
            if next_cell.y == j:
                if next_cell.x == i+1:
                    self._cells[i][j].has_right_wall = False
                    self._cells[i+1][j].has_left_wall = False
                else:
                    self._cells[i][j].has_left_wall = False
                    self._cells[i-1][j].has_right_wall = False
            
            self._draw_cell(i,j)

            self._break_walls_r(next_cell.x, next_cell.y)

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False
        
    def _dag(self):
        row = 0
        while row < self.num_rows:
            for col in range(self.num_cols):
                # print(f"[{col}][{row}] ", end='')
                print(f"{self._cells[col][row].visited} ", end='')
            print()
            row += 1
            