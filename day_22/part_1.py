from collections import defaultdict
from pathlib import Path
from itertools import product

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

bricks = []
with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        start, end = line.split('~')
        start = map(int, start.split(','))
        end = map(int, end.split(','))
        bricks.append(tuple(pos for pos in product(*(range(s, e + 1)
            for (s, e) in zip(start, end)))))

supported_by = {}
supports = {}
ground_height = defaultdict(int)
ground_brick = {}
bricks.sort(key=lambda brick: min(block[2] for block in brick))

# Simulate bricks fall
for index, brick in enumerate(bricks):
    lowest = max(ground_height[(x, y)] for x, y, _ in brick) + 1
    fall = brick[0][2] - lowest
    supported_by[index] = set()
    supports[index] = set()
    for x, y, _ in brick:
        if ground_height[(x, y)] + 1 == lowest and (x, y) in ground_brick:
            supported_by[index].add(ground_brick[(x, y)])
            supports[ground_brick[(x, y)]].add(index)
    for x, y, z in brick:
        ground_height[(x, y)] = z - fall
        ground_brick[(x, y)] = index

# Count total of bricks that can be removed.
# A brick can be removed if all bricks above it are supported by at least one
# other brick
print(sum(1 for aboves in supports.values()
          if all(len(supported_by[above]) > 1 for above in aboves)))
