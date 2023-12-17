from pathlib import Path
from heapq import heappop, heappush

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

with open(INPUT_FILE) as f:
    grid = []
    for line in f.read().splitlines():
        grid.append([int(number) for number in line])

height = len(grid)
width = len(grid[0])
start = (0, 0)
goal = (height - 1, width - 1)

# frontier element = (heat_loss, position, direction, steps), where
# heat_loss = quantity to minimize
# position = (row, column)
# direction = (drow, dcol)
# steps = number of steps since the last time we turned (must be <3)
frontier = []
heappush(frontier, (0, start, (1, 0), 0))
heappush(frontier, (0, start, (0, 1), 0))

# cost_so_far[position, direction, steps] = heat_loss
cost_so_far = {(start, (1, 0), 0): 0, (start, (0, 1), 0): 0}

while frontier:
    heat_loss, position, direction, steps = heappop(frontier)
    row, col = position
    di, dj = direction

    if position == goal:
        break

    new_dirs = [(dj, di), (-dj, -di)]
    # Limit the number of steps in the same direction to 3
    if steps < 3:
        new_dirs.append((di, dj))

    for new_dir in new_dirs:
        drow, dcol = new_dir
        neighbour = row + drow, col + dcol
        nrow, ncol = neighbour
        if new_dir == direction:
            new_steps = steps + 1
        else:
            new_steps = 1
        if 0 <= nrow < height and 0 <= ncol < width:
            new_loss = heat_loss + grid[nrow][ncol]
            if ((neighbour, new_dir, new_steps) not in cost_so_far or
                    new_loss < cost_so_far[neighbour, new_dir, new_steps]):
                cost_so_far[neighbour, new_dir, new_steps] = new_loss
                heappush(frontier, (new_loss, neighbour, new_dir, new_steps))

print(heat_loss)
