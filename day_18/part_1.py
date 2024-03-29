from pathlib import Path
from parse import parse

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'
MOVES = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}


row, col = (0, 0)
s = 0
perimeter = 0

with open(INPUT_FILE) as f:
    row, col = (0, 0)
    for line in f.read().splitlines():
        direction, length, _ = parse('{} {:d} ({})', line)
        drow, dcol = MOVES[direction]
        # Use signed area formula from https://en.wikipedia.org/wiki/Polygon#Area
        s += (drow * col - dcol * row) * length
        row += drow * length
        col += dcol * length
        perimeter += length

print(abs(s) // 2 + perimeter // 2 + 1)
