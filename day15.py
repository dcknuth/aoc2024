# Day 15 part 1

filename = 'test15.txt'
filename = 'test15-2.txt'
filename = 'test15-3.txt'
#filename = 'input15.txt'
move_dir = {'^':[-1, 0], '>':[0, 1], 'v':[1, 0], '<':[0, -1]}

with open(filename) as f:
    ls = f.read().strip().split('\n')

r_pos = [-1, -1]
map = []
for i, l in enumerate(ls):
    if l == '':
        break
    row = [x for x in l]
    map.append(row)
    if '@' in row:
        r_pos[0] = i
        r_pos[1] = row.index('@')
moves = []
for l in ls[len(map):]:
    moves.extend([x for x in l])

def printMap(map):
    for row in map:
        print(''.join(row))

def doMove(map, r_pos, dy, dx):
    if map[r_pos[0]+dy][r_pos[1]+dx] == '.':
        map[r_pos[0]+dy][r_pos[1]+dx] = '@'
        map[r_pos[0]][r_pos[1]] = '.'
        r_pos[0] += dy
        r_pos[1] += dx
    elif map[r_pos[0]+dy][r_pos[1]+dx] == '#':
        pass
    elif map[r_pos[0]+dy][r_pos[1]+dx] == 'O':
        i = 2
        while map[r_pos[0]+dy*i][r_pos[1]+dx*i] != '#' and \
            map[r_pos[0]+dy*i][r_pos[1]+dx*i] != '.':
            i += 1
        if map[r_pos[0]+dy*i][r_pos[1]+dx*i] == '.':
            while i > 0:
                map[r_pos[0]+dy*i][r_pos[1]+dx*i] = \
                    map[r_pos[0]+dy*(i-1)][r_pos[1]+dx*(i-1)]
                i -= 1
            map[r_pos[0]][r_pos[1]] = '.'
            r_pos[0] += dy
            r_pos[1] += dx
    else:
        print(f'Error: {r_pos=} {dy=} {dx=}')

for move in moves:
    dy, dx = move_dir[move]
    doMove(map, r_pos, dy, dx)

total = 0
for y in range(1, len(map)-1):
    for x in range(1, len(map[0])-1):
        if map[y][x] == 'O':
            total += 100 * y + x
print(total)
#printMap(map)

# part 2
wide_map = []
for row in ls:
    if row == '':
        break
    new_row = []
    for c in row:
        if c == '@':
            new_row.extend(['@', '.'])
        elif c == 'O':
            new_row.extend(['[', ']'])
        else:
            new_row.extend([c] * 2)
    wide_map.append(new_row)
printMap(wide_map)
