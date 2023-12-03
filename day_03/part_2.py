from pathlib import Path
import re
from collections import defaultdict

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

gear_sum = 0

with open(INPUT_FILE) as f:
    lines = f.read().splitlines()
    height = len(lines)
    width = len(lines[0])
    numbers = defaultdict(set)
    # First pass: find all numbers and their positions
    for i, line in enumerate(lines):
        for m in re.finditer(r'\d+', line):
            numbers[i].add((m.start(), m.end(), int(m.group())))
    # Second pass: find all gears
    for i, line in enumerate(lines):
        for m in re.finditer(r'\*', line):
            j = m.start()
            neighbours = set()
            for row in range(i - 1, i + 2):
                for col in range(j - 1, j + 2):
                    if (row, col) == (i, j):
                        continue
                    if (0 <= row < height) and (0 <= col < width):
                        for number in numbers[row]:
                            start, end, value = number
                            if col in range(start, end):
                                neighbours.add(number)
            if len(neighbours) == 2:
                neighbours = list(neighbours)
                gear_sum += neighbours[0][2] * neighbours[1][2]
    print(gear_sum)
