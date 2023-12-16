from itertools import cycle
from math import lcm
from pathlib import Path
from parse import parse

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input_3.txt'

with open(INPUT_FILE) as f:
    instructions = f.readline().strip()
    instructions = ['LR'.index(instr) for instr in instructions]
    _ = f.readline()
    directions = {}
    for line in f.read().splitlines():
        start, left, right = parse('{} = ({}, {})', line)
        directions[start] = left, right

min_steps = []
for start in directions:
    pos = start
    if not pos.endswith('A'):
        continue
    for steps, instr in enumerate(cycle(instructions), 1):
        pos = directions[pos][instr]
        if pos.endswith('Z'):
            break
    min_steps.append(steps)

print(lcm(*min_steps))
