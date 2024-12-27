# Day 21 part 1
import networkx as nx
from paths import kp_paths, np_paths
from collections import Counter

filename = "test21.txt"
filename = "input21.txt"
num_robots = 25

with open(filename) as f:
    ls = f.read().strip().split('\n')

num_pad = [['7', '8', '9'],
           ['4', '5', '6'],
           ['1', '2', '3'],
           ['*', '0', 'A']]
key_pad = [['*', '^', 'A'],
           ['<', 'v', '>']]

npg = nx.DiGraph()
for y in range(len(num_pad)):
    for x in range(len(num_pad[y])):
        if num_pad[y][x] == '*':
            continue
        # up
        if y > 0:
            if num_pad[y-1][x] != '*':
                npg.add_edge(num_pad[y][x], num_pad[y-1][x], c='^')
        # down
        if y < len(num_pad)-1:
            if num_pad[y+1][x] != '*':
                npg.add_edge(num_pad[y][x], num_pad[y+1][x], c='v')
        # left
        if x > 0:
            if num_pad[y][x-1] != '*':
                npg.add_edge(num_pad[y][x], num_pad[y][x-1], c='<')
        # right
        if x < len(num_pad[y])-1:
            if num_pad[y][x+1] != '*':
                npg.add_edge(num_pad[y][x], num_pad[y][x+1], c='>')
kpg = nx.DiGraph()
for y in range(len(key_pad)):
    for x in range(len(key_pad[y])):
        if key_pad[y][x] == '*':
            continue
        # up
        if y > 0:
            if key_pad[y-1][x] != '*':
                kpg.add_edge(key_pad[y][x], key_pad[y-1][x], c='^')
        # down
        if y < len(key_pad)-1:
            if key_pad[y+1][x] != '*':
                kpg.add_edge(key_pad[y][x], key_pad[y+1][x], c='v')
        # left
        if x > 0:
            if key_pad[y][x-1] != '*':
                kpg.add_edge(key_pad[y][x], key_pad[y][x-1], c='<')
        # right
        if x < len(key_pad[y])-1:
            if key_pad[y][x+1] != '*':
                kpg.add_edge(key_pad[y][x], key_pad[y][x+1], c='>')

np_to_grid = dict()
for y in range(len(num_pad)):
    for x in range(len(num_pad[y])):
        if num_pad[y][x] != '*':
            np_to_grid[num_pad[y][x]] = (y, x)
kp_to_grid = dict()
for y in range(len(key_pad)):
    for x in range(len(key_pad[y])):
        if key_pad[y][x] != '*':
            kp_to_grid[key_pad[y][x]] = (y, x)

def numTurns(path, grid):
    if len(path) < 3:
        return(0)
    turns = 0
    y1, x1 = grid[path[0]]
    y2, x2 = grid[path[1]]
    yd = y2 - y1
    xd = x2 - x1
    y1, x1 = y2, x2
    for n in path[2:]:
        y2, x2 = grid[n]
        new_yd = y2 - y1
        new_xd = x2 - x1
        if new_yd != yd or new_xd != xd:
            turns += 1
        yd = new_yd
        xd = new_xd
        y1, x1 = y2, x2
    return(turns)

def kpToNp(start, dest, npg):
    filtered_paths = []
    paths = list(nx.all_simple_paths(npg, start, dest))
    for path in paths:
        if numTurns(path, np_to_grid) > 1:
            continue
        c_list = []
        for i in range(len(path)-1):
            c_list.append(npg[path[i]][path[i+1]]['c'])
        c_list.append('A')
        filtered_paths.append(c_list)
    return(filtered_paths)

def kpToKp(start, dest, kpg):
    filtered_paths = []
    paths = list(nx.all_simple_paths(kpg, start, dest))
    for path in paths:
        if numTurns(path, kp_to_grid) > 1:
            continue
        c_list = []
        for i in range(len(path)-1):
            c_list.append(kpg[path[i]][path[i+1]]['c'])
        c_list.append('A')
        filtered_paths.append(c_list)
    return(filtered_paths)

kp_pairs = dict()
for pair in kp_paths.keys():
    kp_list = kp_paths[pair]
    if len(kp_list) == 1:
        kp_pairs[''.join(pair)] = kp_list[0]
        continue
    pair_list = []
    cur = kp_list[0]
    for next in kp_list[1:]:
        pair_list.append(''.join([cur, next]))
        cur = next
    kp_pairs[''.join(pair)] = pair_list
kp_pairs['A'] = ['A']

total = 0
for code in ls:
    full_presses = []
    np_start = 'A'
    for np_dest in code:
        pair_counts = Counter()
        code_presses = ''
        np_path = ''.join(np_paths[(np_start, np_dest)][0])
        code_presses = 'A' + np_path
        p1 = code_presses[0]
        for p2 in code_presses[1:]:
            pair_counts[''.join([p1,p2])] += 1
            p1 = p2
        for i in range(num_robots):
            new_pair_counts = Counter()
            # figure all the new output pairs
            for pair in pair_counts.keys():
                for p in kp_pairs[pair]:
                    new_pair_counts[p] += pair_counts[pair]
            pair_counts = new_pair_counts
        kp_len = 0
        for pair in pair_counts.keys():
            kp_len += pair_counts[pair]
        full_presses.append(kp_len)
        np_start = np_dest
    # get the 'complexity' of the code
    code_num = int(code[:-1])
    sub_total = sum(full_presses)
    total += sub_total*code_num

print(total)
