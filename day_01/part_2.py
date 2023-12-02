from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

calibration_sum = 0
digits = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')

with open(INPUT_FILE) as f:
    for line in f.readlines():
        if any(char.isdigit() for char in line):
            first_digit = next(char for char in line if char.isdigit())
            last_digit = next(char for char in reversed(line) if char.isdigit())
            digit_first_pos = (first_digit, line.index(first_digit))
            digit_last_pos = (last_digit, line.rindex(last_digit))
        else:
            digit_first_pos = ('', len(line))
            digit_last_pos = ('', 0)
        for value, digit in enumerate(digits, 1):
            if digit in line:
                first_pos = line.index(digit)
                last_pos = line.rindex(digit)
                if first_pos < digit_first_pos[1]:
                    digit_first_pos = (str(value), first_pos)
                if last_pos > digit_last_pos[1]:
                    digit_last_pos = (str(value), last_pos)

        calibration_value = int(digit_first_pos[0] + digit_last_pos[0])
        calibration_sum += calibration_value
    print(calibration_sum)
