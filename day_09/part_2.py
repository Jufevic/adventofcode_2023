from pathlib import Path
import numpy as np

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

total = 0

with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        sequence = [int(number) for number in line.split()]
        derivatives = [sequence]
        while any(sequence):
            sequence = np.diff(sequence)
            derivatives.append(sequence)
        last = 0
        while derivatives:
            last = derivatives.pop()[0] - last
        total += last
    print(total)
