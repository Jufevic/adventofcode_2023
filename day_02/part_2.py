from pathlib import Path
from collections import defaultdict
from parse import parse

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

sum_power = 0

with open(INPUT_FILE) as f:
    for line in f.readlines():
        game_id, revealed = parse('Game {:d}: {}', line)
        game = defaultdict(int)
        for reveal in revealed.split('; '):
            for group in reveal.split(', '):
                amount, color = group.split()
                amount = int(amount)
                game[color] = max(game[color], amount)
        sum_power += game['red'] * game['green'] * game['blue']
    print(sum_power)
