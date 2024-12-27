# Day 21 part 1
import networkx as nx

filename = "test21.txt"
filename = "input21.txt"

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

# Now that we have our graphs, we can find the shortest path to each code
# Since doing the whole code was too memory intensive, we will just do one
#  traversal at a time
def kpToNp(start, dest, npg):
    all_paths = []
    paths = nx.all_shortest_paths(npg, start, dest)
    for path in paths:
        c_list = []
        for i in range(len(path)-1):
            c_list.append(npg[path[i]][path[i+1]]['c'])
        c_list.append('A')
        all_paths.append(''.join(c_list))
    return(all_paths)

def kpToKP(presses, kpg):
    all_presses = []
    for cur_presses in presses:
        new_presses = []
        start = 'A'
        for p in cur_presses:
            all_paths = []
            paths = list(nx.all_shortest_paths(kpg, start, p))
            for path in paths:
                c_list = []
                for i in range(len(path)-1):
                    c_list.append(kpg[path[i]][path[i+1]]['c'])
                c_list.append('A')
                all_paths.append(''.join(c_list))
            start = p
            if len(new_presses) == 0:
                for path_to_cur_dest in all_paths:
                    new_presses.append(path_to_cur_dest)
            else:
                temp_presses = []
                for path_so_far in new_presses:
                    for path_to_cur_dest in all_paths:
                        temp_presses.append(path_so_far+path_to_cur_dest)
                new_presses = temp_presses
        all_presses.extend(new_presses)
    return(all_presses)

def onlyShortest(presses):
    shortest = []
    for p in presses:
        if len(shortest) == 0:
            shortest.append(p)
        elif len(p) < len(shortest[0]):
            shortest = [p]
        elif len(p) == len(shortest[0]):
            shortest.append(p)
    return(shortest)

full_presses = []
for code in ls:
    code_presses = ''
    start = 'A'
    for np_dest in code:
        presses = kpToNp(start, np_dest, npg)
        presses = kpToKP(presses, kpg)
        presses = onlyShortest(presses)
        presses = kpToKP(presses, kpg)
        presses = onlyShortest(presses)
        code_presses = code_presses + presses[0]
        start = np_dest
    full_presses.append(code_presses)
# now get the 'complexities'
total = 0
for i, presses in enumerate(full_presses):
    code_num = int(ls[i][:-1])
    print(f'{ls[i]}: {code_num=} {len(presses)}')
    total += len(presses) * code_num
print(total)
