from graphics import Line, Point



class Cell():
    def __init__(self, _win):
        
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = _win
    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self.has_top_wall:
            top_wall = Line(Point(x1, y1), Point(x2, y1))
            top_wall.draw(self._win)
        if self.has_left_wall:
            left_wall = Line(Point(x1, y1), Point(x1, y2))
            left_wall.draw(self._win)
        if self.has_bottom_wall:
            bottom_wall = Line(Point(x1, y2), Point(x2, y2))
            bottom_wall.draw(self._win)
        if self.has_right_wall:
            right_wall = Line(Point(x2, y1), Point(x2, y2))
            right_wall.draw(self._win)
         

