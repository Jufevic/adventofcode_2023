from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

calibration_sum = 0

with open(INPUT_FILE) as f:
    for line in f.readlines():
        first_digit = next(char for char in line if char.isdigit())
        last_digit = next(char for char in reversed(line) if char.isdigit())
        calibration_value = int(first_digit + last_digit)
        calibration_sum += calibration_value
    print(calibration_sum)
