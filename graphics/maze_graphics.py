import pygame



class MazeRenderer:
    def __init__(self, maze):
        pygame.init()
        self.maze = maze
        self.width = maze.width
        self.height = maze.height
        self.screen = maze.screen
        self.color = maze.color

    def draw(self):
        self.screen.fill((0, 0, 0))
        for row in self.maze.grid:
            for cell in row:
                cell.draw()
        pygame.display.flip()