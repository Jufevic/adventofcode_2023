from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'
START = 'S'
MAX_STEPS = 64

with open(INPUT_FILE) as f:
    grid = []
    for row, line in enumerate(f.read().splitlines()):
        grid.append(list(line))
        if START in line:
            start_row = row
            start_col = line.index(START)

height = len(grid)
width = len(grid[0])
pos = (start_row, start_col)
queue = [pos]
reachable = 1
visited = {pos}
for steps in range(1, MAX_STEPS + 1):
    new_queue = []
    while queue:
        row, col = queue.pop()
        for (drow, dcol) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            neighbour = (row + drow, col + dcol)
            nrow, ncol = neighbour
            if (0 <= nrow < height and 0 <= ncol < width
                    and neighbour not in visited and grid[nrow][ncol] != '#'):
                new_queue.append(neighbour)
                visited.add(neighbour)
    queue = new_queue
    if steps % 2 == 0:
        reachable += len(new_queue)
print(f'{reachable=}')