from .cell import Cell

class Grid:
    def __init__(self, width, height, cell_size, color, screen):
        self.cells = [[Cell(row, column, cell_size, color, screen)
                       for column in range(width)]
                      for row in range(height)]
        self.height = height
        self.width = width

    def __iter__(self):
        return iter(self.cells)

    def get_cell(self, row, column):

        return self.cells[row][column]

    def neighbors(self, cell):
        row = cell.row
        column = cell.column
        result = []

        if row > 0:
            result.append(("N", (self.cells[row-1][column])))
        if row < self.height - 1:
            result.append(("S", (self.cells[row+1][column])))
        if column > 0:
            result.append(("W", (self.cells[row][column-1])))
        if column < self.width - 1:
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
