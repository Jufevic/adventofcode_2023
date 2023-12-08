from pathlib import Path
from parse import parse

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

with open(INPUT_FILE) as f:
    line = f.readline()
    (seeds, ) = parse('seeds: {}', line)
    items = {int(seed) for seed in seeds.split()}
    # Ignore first blank line
    _ = f.readline()
    for block in f.read().split('\n\n'):
        # Ignore block first line
        lines = iter(block.splitlines()[1:])
        new_items = set()
        for line in lines:
            d_start, s_start, length = parse('{:d} {:d} {:d}', line)
            for item in items.copy():
                if s_start <= item < s_start + length:
                    items.remove(item)
                    new_items.add(item + (d_start - s_start))
        items = new_items | items
    print(min(items))
