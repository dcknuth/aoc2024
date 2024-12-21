# Day 18 part 1
import functools
from collections import defaultdict

filename = 'test19.txt'
filename = 'input19.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

towels = ls[0].split(', ')
patterns = ls[2:]

@functools.lru_cache(maxsize=None)
def findPat(pat, in_pat):
    for t in in_pat:
        if pat.find(t) == 0:
            if t == pat:
                return(True)
            else:
                if findPat(pat[len(t):], in_pat):
                    return(True)
    return(False)

total = 0
for pattern in patterns:
    in_pat = []
    for towel in towels:
        if towel in pattern:
            in_pat.append(towel)
    if findPat(pattern, tuple(in_pat)):
        total += 1
print(total)

# part 2
@functools.lru_cache(maxsize=None)
def findPatCount(pat, in_pat):
    if len(pat) == 0:
        return(0)
    count = 0
    for t in in_pat:
        if pat.find(t) == 0:
            if t == pat:
                if len(t) == 1:
                    return(1)
                else:
                    temp_pat = list(in_pat)
                    temp_pat.remove(t)
                    if len(temp_pat) > 0:
                        return(1 + findPatCount(pat, tuple(temp_pat)))
            else:
               count += (findPatCount(pat[len(t):], in_pat))
    return(count)

total = 0
for pattern in patterns:
    in_pat = []
    for towel in towels:
        if towel in pattern:
            in_pat.append(towel)
    total += findPatCount(pattern, tuple(in_pat))
print(total)
