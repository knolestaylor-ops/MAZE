"""
Maze solving class, will allow you to select a solving algorithm, and then complete it

attributes:
maze: maze object, holds the current maze state
start: where the solving algorithm starts
end: where the solving algorithm ends
algorithm: what algorithm is being used to solve


"""
import random


class Solver:
    def __init__(self, maze, start, end):
        self.maze = maze
        self.start = start
        self.end = end
        self.algorithm = None


    def dfs_solve(self):
        came_from = {self.start: None}
        call_stack = [self.start]

        while call_stack:
            current = call_stack[-1]

            if current == self.end:
                return self.reconstruct_path(came_from)

            open_passages = self.maze.grid.clear_cells(current)

            if open_passages:
                direction, passage = random.choice(open_passages)
                passage.visited = True
                call_stack.append(passage)
                came_from[passage] = current
            else:
                call_stack.pop()
                came_from.pop(current, None)
        return None

    @staticmethod
    def reconstruct_path(came_from):
        path = []

        for cell in came_from:
            path.append(cell)

        print(path)
        return path









