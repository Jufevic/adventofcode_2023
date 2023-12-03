from pathlib import Path
import re

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

part_sum = 0

with open(INPUT_FILE) as f:
    lines = f.read().splitlines()
    height = len(lines)
    width = len(lines[0])
    for i, line in enumerate(lines):
        for m in re.finditer(r'\d+', line):
            is_part = False
            start, end = m.span()
            for side in (-1, 1):
                row = i + side
                if 0 <= row < height:
                    for col in range(start - 1, end + 1):
                        if 0 <= col < width:
                            symbol = lines[row][col]
                            if symbol != '.' and not line.isdigit():
                                is_part = True
                                break
            for col in (start - 1, end):
                if 0 <= col < width:
                    symbol = lines[i][col]
                    if symbol != '.' and not line.isdigit():
                        is_part = True
                        break
            if is_part:
                part_sum += int(m.group())
    print(part_sum)
