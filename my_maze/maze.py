from .grid import Grid
from .cell import Cell
import random


class Maze:
    def __init__(self, width, height, cell_size, color, screen):
        self.grid = Grid(width, height, cell_size, color, screen)
        self.width = width
        self.height = height
        self.screen = screen
        self.color = color

    def generate(self, start_row, start_column):
        start = self.grid.get_cell(start_row, start_column)
        self.dfs(start)

    def remove_walls(self, cell, neighbor, direction):
        opposite = { "N" : "S", "S" : "N", "E" : "W", "W" : "E" }
        cell.walls[direction] = False
        neighbor.walls[opposite[direction]] = False


    def dfs(self, start):
        self.reset()
        call_stack = [start]


        while call_stack:
            cell = call_stack.pop()
            if not cell.visited:
                cell.visited = True

            neighbors = self.grid.neighbors(cell)
            random.shuffle(neighbors)

            for direction, neighbor in neighbors:
                if not neighbor.visited:
                    self.remove_walls(cell, neighbor, direction)
                    call_stack.append(cell)
                    call_stack.append(neighbor)
                    break

    def reset(self):
        for row in self.grid.cells:
            for cell in row:
                cell.visited = False
                cell.walls = { "N" : True, "S" : True , "E" : True , "W" : True }


    def print(self):
        print(self.grid.to_string())