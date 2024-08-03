from graphics import Window, Line, Point
from cell import Cell
from maze import Maze





def main():
    win = Window(820, 620)

    # maze = Maze(
    #     100, 100,
    #     7, 5,
    #     100, 100,
    #     win
    # )
    maze = Maze(
        10, 10,
        6, 8,
        100, 100,
        win
    )
    # maze = Maze(
    #     10, 10,
    #     6, 8,
    #     95, 95,
    #     win
    # )

    maze._create_cells()
    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)
    maze._reset_cells_visited()
    maze._dag()
    win.wait_for_close()

main()