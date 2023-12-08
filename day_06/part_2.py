from pathlib import Path
from parse import parse

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

with open(INPUT_FILE) as f:
    (time,) = parse('Time: {}', f.readline())
    time = int(''.join(time.strip().split()))
    (dist,) = parse('Distance: {}', f.readline())
    dist = int(''.join(dist.strip().split()))
    wins = 0
    for t in range(time):
        if t * (time - t) > dist:
            break
    wins = 2 * (time // 2 - t) + 1 + time % 2
    print(wins)
