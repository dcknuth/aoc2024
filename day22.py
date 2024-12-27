# Day 22 part 1
# What is the sum of the 2000th secret number generated by each buyer?

filename = "test22.txt"
filename = "test22-2.txt"
filename = "input22.txt"
MOD_NUM = 16_777_216
GEN_NUM = 2000

with open(filename) as f:
    ls = f.read().strip().split("\n")

seeds = [int(x) for x in ls]

def step1(n):
    m = n * 64
    # mix
    n = n ^ m
    # prune
    return(n % MOD_NUM)

def step2(n):
    m = n // 32
    n = n ^ m
    return(n % MOD_NUM)

def step3(n):
    m = n * 2048
    n = n ^ m
    return(n % MOD_NUM)

nth_list = []
for seed in seeds:
    num = seed
    for i in range(GEN_NUM):
        num = step3(step2(step1(num)))
    nth_list.append(num)
print(sum(nth_list))

# part 2
# run again but save last digits, changes and prices following 4 changes
from collections import defaultdict
by_deltas = defaultdict(lambda: defaultdict(list))
for seed in seeds:
    str_num = str(seed)
    deltas = []
    last = int(str_num[-1])
    num = seed
    for i in range(GEN_NUM):
        num = step3(step2(step1(num)))
        str_num = str(num)
        price = int(str_num[-1])
        cur_delta = price - last
        if len(deltas) > 3:
            deltas.pop(0)
            deltas.append(cur_delta)
        else:
            deltas.append(cur_delta)
        if len(deltas) > 3:
            by_deltas[tuple(deltas)][seed].append((i, price))
        last = price

# now look through and save the best
most_bananas = [0, (-1, -1, -1, -1)]
for d in by_deltas.keys():
    bananas = 0
    for s in by_deltas[d].keys():
        bananas += by_deltas[d][s][0][1]
    if bananas > most_bananas[0]:
        most_bananas = [bananas, d]
print(f'{most_bananas[0]} at {most_bananas[1]}')
