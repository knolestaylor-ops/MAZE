from my_maze.cell import Cell
from solving.solver import Solver
import pygame
"""
Uses pygame to draw the path that the maze solver created

attributes:
maze, current maze state

"""

class GenerationGraphics:
    def __init__(self, maze,  color):
        self.maze = maze
        self.grid = maze.grid
        self.color = color

    def draw_path(self, path):
        cell_size = self.maze.cell_size
        for cell in path:
            x = cell.get_column() * cell_size
            y = cell.get_row() * cell_size
            pygame.draw.rect(self.maze.screen, self.color, (x, y, cell_size , cell_size ))