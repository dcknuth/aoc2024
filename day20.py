# Day 20 part 1
import networkx as nx

filename = "test20.txt"
filename = "input20.txt"
TO_BEAT = 99

with open(filename) as f:
    ls = f.read().strip().split('\n')

start = (-1, -1)
end = (-1, -1)
m = []
for y, row in enumerate(ls):
    new_row = []
    for x, c in enumerate(row):
        if c == 'S':
            start = (y, x)
            new_row.append('.')
        elif c == 'E':
            end = (y, x)
            new_row.append('.')
        else:
            new_row.append(c)
    m.append(new_row)
g = nx.Graph()

for y in range(1, len(m)-1):
    for x in range(1, len(m[0])-1):
        if m[y][x] == '.':
            # up
            if m[y-1][x] == '.':
                g.add_edge((y, x), (y-1, x))
            # down
            if m[y+1][x] == '.':
                g.add_edge((y, x), (y+1, x))
            # left
            if m[y][x-1] == '.':
                g.add_edge((y, x), (y, x-1))
            # down
            if m[y][x+1] == '.':
                g.add_edge((y, x), (y, x+1))

# first get the regular path
path = nx.shortest_path(g, start, end)
# then for every node on the path, try any available cheat
total = 0
for i, node in enumerate(path):
    y, x = node
    # up
    if y > 1:
        if m[y-2][x] == '.':
            l = nx.shortest_path_length(g, (y-2, x), end)
            if len(path)-1 > l + i + 2 + TO_BEAT:
                total += 1
    # down
    if y < len(m)-2:
        if m[y+2][x] == '.':
            l = nx.shortest_path_length(g, (y+2, x), end)
            if len(path)-1 > l + i + 2 + TO_BEAT:
                total += 1
    # left
    if x > 1:
        if m[y][x-2] == '.':
            l = nx.shortest_path_length(g, (y, x-2), end)
            if len(path)-1 > l + i + 2 + TO_BEAT:
                total += 1
    # right
    if x < len(m[0])-2:
        if m[y][x+2] == '.':
            l = nx.shortest_path_length(g, (y, x+2), end)
            if len(path)-1 > l + i + 2 + TO_BEAT:
                total += 1
print(total)

# part 2
# Since part 1 takes a minute to run, we need a different approach
#  for this part. Since there is only one path, we can just use the 
#  position of the node in the full path as the remaining length of
#  the cheat. Any node with a Manhatten distance of <=20 is reachable
from collections import defaultdict
len_lookup = dict()
for i, node in enumerate(path):
    len_lookup[node] = (len(path) - i) - 1
md_lookup = defaultdict(lambda: defaultdict(list))
for i, n1 in enumerate(path[:-1]):
    for n2 in path[i+1:]:
        md = abs(n1[0]-n2[0]) + abs(n1[1]-n2[1])
        if md <= 20:
            md_lookup[n1][md].append(n2)
            md_lookup[n2][md].append(n1)
total = 0
for i, node in enumerate(path):
    for md in md_lookup[node].keys():
        for jump_node in md_lookup[node][md]:
            if len(path) - 1 > len_lookup[jump_node] + i + md + TO_BEAT:
                total += 1
print(total)
