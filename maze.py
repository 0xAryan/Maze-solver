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
        time.sleep(0.05)

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
    
    # def solve(self):
    #     return self._solve_r(0, 0)
    
    # def _solve_r(self, i, j):
    #     self._animate()
    #     current_cell = self._cells[i][j]
    #     current_cell.visited = True
    #     if i == self.num_cols -1 and j == self.num_rows - 1 :
    #         return True
    #     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    #     for di, dj in directions:
    #         ni, nj = i + di, j + dj
    #         if ni in range(self.num_cols) and nj in range(self.num_rows):
    #             next_cell = self._cells[ni][nj]
    #             if not next_cell.visited:   
    #                 if ni == i:
    #                     if nj == j + 1:
    #                         if not current_cell.has_bottom_wall and not next_cell.has_top_wall:
    #                             current_cell.draw_move(next_cell)
    #                             res = self._solve_r(ni, nj)
    #                             if res:
    #                                 return True
    #                             else:
    #                                 current_cell.draw_move(next, undo=True)
    #                     else:
    #                         if not current_cell.has_top_wall and not next_cell.has_bottom_wall:
    #                             current_cell.draw_move(next_cell)
    #                             res = self._solve_r(ni, nj)
    #                             if res:
    #                                 return True
    #                             else:
    #                                 current_cell.draw_move(next_cell, undo=True)
    #                 if nj == j:
    #                     if ni == i + 1:
    #                         if not current_cell.has_right_wall and not next_cell.has_right_wall:
    #                             current_cell.draw_move(next_cell)
    #                             res = self._solve_r(ni, nj)
    #                             if res:
    #                                 return True
    #                             else:
    #                                 current_cell.draw_move(next_cell, undo=True)
    #                     else:
    #                         if not current_cell.has_left_wall and not next_cell.right_wall:
    #                             current_cell.draw(next_cell)
    #                             res = self._solve_r(ni, nj)
    #                             if res:
    #                                 return True
    #                             else:
    #                                 current_cell.draw_move(next, undo=True)
                
    #     return False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()  # Step 1: Animate the current step
        current_cell = self._cells[i][j]
        current_cell.visited = True # Step 2: Mark the current cell as visited

        # Step 3: Check if we've reached the goal
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True

        # Step 4: For each direction
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for di, dj in directions:
            ni, nj = i + di, j + dj

            # Step 1: Ensure the next cell is within bounds
            if 0 <= ni < self.num_cols and 0 <= nj < self.num_rows:
                next_cell = self._cells[ni][nj]

                # Step 1: Check if the next cell hasn't been visited and if there's no wall blocking the way
                if not next_cell.visited:
                    if (di == -1 and not current_cell.has_left_wall and not next_cell.has_right_wall) or \
                    (di == 1 and not current_cell.has_right_wall and not next_cell.has_left_wall) or \
                    (dj == -1 and not current_cell.has_top_wall and not next_cell.has_bottom_wall) or \
                    (dj == 1 and not current_cell.has_bottom_wall and not next_cell.has_top_wall):

                        # Step 1: Draw move and recursively solve the next cell
                        current_cell.draw_move(next_cell)
                        

                        # Step 2: recursively call _solve_r
                        if self._solve_r(ni, nj):
                            return True
                        else:
                            current_cell.draw_move(next_cell, undo=True)
        return False



    def _dag(self):
        row = 0
        while row < self.num_rows:
            for col in range(self.num_cols):
                # print(f"[{col}][{row}] ", end='')
                print(f"{self._cells[col][row].visited} ", end='')
            print()
            row += 1
            