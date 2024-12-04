# Day 4 part 1
from collections import defaultdict

filename = 'test04.txt'
filename = 'input04.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

m = [[x for x in y] for y in ls]
s = ['X', 'M', 'A', 'S']

words = defaultdict(list)
for y in range(len(m)):
    for x in range(len(m[0])):
        if m[y][x] == s[0]:
            # up
            if y >= len(s)-1:
                found = True
                for i in range(1, len(s)):
                    if m[y-i][x] != s[i]:
                        found = False
                        break
                if found:
                    words[(y, x)].append('up')
                # up-left
                if x >= len(s)-1:
                    found = True
                    for i in range(1, len(s)):
                        if m[y-i][x-i] != s[i]:
                            found = False
                            break
                    if found:
                        words[(y, x)].append('up-left')
                # up-right
                if x <= len(m[0]) - len(s) :
                    found = True
                    for i in range(1, len(s)):
                        if m[y-i][x+i] != s[i]:
                            found = False
                            break
                    if found:
                        words[(y, x)].append('up-right')
            # down
            if y <= len(m) - len(s) :
                found = True
                for i in range(1, len(s)):
                    if m[y+i][x] != s[i]:
                        found = False
                        break
                if found:
                    words[(y, x)].append('down')
                # down-left
                if x >= len(s)-1:
                    found = True
                    for i in range(1, len(s)):
                        if m[y+i][x-i] != s[i]:
                            found = False
                            break
                    if found:
                        words[(y, x)].append('down-left')
                # down-right
                if x <= len(m[0]) - len(s) :
                    found = True
                    for i in range(1, len(s)):
                        if m[y+i][x+i] != s[i]:
                            found = False
                            break
                    if found:
                        words[(y, x)].append('down-right')
            # right
            if x <= len(m[0]) - len(s) :
                found = True
                for i in range(1, len(s)):
                    if m[y][x+i] != s[i]:
                        found = False
                        break
                if found:
                    words[(y, x)].append('right')
            # left
            if x >= len(s) - 1:
                found = True
                for i in range(1, len(s)):
                    if m[y][x-i] != s[i]:
                        found = False
                        break
                if found:
                    words[(y, x)].append('left')

total = 0
for node in words.keys():
    total += len(words[node])
print("Number of XMAS is", total)

# part 2
def isMatch(m, y, x):
    '''Test for match including bounds testing'''
    if y > 0 and x > 0 and y < len(m)-1 and x < len(m[0])-1:
        # test RL down diag
        if m[y-1][x-1] == 'M' and  m[y+1][x+1] != 'S':
            return(False)
        elif m[y-1][x-1] == 'S' and m[y+1][x+1] != 'M':
            return(False)
        elif m[y-1][x-1] != 'M' and m[y+1][x+1] != 'M':
            return(False)
        elif m[y-1][x-1] != 'S' and m[y+1][x+1] != 'S':
            return(False)
        # test LR up diag
        if m[y+1][x-1] == 'M' and m[y-1][x+1] != 'S':
            return(False)
        elif m[y+1][x-1] == 'S' and m[y-1][x+1] != 'M':
            return(False)
        elif m[y+1][x-1] != 'M' and m[y-1][x+1] != 'M':
            return(False)
        elif m[y+1][x-1] != 'S' and m[y-1][x+1] != 'S':
            return(False)
        return(True)
    return(False)

total = 0
for y in range(len(m)):
    for x in range(len(m[0])):
        if m[y][x] == 'A' and isMatch(m, y, x):
            total += 1
print("Number of X-MAS is", total)
