# Day 6 part 1
from time import perf_counter
from concurrent.futures import ProcessPoolExecutor

d_list = ['^', '>', 'v', '<']
d = {'^':[-1,0], '>':[0,1], 'v':[1,0], '<':[0,-1]}

def onMap(coords, m):
    if coords[0] > -1 and coords[1] > -1 and coords[0] < len(m) \
            and coords[1] < len(m[0]):
        return(True)
    return(False)

# for part 2
def doSubRange(y, m, pos):
    '''Count the looping blocks in a single line. Return that number'''
    loop_limit = len(m) * len(m[0])
    total = 0
    for x in range(len(m[0])):
        # change out a . for a # and test for looping
        if m[y][x] == '.':
            # test if a loop
            cur = pos.copy()
            step_count = 0
            d_num = 0
            cur_d = d_list[d_num]
            while onMap(cur, m):
                step_count += 1
                new_d = d_num
                new_coord = cur.copy()
                new_coord[0] = cur[0] + d[cur_d][0]
                new_coord[1] = cur[1] + d[cur_d][1]
                while onMap(new_coord, m) and \
                        (m[new_coord[0]][new_coord[1]] == '#' or \
                        (new_coord[0] == y and new_coord[1] == x)):
                    new_d = (new_d + 1) % 4
                    cur_d = d_list[new_d]
                    new_coord[0] = cur[0] + d[cur_d][0]
                    new_coord[1] = cur[1] + d[cur_d][1]
                cur = new_coord
                d_num = new_d
                if step_count > loop_limit:
                    total += 1
                    break
    return(total)

def task_wrapper(args):
    return(doSubRange(*args))

def main():
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
    parameters = [(y, map, start) for y in range(len(map))]
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(task_wrapper, parameters))
    print(sum(results))
    T1 = perf_counter()
    print(f'Part 2 took {T1-T0} seconds in parallel')

if __name__ == "__main__":
    main()
