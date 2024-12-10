# Day 10 part 1
# What is the sum of the scores of all trailheads on your topographic map?
import networkx as nx

filename = 'test10.txt'
filename = 'input10.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

trailheads = dict()
peaks = dict()
g = nx.DiGraph()
m = [[int(x) for x in y] for y in ls]

for y, row in enumerate(m):
    for x, n in enumerate(row):
        connected = False
        # up
        if y > 0:
            if m[y][x] == m[y-1][x] - 1:
                g.add_edge((y, x), (y-1, x))
                connected = True
                if m[y-1][x] == 9:
                    peaks[(y-1, x)] = True
        # down
        if y < len(m) - 1:
            if m[y][x] == m[y+1][x] - 1:
                g.add_edge((y, x), (y+1, x))
                connected = True
                if m[y+1][x] == 9:
                    peaks[(y+1, x)] = True
        # left
        if x > 0:
            if m[y][x] == m[y][x-1] - 1:
                g.add_edge((y, x), (y, x-1))
                connected = True
                if m[y][x-1] == 9:
                    peaks[(y, x-1)] = True
        # right
        if x < len(row) - 1:
            if m[y][x] == m[y][x+1] - 1:
                g.add_edge((y, x), (y, x+1))
                connected = True
                if m[y][x+1] == 9:
                    peaks[(y, x+1)] = True
        if n == 0 and connected:
            trailheads[(y, x)] = 0

total = 0
for trailhead in trailheads:
    for peak in peaks:
        if nx.has_path(g, trailhead, peak):
            trailheads[trailhead] += 1
            total += 1
print(total)

# part 2
total = 0
for trailhead in trailheads:
    for peak in peaks:
        try:
            all_paths = list(nx.all_simple_paths(g, trailhead, peak))
            trailheads[trailhead] += len(all_paths)
            total += len(all_paths)
        except:
            pass
print(total)
