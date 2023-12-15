from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

result = 0

with open(INPUT_FILE) as f:
    for instruction in f.readline().strip().split(','):
        hash_tot = 0
        for char in instruction:
            hash_tot = ((hash_tot + ord(char)) * 17) % 256
        result += hash_tot
    print(result)
