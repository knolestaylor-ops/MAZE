"""
Maze solving class, will allow you to select a solving algorithm, and then complete it"

attributes:
maze: maze object, holds the current maze state
start: where the solving algorithm starts
end: where the solving algorithm ends
algorithm: what algorithm is being used to solve


"""

class Solver:
    def __init__(self, maze, start, end):
        self.maze = maze
        self.start = start
        self.end = end
        self.algorithm = None


    def dfs_solve(self):

        came_from = {self.start: None}
        visited = {self.start}
        call_stack = [self.start]

        while call_stack:
            cell = call_stack.pop()

            if cell == self.end:
                return self.reconstruct_path(came_from)

            neighbors = self.maze.grid.neighbors(cell)

            for direction, neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    came_from[neighbor] = cell
                    call_stack.append(neighbor)
        return None

    def reconstruct_path(self, came_from):
        path = []
        current = self.end

        while current:
            path.append(current)
            current = came_from[current]

        path.reverse()
        return path









