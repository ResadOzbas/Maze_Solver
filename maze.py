from graphics import Cell
import time


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):

        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for col in range(self.num_cols):
            col_cells = []
            for row in range(self.num_rows):

                cell_start_x = self.x1 + col * self.cell_size_x
                cell_start_y = self.y1 + row * self.cell_size_y
                cell_end_x = cell_start_x + self.cell_size_x
                cell_end_y = cell_start_y + self.cell_size_y

                new_cell = Cell(True, True, True, True, cell_start_x,
                                cell_end_x, cell_start_y, cell_end_y, self.win)
                col_cells.append(new_cell)

            self._cells.append(col_cells)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cells(i, j)

    def _draw_cells(self, i, j):
        if self.win is None:
            return
        # Draw the cell
        self._cells[i][j].draw()

        # Call the animate method
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.01)
