from pathlib import Path
from itertools import combinations
from parse import parse

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'
LOW = 200000000000000
HIGH = 400000000000000

paths = []

with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        x, y, z, vx, vy, vz = parse('{:d}, {:d}, {:d} @ {:d}, {:d}, {:d}', line)
        paths.append((x, y, vx, vy))

crossings = 0
for ((x_a, y_a, vx_a, vy_a), (x_b, y_b, vx_b, vy_b)) in combinations(paths, 2):
    # Test if lines are parallel
    if vx_a * vy_b == vx_b * vy_a:
        continue
    # Otherwise, find the intersection point
    denominator = vy_b * vx_a - vy_a * vx_b
    x_0 = ((vx_a * y_a - vy_a * x_a) * vx_b + (vy_b * x_b - vx_b * y_b) * vx_a
           ) / denominator
    y_0 = ((vx_a * y_a - vy_a * x_a) * vy_b + (vy_b * x_b - vx_b * y_b) * vy_a
           ) / denominator
    a_sign = (x_0 - x_a) / vx_a if vx_a != 0 else(y_0 - y_a) / vy_a
    b_sign = (x_0 - x_b) / vx_b if vx_b != 0 else(y_0 - y_b) / vy_b
    if a_sign < 0 or b_sign < 0:
        continue
    if LOW <= x_0 <= HIGH and LOW <= y_0 <= HIGH:
        crossings += 1

print(crossings)