# Day 5 part 1

filename = 'test05.txt'
filename = 'input05.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

orders = []
updates = []

i = 0
for l in ls:
    i += 1
    if l == '':
        break
    before, after = l.split('|')
    orders.append((before, after))
for l in ls[i:]:
    updates.append(list(l.split(',')))

total = 0
for pages in updates:
    in_order = True
    for i, page in enumerate(pages):
        for order in orders:
            if page in order:
                if order[0] == page:
                    if order[1] in pages[:i]:
                        in_order = False
                        break
                elif order[1] == page:
                    if order[0] in pages[i+1:]:
                        in_order = False
                        break
        if in_order == False:
            break
    if in_order:
        total += int(pages[len(pages)//2])
print("Middle page totals is", total)

# part 2
from functools import cmp_to_key
from collections import defaultdict

def page_key(x, y):
    if x in less_list:
        if y in less_list[x]:
            return(-1)
    if x in more_list:
        if y in more_list[x]:
            return(1)
    return(0)

less_list = defaultdict(list)
more_list = defaultdict(list)
for x, y in orders:
    less_list[x].append(y)
    more_list[y].append(x)

total = 0
for pages in updates:
    in_order = True
    for i, page in enumerate(pages):
        for order in orders:
            if page in order:
                if order[0] == page:
                    if order[1] in pages[:i]:
                        in_order = False
                        break
                elif order[1] == page:
                    if order[0] in pages[i+1:]:
                        in_order = False
                        break
        if in_order == False:
            break
    if not in_order:
        temp_pages = sorted(pages, key=cmp_to_key(page_key))
        total += int(temp_pages[len(pages)//2])
print("Middle page totals is", total)
