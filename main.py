from tkinter import Tk, BOTH, Canvas
from graphics import Window, Line, Point, Cell


def main():
    win = Window(800, 600)
    c1 = Cell(True, False, True, False, 100, 300, 100, 300, win)
    c1.draw("black")
    c2 = Cell(False, True, True, True, 300, 500, 100, 300, win)
    c2.draw("black")
    c1.draw_move(c2)
    win.wait_for_close()


main()
