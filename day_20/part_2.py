from collections import defaultdict
from functools import reduce
from operator import mul
from pathlib import Path
from parse import parse
from itertools import chain

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'
DEMO_INPUT_FILE_2 = CURRENT_FOLDER / 'demo_input_2.txt'

conjunctions = defaultdict(dict)
flip_flops = defaultdict(dict)
inputs = defaultdict(set)

with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        name, after = parse('{} -> {}', line)
        destinations = after.split(', ')
        # conjunction module
        if name.startswith('&'):
            name = name[1:]
            conjunctions[name]['destinations'] = destinations
        # flip-flop module
        elif name.startswith('%'):
            name = name[1:]
            flip_flops[name]['destinations'] = destinations
            flip_flops[name]['is_on'] = False
        else:
            broadcaster = destinations
        for dest in destinations:
            inputs[dest].add(name)

for conjunction, v in conjunctions.items():
    v['inputs'] = {dest :'low' for dest in inputs[conjunction]}


def push_button(required_high):
    pulses = [('button', 'low', 'broadcaster')]
    required = None
    while pulses:
        new_pulses = []
        for pulse in pulses:
            source, state, destination = pulse
            if source in required_high and state == 'high':
                required = source
            if destination in conjunctions:
                conjunction = conjunctions[destination]
                conjunction['inputs'][source] = state
                if all(v == 'high' for v in conjunction['inputs'].values()):
                    new_state = 'low'
                else:
                    new_state = 'high'
                for new_dest in conjunction['destinations']:
                    new_pulses.append((destination, new_state, new_dest))
            elif destination in flip_flops:
                if state == 'high':
                    continue
                flip_flop = flip_flops[destination]
                flip_flop['is_on'] = not flip_flop['is_on']
                if flip_flop['is_on']:
                    new_state = 'high'
                else:
                    new_state = 'low'
                for new_dest in flip_flop['destinations']:
                    new_pulses.append((destination, new_state, new_dest))
            elif destination == 'broadcaster':
                for new_dest in broadcaster:
                    new_pulses.append((destination, state, new_dest))
        pulses = new_pulses
    return required


required_high = inputs[next(iter(inputs['rx']))]
button_pushes = 0
primes = set()
while required_high:
    button_pushes += 1
    result = push_button(required_high)
    if result:
        required_high.remove(result)
        primes.add(button_pushes)

print(reduce(mul, primes))
