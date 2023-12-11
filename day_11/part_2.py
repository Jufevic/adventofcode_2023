from pathlib import Path
import numpy as np
from scipy.spatial.distance import cdist

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

grid = np.genfromtxt(INPUT_FILE, dtype=str, delimiter=1, comments=None)
galaxies = np.vstack(np.where(grid == '#')).T
duplicated_rows = np.where(np.all(grid == '.', axis=1))[0]
duplicated_cols = np.where(np.all(grid == '.', axis=0))[0]
for row in reversed(duplicated_rows):
    galaxies[galaxies[:, 0] > row, 0] = galaxies[galaxies[:, 0] > row, 0] + 1e6 - 1
for col in reversed(duplicated_cols):
    galaxies[galaxies[:, 1] > col, 1] = galaxies[galaxies[:, 1] > col, 1] + 1e6 - 1
distances = cdist(galaxies, galaxies, metric='cityblock')
print(distances.sum()//2)
