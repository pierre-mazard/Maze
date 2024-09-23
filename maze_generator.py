# Maze generator 

import random 

def generate_maze(n):
    maze = [['#' for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if random.choice([True, False]):
                maze[i][j] = '.'
    maze[0][0] = '.'
    maze[n-1][n-1] = '.'
    return maze

def save_maze(maze, filename):
    with open(filename, 'w') as f:
        for row in maze:
            f.write(''.join(row) + '\n')

if __name__ == '__main__':
    n = int(input('Enter the size of the maze: '))
    filename = input('Enter the filename to save the maze: ')
    maze = generate_maze(n)
    save_maze(maze, filename)
    print('Maze saved to', filename)