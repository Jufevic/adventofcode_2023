from collections import defaultdict
from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

graph = defaultdict(set)

with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        name, connections = line.split(': ')
        connections = connections.split()
        for connection in connections:
            graph[name].add(connection)
            graph[connection].add(name)

# Use graphviz at http://magjac.com/graphviz-visual-editor/
# to see which connections you need to unplug
# Alternatively, implement strongly connected components algorithm
for left, right in (('mmr', 'znk'), ('rnx', 'ddj'), ('lxb', 'vcq')):
    graph[left].remove(right)
    graph[right].remove(left)

# BFS over any edge
start = next(iter(graph.keys()))
visited = set()
queue = [start]
while queue:
    current = queue.pop()
    for neighbour in graph[current]:
        if neighbour not in visited:
            queue.append(neighbour)
    visited.add(current)

print((len(graph) - len(visited)) * len(visited))
