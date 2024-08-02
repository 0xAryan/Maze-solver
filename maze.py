from graphics import Point
from cell import Cell
import time

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []
        self._create_cells()
    def _create_cells(self):
        self.__cells = [[] for i in range(self.num_rows)]
        for column in range(len(self.__cells)):
            self.__cells[column] = [None for i in range(self.num_cols)]
        

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.__cells[i][j] = self._draw_cell(i, j)
        
        

    def _draw_cell(self, i, j):
        x1 = (i * self.cell_size_x) + self.x1
        y1 = (j * self.cell_size_y) + self.y1
        x2 = ((i + 1) * self.cell_size_x) + self.x1
        y2 = ((j + 1) * self.cell_size_y) + self.y1
        cell = Cell(self.win)
        cell.draw(x1, y1, x2, y2)
        self._animate()
        return cell
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
