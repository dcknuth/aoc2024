# Day 3 part 1
import re

filename = 'test03.txt'
filename = 'input03.txt'
#filename = 'test03-2.txt'

with open(filename) as f:
    ls = f.read().strip()

func_ex = r'mul\((\d{1,3}),(\d{1,3})\)'
matches = re.findall(func_ex, ls, re.MULTILINE)

total = 0
for p1, p2 in matches:
    total += int(p1) * int(p2)
    #print(f"Parameters: {p1} {p2}")
print(total)

# part 2
func_ex = r'(mul\((\d{1,3}),(\d{1,3})\))|(do)\(\)|(don\'t)\(\)'
matches = re.findall(func_ex, ls, re.MULTILINE)

total = 0
summing = True
for parts in matches:
    if 'mul' in parts[0] and summing:
        p1, p2 = parts[0][4:].split(',')
        p2 = p2[:-1]
        total += int(p1) * int(p2)
    elif 'do' in parts[3]:
        summing = True
    elif "don't" in parts[4]:
        summing = False
    elif summing:
        print("something's wrong", parts)
print(total)
