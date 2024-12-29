# Day 25 part 1

filename = "test25.txt"
filename = "input25.txt"

with open(filename) as f:
    ls = f.read().strip().split("\n")

locks = []
keys = []
i = 0
while i < len(ls):
    if ls[i] == '':
        i += 1
        continue
    is_lock = False
    cur_item = [0 for x in range(5)]
    for j in range(7):
        if j == 6:
            continue
        if j == 0:
            if ls[i+j][0] == '#':
                is_lock = True
            continue
        else:
            for k, c in enumerate(ls[i+j]):
                if c == '#':
                    cur_item[k] += 1
    if is_lock:
        locks.append(cur_item)
    else:
        keys.append(cur_item)
    i += 7

total = 0
for lock in locks:
    for key in keys:
        fits = True
        for i in range(5):
            if lock[i] + key[i] > 5:
                fits = False
                break
        if fits:
            total += 1
print(total)
