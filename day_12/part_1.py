from pathlib import Path
from itertools import groupby, product

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

valid = 0

with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        springs, hints = line.split()
        hints = [int(hint) for hint in hints.split(',')]
        unknown_springs = [i for i, spring in enumerate(springs) if spring == '?']
        for maybe_valid in product('.#', repeat=len(unknown_springs)):
            new_springs = list(springs)
            for i, replacement in enumerate(maybe_valid):
                new_springs[unknown_springs[i]] = replacement
            new_springs = ''.join(new_springs)
            if [len(list(g)) for k, g in groupby(new_springs) if k == '#'] == hints:
                valid += 1
    print(valid)
