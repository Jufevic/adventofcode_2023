from collections import deque
from pathlib import Path
from parse import parse

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

with open(INPUT_FILE) as f:
    line = f.readline()
    (spans, ) = parse('seeds: {}', line)
    spans = [int(number) for number in spans.split()]
    ranges = list(zip(spans[::2], spans[1::2]))
    ranges = deque(sorted(ranges))

    # Read mapping
    _ = f.readline()
    for block in f.read().split('\n\n'):
        offsets = []
        for line in iter(block.splitlines()[1:]):
            d_start, s_start, length = parse('{:d} {:d} {:d}', line)
            offsets.append((s_start, length, d_start - s_start))
        offsets = deque(sorted(offsets))

        # Create new intervals
        new_ranges = deque([])
        while ranges:
            first_el = ranges.popleft()
            start, length = first_el
            # Case 1: there are no more offsets, finish the loop
            if not offsets:
                new_ranges.append((start, length))
                new_ranges.extend(ranges)
                break
            s_start, s_length, offset = offsets.popleft()
            # Case 2: the range is outside any offset, it is kept as it is
            if start + length <= s_start:
                new_ranges.append((start, length))
                offsets.appendleft((s_start, s_length, offset))
                continue
            # Case 3: the lowest offset does not affect any range, ignore it
            elif s_start + s_length <= start:
                ranges.appendleft((start, length))
                continue
            # Case 4: overlap between range and offset: split the range
            elif start < s_start < start + length:
                new_ranges.append((start, s_start - start))
                ranges.appendleft((s_start, length - (s_start - start)))
                offsets.appendleft((s_start, s_length, offset))
                continue
            # Case 5: offset start lower than range start
            elif s_start <= start < s_start + s_length:
                if s_start + s_length < start + length:
                    new_ranges.append((start + offset, s_start + s_length - start))
                    ranges.appendleft((s_start + s_length, length - (s_start + s_length - start)))
                    continue
                else:
                    new_ranges.append((start + offset, length))
                    offsets.appendleft((s_start, s_length, offset))
                    continue
        ranges = deque(sorted(new_ranges))
        del start
        del length
    print(min(ranges)[0])
