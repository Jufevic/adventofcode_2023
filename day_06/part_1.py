from pathlib import Path
from parse import parse

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

total_wins = 1

with open(INPUT_FILE) as f:
    (times,) = parse('Time: {}', f.readline())
    times = times.strip()
    times = (int(time) for time in times.split())
    (distances,) = parse('Distance: {}', f.readline())
    distances = distances.strip()
    distances = (int(dist) for dist in distances.split())
    for time, dist in zip(times, distances):
        wins = 0
        for t in range(time):
            if t * (time - t) > dist:
                break
        wins = 2 * (time // 2 - t) + 1 + time % 2
        total_wins *= wins
    print(total_wins)
