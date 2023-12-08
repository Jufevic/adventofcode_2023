from pathlib import Path
from itertools import cycle
from parse import parse

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'
DEMO_INPUT_FILE_2 = CURRENT_FOLDER / 'demo_input_2.txt'

with open(INPUT_FILE) as f:
    instructions = f.readline().strip()
    instructions = ['LR'.index(instr) for instr in instructions]
    _ = f.readline()
    directions = {}
    for line in f.read().splitlines():
        start, left, right = parse('{} = ({}, {})', line)
        directions[start] = left, right
    pos = 'AAA'
    for steps, instr in enumerate(cycle(instructions), 1):
        pos = directions[pos][instr]
        if pos == 'ZZZ':
            break
    print(steps)
