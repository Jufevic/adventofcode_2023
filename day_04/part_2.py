from pathlib import Path
from parse import parse
from collections import defaultdict

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

total = defaultdict(lambda: 1)

with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        card_id, winning, current = parse('Card {:>d}: {} | {}', line)
        card_id = int(card_id)
        winning = set(winning.split())
        current = set(current.split())
        common = winning & current
        if common:
            span = len(common)
            copies = total[card_id]
            for i in range(card_id + 1, card_id + span + 1):
                total[i] += copies
        elif card_id not in total:
            total[card_id] = 1
    print(sum(copies for card, copies in total.items() if card <= card_id))
