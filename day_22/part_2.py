from collections import defaultdict
from pathlib import Path
from itertools import product
from copy import deepcopy

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


def dependents(start_brick):
    """
    Count the number of bricks above start_brick that would fall if
    start_brick was removed.
    """
    new_supported_by = deepcopy(supported_by)
    destroyed = 0
    queue = [start_brick]
    while queue:
        brick = queue.pop()
        for above in supports[brick]:
            new_supported_by[above].remove(brick)
            if not new_supported_by[above]:
                destroyed += 1
                queue.append(above)
    return destroyed

print(sum(dependents(brick) for brick in supports))
