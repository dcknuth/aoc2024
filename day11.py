# Day 11 part 1

filename = 'test11.txt'
filename = 'input11.txt'

with open(filename) as f:
    ls = f.read().strip()

stones = [x for x in ls.split()]
print(stones)

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

for i in range(25):
    stones = blink(stones)
print(len(stones))

# part 2
stones = [x for x in ls.split()]
last_len = len(stones)
#print(f'Initial len is {last_len}')
for i in range(25):
    stones = blink(stones)
    cur_len = len(stones)
    #print(f'{i=} {last_len=} {cur_len=} delta={cur_len-last_len}')
    last_len = cur_len
print("Too busy. Let's see if each part loops")
print("First 10 of each part")
stones = [x for x in ls.split()]
for stone in stones:
    #print("Cur stone is", stone)
    cur_stones = [stone]
    last_len = len(cur_stones)
    for i in range(10):
        cur_stones = blink(cur_stones)
        cur_len = len(cur_stones)
        #print(f'{i=} {last_len=} {cur_len=} delta={cur_len-last_len}')
        last_len = cur_len
print("Still too busy. Need another approach. What happens with just 0")
stones = ['0']
for i in range(15):
    stones = blink(stones)
    print(stones)
print("At least some numbers will repeat with a predictable pattern.")
print("Will all of them do so for 0?")
from collections import Counter
seen = Counter()
stones = ['0']
for i in range(15):
    for stone in stones:
        seen[stone] += 1
    done = True
    for stone in seen.keys():
        if seen[stone] == 1:
            done = False
    if done:
        print(f'Done in {i} loops')
        break
    stones = blink(stones)
for num in seen.keys():
    print(f'{num=} {seen[num]=}')
print("Yes. Are all our numbers here? Yes.")
print("So we will need to see where each number is just repeating sets")

def makeIndex(n):
    steps = 0
    index = Counter()
    index[n] += 1
    stones = [n]
    for i in range(50):
        stones = blink(stones)
        done = True
        for stone in stones:
            index[stone] += 1
            if index[stone] == 1:
                done = False
        steps += 1
        if done:
            return(steps, index)
    # should not get here if this works
    return(-1, index)

# indexes = dict()
# for n in ls.split():
#     steps, index = makeIndex(n)
#     indexes[n] = [steps, index]
print("We have four numbers that are not looping.")
print("Looking farther is not helping. I need a new plan.")
print("Let's focus on removing parts that do loop and pre-summing those")

# wait, let's just do counts of things and splits/transitions
from collections import defaultdict
transitions = defaultdict(list)
stone_counts = Counter()
for stone in ls.split():
    stone_counts[stone] += 1
for i in range(75):
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
print(sum(stone_counts.values()))

