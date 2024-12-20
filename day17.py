# Day 17 part 1

filename = 'test17.txt'
filename = 'test17-2.txt'
filename = 'test17-3.txt'
filename = 'test17-4.txt'
filename = 'test17-5.txt'
filename = 'test17-6.txt'
filename = 'input17.txt'
RN = {4:'A', 5:'B', 6:'C'}
RL = ['A', 'B', 'C']
R = {'A':0, 'B':0, 'C':0}
P = []
OUT = []
IP = 0

with open(filename) as f:
    ls = f.read().strip().split('\n')

for i, l in enumerate(ls[0:3]):
    _, name, n = l.split()
    R[RL[i]] = int(n)
_, p = ls[4].split()
P = list(map(int, p.split(',')))

def adv(x):
    if x < 4:
        R['A'] = R['A']//(2**x)
    else:
        R['A'] = R['A']//(2**R[RN[x]])

def bxl(x):
    R['B'] = R['B'] ^ x

def bst(x):
    if x < 4:
        R['B'] = x
    else:
        R['B'] = R[RN[x]] % 8

def jnz(x):
    global IP
    if R['A'] != 0:
        IP = x
    else:
        IP += 2

def bxc(x):
    R['B'] = R['B'] ^ R['C']

def out(x):
    if x < 4:
        OUT.append(x)
    else:
        OUT.append(R[RN[x]] % 8)

def bdv(x):
    if x < 4:
        R['B'] = R['A']//(2**x)
    else:
        R['B'] = R['A']//(2**R[RN[x]])

def cdv(x):
    if x < 4:
        R['C'] = R['A']//(2**x)
    else:
        R['C'] = R['A']//(2**R[RN[x]])

OPC = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

while IP > -1 and IP < len(P):
    x = -1
    i = P[IP]
    if IP < len(P)-1:
        x = P[IP+1]
    if i == 3:
        OPC[i](x)
    else:
        OPC[i](x)
        IP += 2

print(','.join(map(str, OUT)))

# part 2
R = {'A':0, 'B':0, 'C':0}
P = []
OUT = []
IP = 0

with open(filename) as f:
    ls = f.read().strip().split('\n')

for i, l in enumerate(ls[0:3]):
    _, name, n = l.split()
    R[RL[i]] = int(n)
_, p = ls[4].split()
P = list(map(int, p.split(',')))

r_orig = R.copy()
a_in = 8**15
a_in_step = 12
a_step = 8**a_in_step
p_match = -1
found = False
while not found:
    R = r_orig.copy()
    R['A'] = a_in
    IP = 0
    OUT = []
    while IP > -1 and IP < len(P):
        x = -1
        i = P[IP]
        if IP < len(P)-1:
            x = P[IP+1]
        if i == 3:
            OPC[i](x)
        else:
            OPC[i](x)
            IP += 2
    if OUT == P:
        found = True
    else:
        if a_step != 1:
            # look for the next match for the most significant position
            if OUT[p_match:] == P[p_match:]:
                a_in -= a_step*2
                a_in_step -= 1
                a_step = 8**a_in_step
                print(f'{a_in=} {a_in_step=} {a_step=} {p_match=}')
                print(','.join(map(str, OUT)))
                print(','.join(map(str, P)))
                p_match -= 1
        a_in += a_step

print(a_in)
