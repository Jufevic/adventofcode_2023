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

border = set()

with open(INPUT_FILE) as f:
    row, col = (0, 0)
    for line in f.read().splitlines():
        direction, length, color = parse('{} {:d} ({})', line)
        drow, dcol = MOVES[direction]
        for _ in range(length):
            row, col = row + drow, col + dcol
            border.add((row, col))

inside = set()
queue = [(1, 1)]
while queue:
    row, col = queue.pop()
    for drow, dcol in MOVES.values():
        neighbour = row + drow, col + dcol
        if neighbour not in border and neighbour not in inside:
            inside.add(neighbour)
            queue.append(neighbour)

print(len(inside) + len(border))
