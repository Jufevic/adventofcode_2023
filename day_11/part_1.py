from pathlib import Path
import numpy as np
from scipy.spatial.distance import pdist

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

grid = np.genfromtxt(INPUT_FILE, dtype=str, delimiter=1, comments=None)
to_duplicate = np.where(np.all(grid == '.', axis=0))[0]
grid = np.insert(grid, to_duplicate, '.', axis=1)
to_duplicate = np.where(np.all(grid == '.', axis=1))[0]
grid = np.insert(grid, to_duplicate, '.', axis=0)
galaxies = np.vstack(np.where(grid == '#')).T
distances = pdist(galaxies, metric='cityblock')
print(distances.sum())
