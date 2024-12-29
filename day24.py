# Day 24 part 1
from itertools import combinations
from collections import defaultdict

filename = "test24.txt"
filename = "test24-2.txt"
filename = "input24.txt"

with open(filename) as f:
    ls = f.read().strip().split("\n")

wires = dict()
gates = dict()
i = 0
for l in ls:
    if l == '':
        i += 1
        break
    name, val = l.split(': ')
    if val == '1':
        wires[name] = True
    else:
        wires[name] = False
    i += 1
for l in ls[i:]:
    inputs, name = l.split(' -> ')
    i1, gate_type, i2 = inputs.split()
    gates[name] = [i1, i2, gate_type]

while len(gates) > 0:
    for out_wire in gates.keys():
        i1, i2, gate_type = gates[out_wire]
        if i1 in wires and i2 in wires:
            if gate_type == 'AND':
                wires[out_wire] = wires[i1] and wires[i2]
            elif gate_type == 'XOR':
                wires[out_wire] = not wires[i1] == wires[i2]
            else:
                wires[out_wire] = wires[i1] or wires[i2]
            del gates[out_wire]
            break

outputs = []
for wire in wires.keys():
    if wire[0] == 'z':
        if wires[wire]:
            bit = '1'
        else:
            bit = '0'
        outputs.append([wire, bit])
outputs.sort(reverse=True)
bits = [x[1] for x in outputs]
print(int(''.join(bits), 2))

# part 2
# Bit inputs are x and y wires. Then will need to look up a bitwise adder
#  and see where things go wrong. There are too many possible combos to do
#  by brute force

# look for least significant bit deltas
print('gate result =:')
for i in range(23):
    print(f'{45-i:^4}', end='')
print()
for c in bits[:23]:
    print(f'{c:^4}', end='')
print()
x_val = []
y_val = []
for wire in wires.keys():
    if wire[0] == 'x':
        if wires[wire]:
            bit = '1'
        else:
            bit = '0'
        x_val.append([wire, bit])
    if wire[0] == 'y':
        if wires[wire]:
            bit = '1'
        else:
            bit = '0'
        y_val.append([wire, bit])
x_val.sort(reverse=True)
x_bits = [x[1] for x in x_val]
y_val.sort(reverse=True)
y_bits = [x[1] for x in y_val]
print('Intended =:')
good_bits = [c for c in bin(int(''.join(x_bits), 2) + int(''.join(y_bits), 2))]
for c in good_bits[2:25]:
    print(f'{c:^4}', end='')
print()

# reset wires and gates and add a lookup for all inputs
wires = dict()
gates = dict()
by_input = defaultdict(list)
i = 0
for l in ls:
    if l == '':
        i += 1
        break
    name, val = l.split(': ')
    if val == '1':
        wires[name] = True
    else:
        wires[name] = False
    i += 1
for l in ls[i:]:
    inputs, name = l.split(' -> ')
    i1, gate_type, i2 = inputs.split()
    gates[name] = [i1, i2, gate_type]
    by_input[i1].append([name, i1, i2, gate_type])
    by_input[i2].append([name, i1, i2, gate_type])

# check step by step and stop when something doesn't match
input_and = input_xor = input_xor = carry_xor = carry_and = ''
carry_or = first_carry = last_carry_or = last_carry_xor = ''
for bit in range(45):
    b_str_x = 'x' + f'{bit:02d}'
    b_str_y = 'y' + f'{bit:02d}'
    # get first xor and input and gates
    for g_name, yin, xin, g_type in by_input[b_str_x]:
        if g_type == 'XOR':
            input_xor = g_name
        elif g_type == 'AND':
            input_and = g_name
            if bit == 0:
                first_carry = input_and
        else:
            print("Error: 1")
    # get the carry or gate
    if input_and != first_carry and len(by_input[input_and]) > 1:
        print("Error: input_and should only show in one place")
    for g_name, in1, in2, g_type in by_input[input_and]:
        last_carry_or = carry_or
        carry_or = g_name
        carry_or_in1 = in1
        carry_or_in2 = in2
        break
    if bit > 0:
        # get the carry xor/and gates
        last_carry_xor = carry_xor
        last_carry_and = carry_and
        for g_name, in1, in2, g_type in by_input[input_xor]:
            if g_type == 'XOR':
                carry_xor = g_name
                carry_xor_in1 = in1
                carry_xor_in2 = in2
            elif g_type == 'AND':
                carry_and = g_name
                carry_and_in1 = in1
                carry_and_in2 = in2
            else:
                print("Error: 2")
    else:
        last_carry_xor = last_carry_and = input_xor
        carry_xor_in1 = carry_xor_in2 = carry_and_in1 =carry_and_in2 = ''
    # do some checks
    if wires[b_str_x]:
        x = 1
    else:
        x = 0
    if wires[b_str_y]:
        y = 1
    else:
        y = 0
    print(f'{bit=} {x=} {y=} z= {carry_xor=}')
    print(f'{input_xor=} = {carry_xor_in1=} {carry_and_in1=}')
    print(f'{last_carry_or=} = {carry_xor_in2=} {carry_and_in2=}')
    print(f'{carry_or_in2=} = {input_and=}')
    print(f'{carry_or_in1=} = {carry_and=}')
    print(f' {last_carry_xor=}')
    print('-'*30)

# had to swap these
swaps = ['sgj', 'z35', 'kpp', 'z31', 'kdh', 'hjf', 'vss', 'z14']
print(','.join(sorted(swaps)))
