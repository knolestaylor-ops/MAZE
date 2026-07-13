import pygame

from my_maze.maze import Maze
from graphics.maze_graphics import MazeRenderer



start_row = 0
start_column = 0
side_length = 5
cell_size = 5
running = True
RED = (255, 0, 0)
color = RED

width = cell_size * side_length
height = cell_size * side_length

maze = Maze(side_length, side_length, cell_size, color, screen = pygame.display.set_mode((width, height)))
maze.generate(0, 0)

for r, row in enumerate(maze.grid.cells):
    for c, cell in enumerate(row):
        print(f"grid[{r}][{c}] -> cell at ({cell.row}, {cell.column})")
maze.print()



