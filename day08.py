# Day 8 part 1
# How many unique locations within the bounds of the map contain an antinode?
from collections import defaultdict

filename = 'test08.txt'
#filename = 'input08.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

Y = len(ls)
X = len(ls[0])

# load tower locations
map = [[c for c in l] for l in ls]
towers = defaultdict(list)
for y, row in enumerate(map):
    for x, c in enumerate(row):
        if c != '.':
            towers[c].append((y, x))

def isOnMap(y, x):
    if y > -1 and x > -1 and y < Y and x < X:
        return(True)
    return(False)

anti_nodes = defaultdict(list)
# antinodes should be the Manhattan distance again from the pair
for c in towers.keys():
    for i in range(len(towers[c])-1):
        p1y, p1x = towers[c][i]
        for j in range(i+1, len(towers[c])):
            p2y, p2x = towers[c][j]
            dy = p2y - p1y
            dx = p2x - p1x
            a1y = p2y + dy
            a1x = p2x + dx
            if isOnMap(a1y, a1x):
                anti_nodes[(a1y, a1x)].append(c)
            a2y = p1y - dy
            a2x = p1x - dx
            if isOnMap(a2y, a2x):
                anti_nodes[(a2y, a2x)].append(c)

print(f'Total, unique antinodes is {len(anti_nodes)}')

# part 2
anti_nodes = defaultdict(list)
for c in towers.keys():
    for i in range(len(towers[c])-1):
        p1y, p1x = towers[c][i]
        for j in range(i+1, len(towers[c])):
            p2y, p2x = towers[c][j]
            dy = p2y - p1y
            dx = p2x - p1x
            # add the current pair
            anti_nodes[(p1y, p1x)].append(c)
            anti_nodes[(p2y, p2x)].append(c)
            # walk one direction
            a1y = p2y + dy
            a1x = p2x + dx
            while isOnMap(a1y, a1x):
                anti_nodes[(a1y, a1x)].append(c)
                a1y = a1y + dy
                a1x = a1x + dx
            # TODO walk the other direction
            a2y = p1y - dy
            a2x = p1x - dx
            while isOnMap(a2y, a2x):
                anti_nodes[(a2y, a2x)].append(c)
                a2y = a2y - dy
                a2x = a2x - dx

print(f'Total, unique antinodes part2 is {len(anti_nodes)}')
