# Day 11 part 1
from collections import Counter
from collections import defaultdict

filename = 'test11.txt'
filename = 'input11.txt'

with open(filename) as f:
    ls = f.read().strip()

def r1(stone_list):
    if stone_list[0] == '0':
        stone_list[0] = '1'
        return(True)
    return(False)

def r2(stone_list):
    if len(stone_list[0]) % 2 == 1:
        return(False)
    old_stone = stone_list.pop()
    s1 = old_stone[:(len(old_stone)+1)//2]
    stone_list.append(s1)
    s2 = str(int(old_stone[(len(old_stone)+1)//2:]))
    stone_list.append(s2)
    return(True)

def r3(stone_list):
    stone_list[0] = str(int(stone_list[0]) * 2024)

def blink(stones):
    new_stones = []
    for stone in stones:
        stone_list = [stone]
        if r1(stone_list):
            new_stones.extend(stone_list)
        elif r2(stone_list):
            new_stones.extend(stone_list)
        else:
            r3(stone_list)
            new_stones.extend(stone_list)
    return(new_stones)

transitions = defaultdict(list)
stone_counts = Counter()
for stone in ls.split():
    stone_counts[stone] += 1
for i in range(75):
    # part 1
    if i == 25:
        print(sum(stone_counts.values()))
    new_counts = Counter()
    for stone in stone_counts.keys():
        if stone in transitions:
            for new_stone in transitions[stone]:
                new_counts[new_stone] += stone_counts[stone]
        else:
            blink_result = blink([stone])
            transitions[stone] = blink_result
            for new_stone in blink_result:
                new_counts[new_stone] += stone_counts[stone]
    stone_counts = new_counts
# part 2
print(sum(stone_counts.values()))
