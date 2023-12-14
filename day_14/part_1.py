from collections import defaultdict
from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

with open(INPUT_FILE) as f:
    stages = defaultdict(int)
    ground = defaultdict(int)
    for row, line in enumerate(f.read().splitlines()):
        for col, item in enumerate(line):
            # Move the rounded rock to the north
            if item == 'O':
                stages[ground[col]] += 1
                ground[col] += 1
            elif item == '#':
                ground[col] = row + 1
    print(sum((row + 1 - stage) * rocks for stage, rocks in stages.items()))
