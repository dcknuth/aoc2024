# Day 1 part 1

filename = 'test01.txt'
filename = 'input01.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

l1 = []
l2 = []
for l in ls:
    p1, p2 = l.split()
    l1.append(int(p1))
    l2.append(int(p2))
l1.sort()
l2.sort()
total = 0
for i in range(len(l1)):
    total += abs(l1[i] - l2[i])
print(total)

# part 2
from collections import Counter
total = 0
for i in range(len(l1)):
    cur_count = 0
    for j in l2:
        if l1[i] == j:
            cur_count += 1
    total += cur_count * l1[i]
print(f"Sim score is {total}")
