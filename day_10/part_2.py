from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE_3 = CURRENT_FOLDER / 'demo_input_3.txt'
DEMO_INPUT_FILE_4 = CURRENT_FOLDER / 'demo_input_4.txt'
DEMO_INPUT_FILE_5 = CURRENT_FOLDER / 'demo_input_5.txt'

PIPES = {
    '|': {(-1, 0), (1, 0)},
    '-': {(0, -1), (0, 1)},
    'L': {(-1, 0), (0, 1)},
    'J': {(-1, 0), (0, -1)},
    '7': {(0, -1), (1, 0)},
    'F': {(1, 0), (0, 1)},
}
START = 'S'

grid = []

with open(INPUT_FILE) as f:
    for row, line in enumerate(f.read().splitlines()):
        grid.append(list(line))
        if START in line:
            start_row = row
            start_col = line.index(START)
            start_pos = start_row, start_col
height = len(grid)
width = len(grid[0])

def neighbours(pos):
    row, col = pos
    current = grid[row][col]
    if current in PIPES:
        for drow, dcol in PIPES[current]:
            if 0 <= row + drow < height and 0 <= col + dcol < width:
                yield (row + drow, col + dcol)

# BFS to find all pipes in the loop
visited = {start_pos}
frontier = []
directions = set()
for drow, dcol in ((-1, 0), (0, -1), (1, 0), (0, 1)):
    if 0 <= start_row + drow < height and 0 <= start_col + dcol < width:
        n_pos = (start_row + drow, start_col + dcol)
        if start_pos in neighbours(n_pos):
            frontier.append(n_pos)
            directions.add((drow, dcol))
# Replace the start pipe by what it really is
for pipe, dirs in PIPES.items():
    if dirs == directions:
        grid[start_row][start_col] = pipe
        break
while frontier:
    new_frontier = []
    for current in frontier:
        for neighbour in neighbours(current):
            if neighbour not in visited:
                new_frontier.append(neighbour)
                visited.add(neighbour)
    frontier = new_frontier

# Do a line scan to find which tiles are inside the loop
inside = 0
for row, line in enumerate(grid):
    intersects = 0
    for col, current in enumerate(line):
        if (row, col) in visited:
            if current == '-':
                continue
            if current in 'LF':
                partial = current
            elif current in 'J7':
                match partial + current:
                    case 'LJ' | 'F7':
                        continue
                    case 'L7' | 'FJ':
                        intersects += 1
            else:
                intersects += 1
        elif intersects % 2 == 1:
            inside += 1
print(inside)
