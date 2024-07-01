from graphics import Cell
import time
import random


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
        seed=None
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
        self.seed = seed

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

    def _break_entrance_and_exit(self):
        # break top wall of top left = Entrance
        self._cells[0][0].TW = False
        self._draw_cells(0, 0)

        # break bottom wall of bottom right = Exit
        self._cells[self.num_cols - 1][self.num_rows - 1].BW = False
        self._draw_cells(self.num_cols - 1, self.num_rows - 1)

    def _break_walls_r(self, i, j):
        # marked current cell as visited
        current_cell = self._cells[i][j]
        current_cell.visited = True
        # infinite loop

        while True:
            cells_to_visit = []
            # keep track of adjacent cells that have not been visited from current cell
            if i < self.num_cols - 1 and self._cells[i+1][j].visited == False:
                cells_to_visit.append((i+1, j))
            if j < self.num_rows - 1 and self._cells[i][j+1].visited == False:
                cells_to_visit.append((i, j + 1))
            if i > 0 and self._cells[i - 1][j].visited == False:
                cells_to_visit.append((i-1, j))
            if j > 0 and self._cells[i][j - 1].visited == False:
                cells_to_visit.append((i, j-1))

            # check if there is a direction to go
            if len(cells_to_visit) == 0:
                self._draw_cells(i, j)
                return

            # choose direction to go next
            random_index = random.randint(0, len(cells_to_visit) - 1)
            next_index = cells_to_visit[random_index]

            # check which direction and remove walls between
            if next_index[0] == i + 1:
                current_cell.RW = False
                self._cells[i + 1][j].LW = False

            if next_index[0] == i - 1:
                current_cell.RW = False
                self._cells[i - 1][j].LW = False

            if next_index[1] == j + 1:
                current_cell.RW = False
                self._cells[i][j + 1].LW = False

            if next_index[1] == j - 1:
                current_cell.RW = False
                self._cells[i][j - 1].LW = False

            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for i in range(self.num_cols-1):
            for j in range(self.num_rows-1):
                self._cells[i][j].visited = False
