import pygame
from my_maze.maze import Maze
from graphics.maze_graphics import MazeRenderer


RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

start_row = 0
start_column = 0
side_length = 160
cell_size = 5
running = True
background_color = GREEN

width = cell_size * side_length
height = cell_size * side_length


def init_maze():
    maze = Maze(side_length, side_length, cell_size, background_color, screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)))
    maze.generate(0, 0)

    for r, row in enumerate(maze.grid.cells):
        for c, cell in enumerate(row):
            print(f"grid[{r}][{c}] -> cell at ({cell.row}, {cell.column})")

    maze.print()
    return maze

def pygame_create_maze(maze):
    maze_renderer = MazeRenderer(maze)
    pygame.display.set_caption("Maze")

    clock = pygame.time.Clock()
    FPS = 60

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        maze_renderer.draw()

        pygame.display.flip()

        clock.tick(FPS)
    pygame.quit()



if __name__ == "__main__":
    pygame.init()
    pygame_create_maze(init_maze())