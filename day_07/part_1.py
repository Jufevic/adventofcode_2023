from pathlib import Path
from collections import Counter
from parse import parse

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

RANKS = "AKQJT98765432"

def rank(hand):
    hand_rank = [RANKS.index(card) for card in hand]
    counts = Counter(hand).values()
    counts = sorted(counts, reverse=True)
    # Five of a kind
    if counts[0] == 5:
        return 0, *hand_rank
    # Four of a kind
    elif counts[0] == 4:
        return 1, *hand_rank
    # Full house
    elif counts[0] == 3 and counts[1] == 2:
        return 2, *hand_rank
    # Three of a kind
    elif counts[0] == 3:
        return 3, *hand_rank
    # Two pairs
    elif counts[0] == 2 and counts[1] == 2:
        return 4, *hand_rank
    # One pair
    elif counts[0] == 2:
        return 5, *hand_rank
    # High card
    else:
        return 6, *hand_rank

with open(INPUT_FILE) as f:
    hands = []
    for line in f.read().splitlines():
        hand, bid = parse('{} {:d}', line)
        hands.append((hand, bid))
    hands = sorted(hands, key=lambda c: rank(c[0]), reverse=True)
    winnings = sum(bid * index for index, (_, bid) in enumerate(hands, 1))
    print(winnings)
