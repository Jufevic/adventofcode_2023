from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'
MOVES = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
REDIRECTIONS = {
    '\\': {'N': 'W', 'S': 'E', 'W': 'N', 'E': 'S'},
    '/': {'N': 'E', 'S': 'W', 'W': 'S', 'E': 'N'},
    '-': {'N': ('W', 'E'), 'S': ('W', 'E'), 'W': 'W', 'E': 'E'},
    '|': {'N': 'N', 'S': 'S', 'W': ('N', 'S'), 'E': ('N', 'S')},
    '.': {'N': 'N', 'S': 'S', 'W': 'W', 'E': 'E'},
}

with open(INPUT_FILE) as f:
    grid = []
    for line in f.read().splitlines():
        grid.append(list(line))

height = len(grid)
width = len(grid[0])
pos = (0, -1)
direction = 'E'
energized = {(pos, direction)}
queue = [(pos, direction)]
while queue:
    (row, col), direction = queue.pop()
    drow, dcol = MOVES[direction]
    neighbour = (row + drow, col + dcol)
    nrow, ncol = neighbour
    if 0 <= nrow < height and 0 <= ncol < width:
        new_directions = REDIRECTIONS[grid[nrow][ncol]][direction]
        for direction in new_directions:
            if (neighbour, direction) not in energized:
                energized.add((neighbour, direction))
                queue.append((neighbour, direction))
print(len(set(pos for pos, dir in energized if pos != (0, -1))))
