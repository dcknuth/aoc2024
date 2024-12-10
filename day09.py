# Day 9 part 1
from collections import defaultdict

filename = 'test09.txt'
filename = 'input09.txt'

with open(filename) as f:
    ls = f.read().strip()

def expand(s):
    new_space = []
    is_file = True
    id = 0
    for c in s:
        size = int(c)
        if is_file:
            new_space.append([id, size])
            id += 1
            is_file = False
        else:
            if size > 0:
                new_space.append([-1, size])
            is_file = True
    # add an end space
    new_space.append([-1, 0])
    return(new_space)

def printDisk(d):
    for id, size in d:
        if id < 0:
            print('.' * size, end='')
        else:
            print(str(id) * size, end='')
    print()

d = expand(ls)

def compress(d):
    cur_end = len(d) - 2
    end_buf = len(d) - 1
    cur_buf = end_buf
    for i, cur_sec in enumerate(d):
        if cur_sec[0] == -1:
            cur_buf = i
            break
    while cur_buf != end_buf:
        buf_len = d[cur_buf][1]
        fill_len = d[cur_end][1]
        if fill_len == buf_len:
            move_buf = d.pop(cur_end)
            d.insert(cur_buf, move_buf)
            _ = d.pop(cur_buf + 1)
            d[-1][1] += buf_len
        elif fill_len > buf_len:
            move_buf = [d[cur_end][0], buf_len]
            d.insert(cur_buf, move_buf)
            _ = d.pop(cur_buf + 1)
            d[cur_end][1] -= buf_len
            d[end_buf][1] += buf_len
        elif fill_len < buf_len:
            move_buf = d.pop(cur_end)
            d.insert(cur_buf, move_buf)
            d[cur_buf+1][1] -= fill_len
            d[end_buf][1] += fill_len
        # trim extra blank sector at the end if needed
        if d[-2][0] == -1:
            d[-2][1] += d[-1][1]
            _ = d.pop()
        end_buf = len(d) - 1
        cur_end = len(d) - 2
        for i, cur_sec in enumerate(d):
            if cur_sec[0] == -1:
                cur_buf = i
                break
    return()

def findCS(d):
    total = 0
    block_num = 0
    for id, size in d:
        for x in range(size):
            if id > -1:
                total += id * block_num
            block_num += 1
    return(total)

compress(d)
print(findCS(d))

# part 2
d = expand(ls)
# no need for the 0 size end buffer anymore
d.pop()

def compressByFile(d):
    cur_end = len(d) - 1
    while cur_end > 0:
        #printDisk(d)
        if d[cur_end][0] == -1:
            cur_end -= 1
        else:
            for i in range(len(d)):
                if i >= cur_end:
                    cur_end -= 1
                    break
                if d[i][0] != -1 or d[i][1] < d[cur_end][1]:
                    continue
                else:
                    fill_len = d[cur_end][1]
                    if fill_len == d[i][1]:
                        move_file = d.pop(cur_end)
                        d.insert(i, move_file)
                        move_space = d.pop(i+1)
                        d.insert(cur_end, move_space)
                        cur_end -= 1
                    if fill_len < d[i][1]:
                        move_file = d.pop(cur_end)
                        d.insert(i, move_file)
                        d.insert(cur_end+1, [-1, fill_len])
                        d[i+1][1] -= fill_len
                    break
    return()

compressByFile(d)
print(findCS(d))
