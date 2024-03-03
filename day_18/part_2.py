from pathlib import Path
from parse import parse

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'
MOVES = {
    0: (0, 1),
    1: (1, 0),
    2: (0, -1),
    3: (-1, 0),
}


row, col = (0, 0)
s = 0
perimeter = 0

with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        _, color = parse('{} (#{})', line)
        length = int(color[:-1], 16)
        drow, dcol = MOVES[int(color[-1])]
        # Use signed area formula from https://en.wikipedia.org/wiki/Polygon#Area
        s += (drow * col - dcol * row) * length
        row += drow * length
        col += dcol * length
        perimeter += length

print(abs(s) // 2 + perimeter // 2 + 1)