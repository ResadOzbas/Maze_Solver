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
    def __init__(self, LW, RW, TW, BW, x1, x2, y1, y2, win):
        self.LW = LW
        self.RW = RW
        self.TW = TW
        self.BW = BW
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.win = win

# x1 y1 top left corner, x2 y2 bottom right corner
# if LW == true, create line x1 y1 -> x1 y2 ...
    def draw(self, fill_colour="black"):
        if self.LW:
            l = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.win.draw_line(l, fill_colour)
        if self.RW:
            l = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.win.draw_line(l, fill_colour)
        if self.TW:
            l = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.win.draw_line(l, fill_colour)
        if self.BW:
            l = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.win.draw_line(l, fill_colour)
