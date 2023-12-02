from pathlib import Path
from parse import parse

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

MAX_REVEAL = {
    'red': 12,
    'green': 13,
    'blue': 14,
}
sum_id = 0

with open(INPUT_FILE) as f:
    for line in f.readlines():
        game_id, revealed = parse('Game {:d}: {}', line)
        possible = True
        for reveal in revealed.split('; '):
            for group in reveal.split(', '):
                amount, color = group.split()
                amount = int(amount)
                if amount > MAX_REVEAL[color]:
                    possible = False
                    break
            if not possible:
                break
        if possible:
            sum_id += game_id
    print(sum_id)
