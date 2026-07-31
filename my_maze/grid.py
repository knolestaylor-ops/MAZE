from .cell import Cell

class Grid:
    """
    Where the data lives, creates all the cells in a 2d list

    attributes:
    cells: 2d list, init the cells that the maze class will use
    height: integer, height of maze
    width: integer, width of maze

    """
    def __init__(self, width, height, cell_size, color, screen):
        self.cells = [[Cell(row, column, cell_size, color, screen)
                       for column in range(width)]
                      for row in range(height)]
        self.height = height
        self.width = width
        self.cell_size = cell_size

    def __iter__(self):
        return iter(self.cells)

    def get_cell(self, row, column):
        return self.cells[row][column]

    def get_cellsize(self):
        return self.cell_size

    def neighbors(self, cell):
        row = cell.row
        column = cell.column
        result = []

        if  cell.walls["N"] and row > 0:
            result.append(("N", (self.cells[row-1][column])))
        if  cell.walls["S"] and row < self.height - 1:
            result.append(("S", (self.cells[row+1][column])))
        if  cell.walls["W"] and column > 0:
            result.append(("W", (self.cells[row][column-1])))
        if  cell.walls["E"] and column < self.width - 1:
            result.append(("E", (self.cells[row][column+1])))

        return result

    def to_string(self):
        output = ""

        # Top border
        output += "+" + "---+" * self.width + "\n"

        for row in self.cells:
            # Row of cells: draw west/east walls
            top = "|"
            bottom = "+"

            for cell in row:
                # Cell interior
                top += "    " if not cell.walls["E"] else "   |"

                # South wall
                bottom += "---+" if cell.walls["S"] else "   +"

            output += top + "\n"
            output += bottom + "\n"

        return output
