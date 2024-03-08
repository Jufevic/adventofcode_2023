from pathlib import Path
from parse import parse

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

rules = {}
accepted = 0

with open(INPUT_FILE) as f:
    rules_block, ratings_block = f.read().split('\n\n')

for line in rules_block.splitlines():
    name, workflows = parse('{}{{{}}}', line)
    *workflows, default = workflows.split(',')
    rules[name] = [workflow.split(':') for workflow in workflows]
    rules[name].append(default)

for line in ratings_block.splitlines():
    x, m, a, s = parse('{{x={:d},m={:d},a={:d},s={:d}}}', line)
    current = 'in'
    while current not in 'AR':
        *conditions, default = rules[current]
        for condition, consequence in conditions:
            if eval(condition):
                current = consequence
                break
        else:
            current = default
    if current == 'A':
        accepted += x + m + a + s
    
print(accepted)
