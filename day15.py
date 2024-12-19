# Day 15 part 1

#filename = 'test15.txt'
#filename = 'test15-2.txt'
#filename = 'test15-3.txt'
#filename = 'test15-4.txt'
#filename = 'test15-5.txt'
#filename = 'test15-6.txt'
filename = 'input15.txt'
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
#printMap(wide_map)
found = False
for y in range(len(wide_map)):
    if not found:
        for x in range(len(wide_map[0])):
            if wide_map[y][x] == '@':
                r_pos[0] = y
                r_pos[1] = x
                found = True
                break

def canMove(map, lb, rb, dy):
    ly, lx = lb
    ry, rx = rb
    if map[ly+dy][lx] == '#':
        return(False)
    if map[ly+dy][lx] == '.' and map[ry+dy][rx] == '.':
        return(True)
    if map[ly+dy][lx] == '[':
        return(canMove(map, (ly+dy, lx), (ry+dy, rx), dy))
    if map[ly+dy][lx] == ']' and map[ly][lx] == '@':
        return(canMove(map, (ly+dy, lx-1), (ly+dy, lx), dy))
    if map[ly+dy][lx] == ']' and map[ry+dy][rx] == '.':
        return(canMove(map, (ly+dy, lx-1), (ly+dy, lx), dy))
    if map[ly+dy][lx] == ']' and map[ry+dy][rx] == '#':
        return(False)
    if map[ly+dy][lx] == ']' and map[ry+dy][rx] == '[':
        return(canMove(map, (ly+dy, lx-1), (ly+dy, lx), dy) and \
               canMove(map, (ry+dy, rx), (ry+dy, rx+1), dy))
    if map[ly+dy][lx] == '.' and map[ry+dy][rx] == '[':
        return(canMove(map, (ry+dy, rx), (ry+dy, rx+1), dy))
    return(False)

def moveBox(map, ly, lx, ry, rx, dy):
    if map[ly][lx] == '.' and map[ry][rx] == '.':
        return()
    if map[ly][lx] == '@':
        if map[ly+dy][lx] == '[':
            moveBox(map, ly+dy, lx, ry+dy, lx+1, dy)
            map[ly+dy][lx] = '@'
            map[ly+dy][lx+1] ='.'
            map[ly][lx] = '.'
            return()
        if map[ly+dy][lx] == ']':
            moveBox(map, ly+dy, lx-1, ry+dy, lx, dy)
            map[ly+dy][lx] = '@'
            map[ly+dy][lx-1] ='.'
            map[ly][lx] = '.'
            return()
    if map[ly][lx] == '[':
        if map[ly+dy][lx] == '[':
            moveBox(map, ly+dy, lx, ry+dy, lx+1, dy)
            map[ly+dy][lx] = '['
            map[ly+dy][lx+1] =']'
            map[ly][lx] = '.'
            map[ry][rx] = '.'
            return()
        elif map[ly+dy][lx] == ']':
            moveBox(map, ly+dy, lx-1, ry+dy, lx, dy)
            moveBox(map, ly+dy, lx+1, ry+dy, lx+2, dy)
            map[ly+dy][lx] = '['
            map[ly+dy][lx+1] =']'
            map[ly][lx] = '.'
            map[ry][rx] = '.'
            return()
        elif map[ry+dy][rx] == '[':
            moveBox(map, ly+dy, lx+1, ry+dy, lx+2, dy)
            map[ly+dy][lx] = '['
            map[ly+dy][lx+1] =']'
            map[ly][lx] = '.'
            map[ry][rx] = '.'
            return()
        else:
            map[ly+dy][lx] = '['
            map[ly+dy][lx+1] =']'
            map[ly][lx] = '.'
            map[ry][rx] = '.'
            return()

def doMoveW(map, r_pos, dy, dx):
    if map[r_pos[0]+dy][r_pos[1]+dx] == '.':
        map[r_pos[0]+dy][r_pos[1]+dx] = '@'
        map[r_pos[0]][r_pos[1]] = '.'
        r_pos[0] += dy
        r_pos[1] += dx
    elif map[r_pos[0]+dy][r_pos[1]+dx] == '#':
        return()
    elif map[r_pos[0]+dy][r_pos[1]+dx] == '[' or \
        map[r_pos[0]+dy][r_pos[1]+dx] == ']':
        if dy == 0: # moving horizontal, like part 1
            i = 3
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
            if canMove(map, (r_pos[0], r_pos[1]), (r_pos[0], r_pos[1]+1), dy):
                moveBox(map, r_pos[0], r_pos[1], r_pos[0], r_pos[1]+1, dy)
                r_pos[0] += dy
                r_pos[1] += dx
    else:
        print(f'Error: doMoveW {r_pos=} {dy=} {dx=}')

for move in moves:
    dy, dx = move_dir[move]
    doMoveW(wide_map, r_pos, dy, dx)
    #printMap(wide_map)

total = 0
for y in range(1, len(wide_map)-1):
    for x in range(1, len(wide_map[0])-1):
        if wide_map[y][x] == '[':
            total += 100 * y + x
print(total)