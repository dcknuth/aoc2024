# Day 3 part 1

filename = 'test03.txt'
#filename = 'input03.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

print(ls)
