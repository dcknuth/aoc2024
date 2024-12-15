# Day 13 part 1

filename = 'test13.txt'
filename = 'input13.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

machines = []
i = 0
while i < len(ls):
    if ls[i] == '':
        i += 1
        continue
    _, a = ls[i].split(': ')
    _, b = ls[i+1].split(': ')
    _, p = ls[i+2].split(': ')
    ax, ay = a.split(', ')
    ax = int(ax[2:])
    ay = int(ay[2:])
    bx, by = b.split(', ')
    bx = int(bx[2:])
    by = int(by[2:])
    px, py = p.split(', ')
    px = int(px[2:])
    py = int(py[2:])
    machines.append([(ax, ay), (bx, by), (px, py)])
    i += 3

def bfSolve(m):
    a, b, p = m
    ax, ay = a
    bx, by = b
    px, py = p
    i = max(px//ax, py//ay)
    j = max(py//ay, py//by)
    big_n = 1_000_000_000_000
    win_min = big_n
    for a_num in range(i+1):
        for b_num in range(j+1):
            if a_num*ax + b_num*bx == px and a_num*ay + b_num*by == py:
                win = 3*a_num + b_num
                if win_min > win:
                    win_min = win
    if win_min < big_n:
        return(win_min)
    return(0)

total = 0
for m in machines:
    win = bfSolve(m)
    total += win
print(total)

# part 2
import numpy as np

def npSolve(m):
    a, b, p = m
    ax, ay = a
    bx, by = b
    coeffs = np.array([[ax, bx], [ay, by]])
    consts = np.array(p) + 10_000_000_000_000
    ans = np.linalg.solve(coeffs, consts)
    return(ans)

total = 0
for m in machines:
    ans = npSolve(m)
    round_a = round(ans[0])
    round_b = round(ans[1])
    x = round_a * m[0][0] + round_b * m[1][0]
    y = round_a * m[0][1] + round_b * m[1][1]
    if x == m[2][0] + 10_000_000_000_000 and \
        y == m[2][1] + 10_000_000_000_000:
        total += 3*round_a + round_b
print(total)
