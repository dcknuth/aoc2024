# Day 2 part 1

filename = 'test02.txt'
filename = 'input02.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

def isSafe(d):
    i = 0
    if d[-1] - d[0] > 0:
        increasing = True
    else:
        increasing = False
    i += 1
    for x in range(len(d)-1):
        if increasing:
            if d[i] > d[x] and 3 >= d[i] - d[x]:
                pass
            else:
                return(False)
        else:
            if d[i] < d[x] and 3 >= d[x] - d[i]:
                pass
            else:
                return(False)
        i += 1
    return(True)

total = 0
for l in ls:
    l = [int(x) for x in l.split()]
    if isSafe(l):
        total += 1
print(f'Number of safe reports is {total}')

# part 2
total = 0
for l in ls:
    l = [int(x) for x in l.split()]
    for i in range(len(l)):
        cur_l = [l[j] for j in range(len(l)) if j != i]
        if isSafe(cur_l):
            total += 1
            break
print(f'Number of safe reports is {total}')
