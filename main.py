from tkinter import Tk, BOTH, Canvas
from graphics import Window, Line, Point, Cell


def main():
    win = Window(800, 600)
    c = Cell(True, False, True, False, 100, 300, 100, 300, win)
    c.draw("black")
    c = Cell(False, True, True, True, 300, 500, 100, 300, win)
    c.draw("black")
    win.wait_for_close()


main()
