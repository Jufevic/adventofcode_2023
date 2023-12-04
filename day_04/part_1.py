from pathlib import Path
from parse import parse

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

total = 0

with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        _, winning, current = parse('Card {}: {} | {}', line)
        winning = set(winning.split())
        current = set(current.split())
        common = winning & current
        if common:
            total += 2 ** (len(common) - 1)
    print(total)
