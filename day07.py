# Day 7 part 1
from itertools import product

filename = 'test07.txt'
filename = 'input07.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

tests = []
for l in ls:
    nums = l.split(': ')
    ans = int(nums[0])
    ops = list(map(int, nums[1].split()))
    tests.append([ans, ops])

total = 0
for ans, operands in tests:
    for ops in product(['+', '*'], repeat=len(operands)-1):
        result = operands[0]
        for i in range(1, len(operands)):
            if ops[i-1] == '+':
                result += operands[i]
            else:
                result *= operands[i]
        if ans == result:
            total += ans
            break
print(total)

# part 2
total = 0
for ans, operands in tests:
    for ops in product(['+', '*', 'c'], repeat=len(operands)-1):
        result = operands[0]
        for i in range(1, len(operands)):
            if ops[i-1] == '+':
                result += operands[i]
            elif ops[i-1] == '*':
                result *= operands[i]
            else:
                result = result * 10 ** len(str(operands[i])) + operands[i]
            if result > ans:
                break
        if ans == result:
            total += ans
            break
print(total)
