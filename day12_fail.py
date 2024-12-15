# Day 12 part 1, find total price
import networkx as nx
from collections import Counter

filename = 'test12.txt'
filename = 'test12-2.txt'
filename = 'test12-3.txt'
filename = 'input12.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

m = [[x for x in y] for y in ls]
g = nx.Graph()

for y, row in enumerate(m):
    for x, c in enumerate(row):
        g.add_node((y, x), name=m[y][x])
        # up
        if y > 0 and m[y][x] == m[y-1][x]:
            g.add_edge((y, x), (y-1, x))
        # down
        if y < len(m)-1 and m[y][x] == m[y+1][x]:
            g.add_edge((y, x), (y+1, x))
        # left
        if x > 0 and m[y][x] == m[y][x-1]:
            g.add_edge((y, x), (y, x-1))
        # right
        if x < len(row)-1 and m[y][x] == m[y][x+1]:
            g.add_edge((y, x), (y, x+1))

# count up areas and perimeters
area_count = Counter()
edge_count = Counter()
subgraphs = dict()
group_nodes = dict()
group_num = 0
for node, data in g.nodes(data=True):
    if (node) not in subgraphs:
        connected_nodes = nx.node_connected_component(g, node)
        cur_node_set = tuple(connected_nodes)
        # area count
        area_count[(data['name'], group_num)] += len(cur_node_set)
        # edge count
        subgraph = g.subgraph(connected_nodes)
        edge_count[(data['name'], group_num)] = subgraph.number_of_edges()
        for n in cur_node_set:
            subgraphs[n] = cur_node_set
            group_nodes[group_num] = cur_node_set
        group_num += 1
            
total = 0
for n in area_count.keys():
    perimeter = area_count[n] * 4 - edge_count[n] * 2
    total += area_count[n] * perimeter
print(total)

# part 2
# for each group we will add all the corners to a new graph and 
#  count both corners and edges between them. Then traverse along
#  non, count 4 nodes using only count 1 edges and counting turns
#  to get the number of sides
# There is an edge case where a corner can be visited twice if it
#  is on a diagonal between just two blocks. Will need to store and
#  handle those separately
total = 0
for n in area_count.keys():
    corner_count = Counter()
    side_count = Counter()
    cur_g = nx.Graph()
    for cube in group_nodes[n[1]]:
        y, x = cube
        # add corners to counts
        corner_count[cube] += 1
        corner_count[(y+1, x)] += 1
        corner_count[(y+1, x+1)] += 1
        corner_count[(y, x+1)] += 1
        # add sides to counts and add to graph
        side_count[(cube, (y+1, x))] += 1
        cur_g.add_edge(cube, (y+1, x))
        side_count[(cube, (y, x+1))] += 1
        cur_g.add_edge(cube, (y, x+1))
        side_count[((y+1, x), (y+1, x+1))] += 1
        cur_g.add_edge((y+1, x), (y+1, x+1))
        side_count[((y, x+1), (y+1, x+1))] += 1
        cur_g.add_edge((y, x+1), (y+1, x+1))
    # now we need to find all sides
    outside_corners = {x:[] for x in corner_count.keys() \
        if corner_count[x] < 4}
    sides = 0
    while len(outside_corners) > 0:
        orig_corner = (-1, -1)
        # Don't start on a weird, diagonally shared corner
        for corner in outside_corners.keys():
            orig_corner = corner
            # TODO need not four single edge test below
            if cur_g.degree[corner] != 4:
                break
            inside_edges = False
            for side in cur_g.edges(cur_corner):
                if side_count[tuple(sorted(side))] > 1:
                    inside_edges = True
                    break
            if inside_edges:
                break
        cur_corner = orig_corner
        cur_dir = (-1, -1) # starting with invalid direction
        last_dir = cur_dir
        last_corner = (-1, -1)
        looped = False
        traversed_sides = dict()
        while not looped:
            if cur_g.degree[cur_corner] != 4:
                del outside_corners[cur_corner]
            elif len(outside_corners[cur_corner]) > 0:
                del outside_corners[cur_corner]
            else:
                no_inside_edges = True
                for side in cur_g.edges(cur_corner):
                    if side_count[tuple(sorted(side))] > 1:
                        del outside_corners[cur_corner]
                        no_inside_edges = False
                        break
                if no_inside_edges:
                    outside_corners[cur_corner].append(last_corner)
            for next_corner in nx.neighbors(cur_g, cur_corner):
                if (tuple(sorted([cur_corner, next_corner]))) in traversed_sides:
                    continue
                if next_corner == last_corner:
                    continue
                if corner_count[next_corner] > 3:
                    continue
                next_edge = tuple(sorted([cur_corner, next_corner]))
                if side_count[next_edge] > 1:
                    continue
                if next_corner == orig_corner and next_corner != last_corner:
                    looped = True
                    dir = (next_corner[0]-cur_corner[0], \
                        next_corner[1]-cur_corner[1])
                    if dir != cur_dir:
                        sides += 1
                        last_dir = cur_dir
                        cur_dir = dir
                    last_corner = cur_corner
                    cur_corner = next_corner
                    traversed_sides[tuple(sorted([last_corner, \
                        cur_corner]))] = True
                    break
                if next_corner not in outside_corners:
                    continue
                if cur_corner in outside_corners[next_corner]:
                    continue
                dir = (next_corner[0]-cur_corner[0], \
                    next_corner[1]-cur_corner[1])
                if dir != cur_dir:
                    sides += 1
                    last_dir = cur_dir
                    cur_dir = dir
                elif cur_corner in outside_corners:
                    sides += 1
                last_corner = cur_corner
                cur_corner = next_corner
                traversed_sides[tuple(sorted([last_corner, \
                    cur_corner]))] = True
                break
    if sides % 2 == 1:
        total += area_count[n] * (sides-1)
    else:
        total += area_count[n] * sides
print(total)
