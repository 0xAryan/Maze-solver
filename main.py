from graphics import Window, Line, Point
from cell import Cell
from maze import Maze





def main():
    win = Window(800, 600)

    # maze = Maze(
    #     100, 100,
    #     7, 5,
    #     100, 100,
    #     win
    # )
    maze = Maze(
        0, 0,
        8, 6,
        100, 100,
        win
    )

    maze._create_cells()

    win.wait_for_close()

main()