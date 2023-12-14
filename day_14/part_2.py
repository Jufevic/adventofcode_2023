from collections import defaultdict
from pathlib import Path
import numpy as np

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

with open(INPUT_FILE) as f:
    grid = np.array([list(line) for line in f.read().splitlines()])

for rotation in range(1000 + 1):
    ground = np.zeros(grid.shape[1], dtype=int)
    for row, line in enumerate(grid):
        if 'O' in line:
            indices = np.where(line == 'O')
            grid[row, indices] = '.'
            grid[ground[indices], indices] = 'O'
            ground[indices] += 1
        ground[line != '.'] = row + 1
    # Rotate the grid by 90° clockwise
    grid = np.rot90(grid, -1)
    # Note: not actually solved, but there seem to be a pattern at some point...
    if rotation % 4 == 3:
        print(sum(i * np.sum(line == 'O') for i, line in enumerate(reversed(grid), 1)))
