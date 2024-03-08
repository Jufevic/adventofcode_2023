from collections import defaultdict
from pathlib import Path
from parse import parse
from copy import deepcopy

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'
MIN = 1
MAX = 4000

rules = {}

with open(INPUT_FILE) as f:
    rules_block, _ = f.read().split('\n\n')

for line in rules_block.splitlines():
    name, workflows = parse('{}{{{}}}', line)
    *workflows, default = workflows.split(',')
    rules[name] = []
    for workflow in workflows:
        assertion, consequence = workflow.split(':')
        # Translate assertions into span and inverse span
        if '<' in assertion:
            letter, limit = parse('{}<{:d}', assertion)
            span = (MIN, limit)
            inverse_span = (limit, MAX + 1)
        elif '>' in assertion:
            letter, limit = parse('{}>{:d}', assertion)
            span = (limit + 1, MAX + 1)
            inverse_span = (MIN, limit + 1)
        rules[name].append((letter, span, inverse_span, consequence))
    rules[name].append(default)

def union_size(intervals):
    low = max(interval[0] for interval in intervals)
    high = min(interval[1] for interval in intervals)
    return high - low if high > low else 0

def recurse(current, intervals):
    """Recursively sum all possibilities."""

    # Compute number of all possible distinct combinations which will be
    # accepted
    if current == 'A':
        total = 1
        for spans in intervals.values():
            total *= union_size(spans)
        return total

    # Ignore combinations that won't be accepted
    elif current == 'R':
        return 0

    # General case: recurse
    *conditions, default = rules[current]
    total = 0
    for letter, span, inverse_span, consequence in conditions:
        # Update intervals with condition
        new_intervals = deepcopy(intervals)
        new_intervals[letter].append(span)

        # Add this subtotal to the total
        total += recurse(consequence, new_intervals)

        # Update intervals with negative condition
        intervals[letter].append(inverse_span)
    total += recurse(default, intervals)
    return total

intervals = defaultdict(list)
for letter in 'xmas':
    intervals[letter].append((MIN, MAX + 1))

print(recurse('in', intervals))
