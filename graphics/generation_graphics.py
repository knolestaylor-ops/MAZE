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
        self.screen = maze.screen
        self.grid = maze.grid
        self.color = color

    def draw_path(self, cell):
        padding = 3
        cell_size = cell.cell_size
        x = cell.get_column() * cell_size
        y = cell.get_row() * cell_size
        pygame.draw.rect(self.screen, self.color,(x + padding, y + padding, cell_size - 2 * padding, cell_size - 2 * padding))
