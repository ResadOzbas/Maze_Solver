from tkinter import Tk, BOTH, Canvas

# Window class, has width, height, title, canvas and running


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Window")
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
# need to tell the window to redraw for when it should render visual

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
# keeps running redraw until running is not True

    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.redraw()
# stops redraw

    def close(self):
        self.running = False

# draws line
    def draw_line(self, line, fill_colour):
        line.draw(self.canvas, fill_colour)

# Point class has two coordinates


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Line class also has two points
class Line:
    def __init__(
        self,
        p1,
        p2,
    ):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_colour="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_colour, width=2
        )

# Cell class, LW= has left wall? RW = has right wall? ...


class Cell:
    def __init__(self, LW, RW, TW, BW, x1, x2, y1, y2, win=None):
        self.LW = LW
        self.RW = RW
        self.TW = TW
        self.BW = BW
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.win = win

# x1 y1 top left corner, x2 y2 bottom right corner y1 > y2
# if LW == true, create line x1 y1 -> x1 y2 ...
    def draw(self, fill_colour="black"):
        if self.win is None:
            return
        LW_line = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
        RW_line = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
        TW_line = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
        BW_line = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))

        if self.LW:
            self.win.draw_line(LW_line, fill_colour)
        else:
            self.win.draw_line(LW_line, "#D9D9D9")

        if self.RW:
            self.win.draw_line(RW_line, fill_colour)
        else:
            self.win.draw_line(RW_line, "#D9D9D9")

        if self.TW:
            self.win.draw_line(TW_line, fill_colour)
        else:
            self.win.draw_line(TW_line, "#D9D9D9")

        if self.BW:
            self.win.draw_line(BW_line, fill_colour)
        else:
            self.win.draw_line(BW_line, "#D9D9D9")

# draws a path from the center of one cell to the next

    def draw_move(self, to_cell, undo=False):
        if undo == False:
            colour = "red"
        else:
            colour = "gray"

        half_point1 = abs(self.x2 - self.x1)//2
        x_center1 = half_point1 + self.x1
        y_center1 = half_point1 + self.y1

        half_point2 = abs(to_cell.x2 - to_cell.x1)//2
        x_center2 = half_point2 + to_cell.x1
        y_center2 = half_point2 + to_cell.y1

        mid_cell1 = Point(x_center1, y_center1)
        mid_cell2 = Point(x_center2, y_center2)

        l = Line(mid_cell1, mid_cell2)
        self.win.draw_line(l, colour)
