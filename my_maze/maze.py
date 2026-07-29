from .grid import Grid
from .cell import Cell
import random


class Maze:
    """
    Generates a maze using a randomized dfs algorithm

    attributes:
    grid: Grid class, where the data is stored
    width: int, the width of the maze
    height: int, the height of the maze
    screen: pygame.Surface, the screen where the maze is stored
    color: tuple, background color of the maze
    """

    def __init__(self, width, height, cell_size, color, screen):
        self.grid = Grid(width, height, cell_size, color, screen)
        self.width = width
        self.height = height
        self.screen = screen
        self.color = color
        self.cell_size = cell_size

    def generate(self, start_row, start_column):
        # picks starting cell and starts dfs
        start = self.grid.get_cell(start_row, start_column)
        self.dfs(start)

    @staticmethod
    def remove_wall(cell, neighbor, direction):
        opposite = { "N" : "S", "S" : "N", "E" : "W", "W" : "E" }
        cell.walls[direction] = False
        neighbor.walls[opposite[direction]] = False

    def dfs(self, start):
        self.reset()
        call_stack = [start]
        start.visited = True

        while call_stack:
            current = call_stack[-1]

            neighbors = self.grid.neighbors(current)
            unvisited = [(d, n) for d, n in neighbors if not n.visited]

            if unvisited:
                direction, neighbor = random.choice(unvisited)

                self.remove_wall(current, neighbor, direction)

                neighbor.visited = True
                call_stack.append(neighbor)

            else:
                call_stack.pop()


    def reset(self):
        for row in self.grid.cells:
            for cell in row:
                cell.visited = False
                cell.walls = { "N" : True, "S" : True , "E" : True , "W" : True }


    def print(self):
        # ascii print
        print(self.grid.to_string())