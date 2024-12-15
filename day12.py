# Day 12 part 1, find total price
import networkx as nx
from collections import Counter

filename = 'test12.txt'
filename = 'test12-2.txt'
filename = 'test12-3.txt'
#filename = 'test12-4.txt'
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
#  count both corners and edges between them. Then count all turning
#  corners TODO
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
    outside_corners = {x:True for x in corner_count.keys() \
        if corner_count[x] < 4}
    turning_corners = 0
    for cur_corner in outside_corners.keys():
        # if a corner has two outside neighbors, not in same direction,
        #  via outside edges we count 1. If four via outside edges we count 2
        neighbors = list(cur_g.neighbors(cur_corner))
        n_outside = [x for x in neighbors if x in outside_corners]
        via_out_edge = []
        for o_n in n_outside:
            if side_count[tuple(sorted([o_n, cur_corner]))] < 2:
                via_out_edge.append(o_n)
        if len(via_out_edge) == 2:
            y1, x1 = via_out_edge[0]
            y2, x2 = via_out_edge[1]
            if y1 != y2 and x1 != x2:
                turning_corners += 1
        elif len(via_out_edge) == 4:
            turning_corners += 2
    total += area_count[n] * turning_corners
print(total)
