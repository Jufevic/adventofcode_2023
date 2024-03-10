from pathlib import Path
from collections import defaultdict
from functools import cache
from copy import deepcopy

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'
START = (0, 1)
MOVES = {
    '>': (0, 1),
    '^': (-1, 0),
    '<': (0, -1),
    'v': (1, 0),
}
FOREST = '#'
FREEWAY = '.'

with open(INPUT_FILE) as f:
    grid = []
    for row, line in enumerate(f.read().splitlines()):
        grid.append(list(line))


# Reduce the grid to a weighted directed graph
end = len(grid) - 1, len(grid[0]) - 2
graph = defaultdict(dict)
visited_nodes = {START}
node_queue = {START}
grid[START[0]][START[1]] = FOREST
# Node queue: set of intersection nodes
while node_queue:
    node_row, node_col = node_queue.pop()

    # Explore all directions around the node
    for di, dj in MOVES.values():
        frow, fcol = node_row + di, node_col + dj
        if grid[frow][fcol] == FOREST:
            continue

        # Move one step forward until we either find a dead end, or another node
        row, col = frow, fcol
        path_length = 1
        visited = {(node_row, node_col)}
        while True:
            visited.add((row, col))

            # If it's the end position, don't step any further.
            if (row, col) == end:
                graph[(node_row, node_col)][(row, col)] = path_length
                break
            
            # Build the set of neighbours.
            neighbours = set()
            current = grid[row][col]
            if current in MOVES:
                possible = {MOVES[current]}
            else:
                possible = MOVES.values()
            for drow, dcol in possible:
                nrow, ncol = row + drow, col + dcol
                neighbour = nrow, ncol
                if grid[nrow][ncol] != FOREST and neighbour not in visited:
                    neighbours.add(neighbour)

            # If it's a dead end, abandon this track.
            if not neighbours:
                break

            # If there is only one possible direction, move one step forward.
            elif len(neighbours) == 1:
                path_length += 1
                for neighbour in neighbours:
                    row, col = neighbour
                if neighbour in visited_nodes:
                    graph[(node_row, node_col)][(row, col)] = path_length
                    node_queue.add((row, col))
                    visited_nodes.add((row, col))
                    break

            # If there are two or more possible directions, it's an
            # intersection. Add it to the node_queue.
            elif len(neighbours) > 1:
                graph[(node_row, node_col)][(row, col)] = path_length
                node_queue.add((row, col))
                visited_nodes.add((row, col))
                break

# Make graph undirected
for start_node, others in graph.copy().items():
    for end_node, length in others.items():
        graph[end_node][start_node] = length

print(graph)

# Find the longest path in the graph from start to end
@cache
def longest_path(am, been):
    """
    Find the longest path between the node `am` and the end
    :param am: Where I currently am
    :param been: The nodes where I have been
    """
    if am == end:
        return 0
    maximum = 0
    possibilities = graph[am].keys() - been
    if not possibilities:
        return None
    for possible in possibilities:
        length = graph[am][possible]
        local_max = longest_path(possible, frozenset(been | {am}))
        if local_max is not None:
            maximum = max(maximum, length + local_max)
    return maximum

print(longest_path(START, frozenset()))
