# Day 6 part 1
from time import perf_counter

filename = 'test06.txt'
filename = 'input06.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

T0 = perf_counter()
start = [-1, -1]
map = []
for i, l in enumerate(ls):
    map.append([c for c in l])
    if '^' in l:
        start[0] = i
        start[1] = l.find('^')
d_list = ['^', '>', 'v', '<']
d = {'^':[-1,0], '>':[0,1], 'v':[1,0], '<':[0,-1]}

def onMap(coords, m):
    if coords[0] > -1 and coords[1] > -1 and coords[0] < len(m) \
            and coords[1] < len(m[0]):
        return(True)
    return(False)

cur = start.copy()
visited = dict()
total = 0
d_num = 0
cur_d = d_list[d_num]
while onMap(cur, map):
    if tuple(cur) not in visited:
        total += 1
        visited[tuple(cur)] = True
    new_d = d_num
    new_coord = cur.copy()
    new_coord[0] = cur[0] + d[cur_d][0]
    new_coord[1] = cur[1] + d[cur_d][1]
    while onMap(new_coord, map) and map[new_coord[0]][new_coord[1]] == '#':
        new_d = (d_num + 1) % 4
        cur_d = d_list[new_d]
        new_coord[0] = cur[0] + d[cur_d][0]
        new_coord[1] = cur[1] + d[cur_d][1]
    cur = new_coord
    d_num = new_d
print(total)
T1 = perf_counter()
print(f'Part 1 took {T1-T0} seconds')

# part 2
T0 = perf_counter()
loop_positions = []
loop_limit = len(map) * len(map[0])
for y in range(len(map)):
    #print(f'starting row {y}')
    for x in range(len(map[0])):
        # change out a . for a # and test for looping
        if map[y][x] == '.':
            map[y][x] = '#'
            # test if a loop
            cur = start.copy()
            step_count = 0
            d_num = 0
            cur_d = d_list[d_num]
            while onMap(cur, map):
                step_count += 1
                new_d = d_num
                new_coord = cur.copy()
                new_coord[0] = cur[0] + d[cur_d][0]
                new_coord[1] = cur[1] + d[cur_d][1]
                while onMap(new_coord, map) and \
                        map[new_coord[0]][new_coord[1]] == '#':
                    new_d = (new_d + 1) % 4
                    cur_d = d_list[new_d]
                    new_coord[0] = cur[0] + d[cur_d][0]
                    new_coord[1] = cur[1] + d[cur_d][1]
                cur = new_coord
                d_num = new_d
                if step_count > loop_limit:
                    loop_positions.append([y, x])
                    break
            # change back
            map[y][x] = '.'
# print the number of loops
print(len(loop_positions))
T1 = perf_counter()
print(f'Part 2 took {T1-T0} seconds')
