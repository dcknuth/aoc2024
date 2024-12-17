# Day 16 part 1
import networkx as nx
import matplotlib.pyplot as plt

filename = 'test16.txt'
#filename = 'test16-2.txt'
filename = 'input16.txt'
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

with open(filename) as f:
    ls = f.read().strip().split('\n')

m = [[c for c in row] for row in ls]
m = [[c for c in row] for row in ls]
# find start and finish and replace with '.'s
end = []
start = (-1, -1)
start_dir = (0, 1)
for y in range(1, len(m)-1):
    for x in range(1, len(m[0])-1):
        c = m[y][x]
        if c == 'E':
            for dy, dx in DIRS:
                end.append((y, x, dy, dx))
            m[y][x] = '.'
        elif c == 'S':
            start = (y, x, start_dir[0], start_dir[1])
            m[y][x] = '.'

g = nx.Graph()
for y in range(1, len(m)-1):
    for x in range(1, len(m[0])-1):
        if m[y][x] == '.':
            for dy, dx in DIRS:
                if m[y+dy][x+dx] == '.':
                    for old_dy, old_dx in DIRS:
                        if (old_dy, old_dx) == (dy, dx):
                            g.add_edge((y, x, old_dy, old_dx),
                                       (y+dy, x+dx, dy, dx), weight=1)
                        else:
                            g.add_edge((y, x, old_dy, old_dx),
                                       (y+dy, x+dx, dy, dx), weight=1001)

# nx.draw(g, with_labels=True, node_color='lightblue', edge_color='gray',
#         node_size=2000, font_size=15, font_weight='bold')
# plt.show()
min_count = 10_000_000_000
for e in end:
    try:
        short_len = nx.shortest_path_length(g, start, e, weight='weight')
        if min_count > short_len:
            min_count = short_len
    except:
        pass
print(min_count)

# part 2
best_tiles = set()
for e in end:
    try:
        short_len = nx.shortest_path_length(g, start, e, weight='weight')
        if short_len == min_count:
            paths = list(nx.all_shortest_paths(g, start, e, weight='weight',))
            if len(paths) > 0:
                for path in paths:
                    for y, x, dy, dx in path:
                        best_tiles.add((y, x))
    except:
        pass
print(len(best_tiles))
