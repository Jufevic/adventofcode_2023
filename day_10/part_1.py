from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'
DEMO_INPUT_FILE_2 = CURRENT_FOLDER / 'demo_input_2.txt'

PIPES = {
    '|': ((-1, 0), (1, 0)),
    '-': ((0, -1), (0, 1)),
    'L': ((-1, 0), (0, 1)),
    'J': ((-1, 0), (0, -1)),
    '7': ((0, -1), (1, 0)),
    'F': ((1, 0), (0, 1)),
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
for drow, dcol in ((-1, 0), (0, -1), (1, 0), (0, 1)):
    if 0 <= start_row + drow < height and 0 <= start_col + dcol < width:
        n_pos = (start_row + drow, start_col + dcol)
        if start_pos in neighbours(n_pos):
            frontier.append(n_pos)
steps = 0
while frontier:
    new_frontier = []
    for current in frontier:
        for neighbour in neighbours(current):
            if neighbour not in visited:
                new_frontier.append(neighbour)
                visited.add(neighbour)
    frontier = new_frontier
    steps += 1

print(steps)