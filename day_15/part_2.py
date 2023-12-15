from pathlib import Path
from collections import defaultdict
from parse import parse

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

result = 0
boxes = defaultdict(dict)

with open(INPUT_FILE) as f:
    for instruction in f.readline().strip().split(','):
        if '=' in instruction:
            name, focusing_power = parse('{}={:d}', instruction)
            hash_tot = 0
            for char in name:
                hash_tot = ((hash_tot + ord(char)) * 17) % 256
            if name in boxes[hash_tot]:
                boxes[hash_tot][name] = focusing_power
            else:
                boxes[hash_tot][name] = focusing_power
        else:
            name = instruction[:-1]
            hash_tot = 0
            for char in name:
                hash_tot = ((hash_tot + ord(char)) * 17) % 256
            if name in boxes[hash_tot]:
                del boxes[hash_tot][name]
    for box, content in boxes.items():
        for index, (name, focusing_power) in enumerate(content.items(), 1):
            result += (box + 1) * index * focusing_power
    print(result)
