import os
import random

class Maze:
    def __init__(self, size):
        self.size = size
        self.maze = [['#' for _ in range(size)] for _ in range(size)]
        self.generate_maze()

    def generate_maze(self):
        for i in range(self.size):
            for j in range(self.size):
                if random.choice([True, False]):
                    self.maze[i][j] = '.'
        self.maze[0][0] = '.'  # Entrée
        self.maze[self.size-1][self.size-1] = '.'  # Sortie

    def save_maze(self, filename):
        if not os.path.exists('mazes'):
            os.makedirs('mazes')
        filepath = os.path.join('mazes', filename)
        with open(filepath, 'w') as f:
            for row in self.maze:
                f.write(''.join(row) + '\n')
