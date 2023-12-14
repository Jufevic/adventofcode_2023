from pathlib import Path
import numpy as np

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

columns_left = 0
rows_above = 0

with open(INPUT_FILE) as f:
    for block in f.read().split('\n\n'):
        grid = np.array([list(line) for line in block.splitlines()], dtype=str)
        for row in range(1, grid.shape[0] // 2 + 1):
            if np.all(grid[:row, :] == np.flipud(grid[row:2*row, :])):
                rows_above += row
                break
            if np.all(grid[-row:, :] == np.flipud(grid[-2*row:-row, :])):
                rows_above += grid.shape[0] - row
                break
        for col in range(1, grid.shape[1] // 2 + 1):
            if np.all(grid[:, :col] == np.fliplr(grid[:, col:2*col])):
                columns_left += col
                break
            if np.all(grid[:, -col:] == np.fliplr(grid[:, -2*col:-col])):
                columns_left += grid.shape[1] - col
                break

print(columns_left + 100 * rows_above)
