from pathlib import Path
from functools import cache

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

@cache
def count_possibilities(springs, hints):
    if not hints:
        return '#' not in springs
    if not springs:
        return not hints
    match springs[0]:
        case '.':
            return count_possibilities(springs[1:], hints)
        case '#':
            hint = hints[0]
            if ((len(springs) < hint)
                    or (any(spring == '.' for spring in springs[:hint]))
                    or (len(springs) >= hint + 1 and springs[hint] == '#')):
                return 0
            return count_possibilities(springs[hint + 1:], hints[1:])
        case '?':
            return (count_possibilities('#' + springs[1:], hints) +
                    count_possibilities(springs[1:], hints))

valid = 0
with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        springs, hints = line.split()
        springs = '?'.join([springs] * 5)
        hints = tuple([int(hint) for hint in hints.split(',')] * 5)
        valid += count_possibilities(springs, hints)
    print(valid)
