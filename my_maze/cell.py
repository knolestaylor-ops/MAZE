import pygame

RED = (255, 0, 0)


class Cell:
    def __init__(self, row, column, cell_size, color, screen):
        self.row = row
        self.column = column
        self.walls = {
            "N" : True,
            "S" : True,
            "E" : True,
            "W" : True,
        }
        self.visited = False
        self.cell_size = cell_size
        self.color = color
        self.screen = screen

    def get_walls(self):
        return list(self.walls.keys())

    def get_position(self):
        return self.row, self.column

    def draw(self):
        x = self.column * self.cell_size
        y = self.row * self.cell_size

        # Draw cell background (optional)
        pygame.draw.rect(self.screen, self.color, (x, y, self.cell_size, self.cell_size))

        # Draw walls
        if self.walls["N"]:
            pygame.draw.line(self.screen, RED, (x, y), (x + self.cell_size, y), 2)
        if self.walls["S"]:
            pygame.draw.line(self.screen, RED, (x, y + self.cell_size), (x + self.cell_size, y + self.cell_size), 2)
        if self.walls["W"]:
            pygame.draw.line(self.screen, RED, (x, y), (x, y + self.cell_size), 2)
        if self.walls["E"]:
            pygame.draw.line(self.screen, RED, (x + self.cell_size, y), (x + self.cell_size, y + self.cell_size), 2)
