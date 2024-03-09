from copy import deepcopy
from pathlib import Path
from parse import parse

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'


rules = {}

with open(INPUT_FILE) as f:
    rules_block, _ = f.read().split('\n\n')

for line in rules_block.splitlines():
    name, workflows = parse('{}{{{}}}', line)
    *workflows, default = workflows.split(',')
    rules[name] = [workflow.split(':') for workflow in workflows]
    rules[name].append(default)

def recurse(current, intervals):
    """Recursively sum all possibilities."""

    # Compute number of all possible distinct combinations which will be
    # accepted
    if current == 'A':
        total = 1
        for low, high in intervals.values():
            total *= (high - low + 1)
        return total

    # Ignore combinations that won't be accepted
    elif current == 'R':
        return 0

    # General case: recurse
    *conditions, default = rules[current]
    total = 0
    for assertion, consequence in conditions:
        new_intervals = deepcopy(intervals)
        if '<' in assertion:
            letter, limit = parse('{}<{:d}', assertion)
            new_intervals[letter][1] = min(new_intervals[letter][1], limit - 1)
            total += recurse(consequence, new_intervals)
            intervals[letter][0] = max(intervals[letter][0], limit)
        elif '>' in assertion:
            letter, limit = parse('{}>{:d}', assertion)
            new_intervals[letter][0] = max(new_intervals[letter][0], limit + 1)
            total += recurse(consequence, new_intervals)
            intervals[letter][1] = min(intervals[letter][1], limit)
    total += recurse(default, intervals)
    return total


print(recurse('in', {letter: [1, 4000] for letter in 'xmas'}))
