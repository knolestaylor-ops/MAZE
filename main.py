import pygame
from my_maze.maze import Maze
from graphics.maze_graphics import MazeRenderer
from graphics.generation_graphics import GenerationGraphics
from solving.solver import Solver


RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

start_row = 0
start_column = 0
side_length = 50
running = True
background_color = GREEN
width, height = 800, 800

cell_size = width // side_length
maze = Maze(side_length, side_length, cell_size, background_color, screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)))
maze.generate(0, 0)

def init_maze():

    maze.print()
    return maze

def pygame_create_maze(maze):
    maze_renderer = MazeRenderer(maze)
    generation_graphics = GenerationGraphics(maze, RED)
    pygame.display.set_caption("Maze")
    route = solve_maze(maze)

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

def solve_maze(maze):
    start = maze.grid.get_cell(0,0)
    end = maze.grid.get_cell(side_length - 1,side_length - 1)
    solver = Solver(maze, start, end)

    route = solver.dfs_solve()
    print(f"route type: {type(route)}")
    print(route)
    return route





if __name__ == "__main__":
    pygame.init()
    pygame_create_maze(init_maze())
