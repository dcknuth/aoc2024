# Day 18 part 1
import networkx as nx

filename = 'test18.txt'
filename = 'input18.txt'
NUM_BYTES = 1024
SIZE = 71

with open(filename) as f:
    ls = f.read().strip().split('\n')

m = [['.' for x in range(SIZE)] for y in range(SIZE)]

b_list = []
for l in ls:
    x, y = map(int, l.split(','))
    b_list.append((y, x))
for y, x in b_list[:NUM_BYTES]:
    m[y][x] = '#'
g = nx.Graph()
for y in range(SIZE):
    for x in range(SIZE):
        if m[y][x] == '.':
            # up
            if y > 0:
                if m[y-1][x] == '.':
                    g.add_edge((y, x), (y-1, x))
            # down
            if y < SIZE-1:
                if m[y+1][x] == '.':
                    g.add_edge((y, x), (y+1, x))
            # left
            if x > 0:
                if m[y][x-1] == '.':
                    g.add_edge((y, x), (y, x-1))
            # right
            if x < SIZE-1:
                if m[y][x+1] == '.':
                    g.add_edge((y, x), (y, x+1))
path_len = nx.shortest_path_length(g, (0, 0), (SIZE-1, SIZE-1))
print(path_len)

# part 2
for y, x in b_list[NUM_BYTES:]:
    if (y, x) in g.nodes:
        g.remove_node((y, x))
        if not nx.has_path(g, (0, 0), (SIZE-1, SIZE-1)):
            print(f'{x},{y}') # print in correct order for answer
            break
