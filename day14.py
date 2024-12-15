# Day 14 part 1

filename = 'test14.txt'
filename = 'input14.txt'
TALL = 7
WIDE = 11
TALL = 103
WIDE = 101
QX_CUT = round((WIDE-1)/2)
QY_CUT = round((TALL-1)/2)
SECONDS = 100

with open(filename) as f:
    ls = f.read().strip().split('\n')

robots = []
for l in ls:
    p, v = l.split()
    p = p[2:]
    v = v[2:]
    px, py = map(int, p.split(','))
    vx, vy = map(int, v.split(','))
    robots.append([px, py, vx, vy])

positions = []
counts = [0 for x in range(5)]
for r in robots:
    px, py, vx, vy = r
    x = (px + vx * SECONDS) % WIDE
    y = (py + vy * SECONDS) % TALL
    positions.append([x, y])
    if x < QX_CUT and y < QY_CUT:
        counts[0] += 1
    elif x > QX_CUT and y < QY_CUT:
        counts[1] += 1
    elif x < QX_CUT and y > QY_CUT:
        counts[2] += 1
    elif x > QX_CUT and y > QY_CUT:
        counts[3] += 1
    else:
        counts[4] += 1
        #print(f'On midway lines {x=} {y=}')
total = 1
for i in range(4):
    total *= counts[i]
print(total)

# part 2
# Guess that the top row will have 1 robot and the next couple will have
#  two when the picture is complete. Also the next to last few rows should
#  have 2 for the trunk
m = [[0 for x in range(WIDE)] for y in range(TALL)]

def updateMatrix(m, p, n):
    for x, y in p:
        m[y][x] = n

def treeTest(m):
    '''Look for the top and bottom of a big tree'''
    if sum(m[0]) == 1 and sum(m[1]) == 2 and sum(m[2]) == 2 and \
        sum(m[3]) == 2 and sum(m[-2]) == 2 and sum(m[-3]) == 2 and \
        sum(m[-4]) == 2:
        return(True)
    return(False)

def treeTest2(m):
    '''Look for a filled block indicating a smaller, filled-in
    tree'''
    for y in range(TALL-5):
        for x in range(WIDE - 5):
            total = 0
            total += sum(m[y][x:x+4])
            total += sum(m[y+1][x:x+4])
            total += sum(m[y+2][x:x+4])
            total += sum(m[y+3][x:x+4])
            if total == 16:
                return(True)
    return(False)

def stepSec(robots, s):
    positions = []
    for r in robots:
        px, py, vx, vy = r
        x = (px + vx * s) % WIDE
        y = (py + vy * s) % TALL
        positions.append([x, y])
    return(positions)

for s in range(1, 100_000):
    positions = stepSec(robots, s)
    updateMatrix(m, positions, 1)
    if treeTest2(m):
        print(f'Displays tree after {s} seconds')
        break
    updateMatrix(m, positions, 0)
