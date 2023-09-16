from graphics import Line, Point


class Cell:
    def __init__(self, win = None):
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
            self._win.draw_line(line, "aquamarine4")

        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "aquamarine4")
        
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "aquamarine4")
        
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "aquamarine4")

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        self_midx = (self._x1 + self._x2)/2
        self_midy = (self._y1 + self._y2)/2
        
        to_cell_midx = (to_cell._x1 + to_cell._x2)/2
        to_cell_midy = (to_cell._y1 + to_cell._y2)/2

        fill_color = "white"
        if undo:
            fill_color = 'gray'

        #Move left
        if self._x1 > to_cell._x1:
            line = Line(Point(self._x1, self_midy), Point(self_midx, self_midy))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_cell_midx, to_cell_midy), Point(to_cell._x2, to_cell_midy))
            self._win.draw_line(line, fill_color)

        #Move right
        if self._x1 < to_cell._x1:
            line = Line(Point(self_midx, self_midy), Point(self._x2, self_midy))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_cell._x1, to_cell_midy), Point(to_cell_midx, to_cell_midy))
            self._win.draw_line(line, fill_color)

        #Move up
        if self._y1 > to_cell._y1:
            line = Line(Point(self_midx, self_midy), Point(self_midx, self._y1))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_cell_midx, to_cell._y2), Point(to_cell_midx, to_cell_midy))
            self._win.draw_line(line, fill_color)

        #Move down
        if self._y1 < to_cell._y1:
            line = Line(Point(self_midx, self_midy), Point(self_midx , self._y2))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_cell_midx, to_cell_midy), Point(to_cell_midx, to_cell._y1))
            self._win.draw_line(line, fill_color)

