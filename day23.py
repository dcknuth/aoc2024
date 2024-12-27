# Day 23 part 1
import networkx as nx
from itertools import combinations

filename = "test23.txt"
filename = "input23.txt"

with open(filename) as f:
    ls = f.read().strip().split("\n")

g = nx.Graph()
for l in ls:
    n1, n2 = l.split('-')
    g.add_edge(n1, n2)

#tri_counts = nx.triangles(g)
#print(sum(tri_counts.values()) // 3)

groups = set()
with_t = set()
for clique in nx.find_cliques(g):
    if len(clique) == 3:
        groups.add(tuple(sorted(clique)))
        for n in clique:
            if n[0] == 't':
                with_t.add(tuple(sorted(clique)))
                break
    if len(clique) > 3:
        for g3 in combinations(clique, 3):
            groups.add(tuple(sorted(list(g3))))
            for n in g3:
                if n[0] == 't':
                    with_t.add(tuple(sorted(list(g3))))
                    break
print(len(with_t))

# part 2
# since we are already using cliques, we can just find the largest
password = ''
largest = 0
for clique in nx.find_cliques(g):
    if len(clique) > largest:
        largest = len(clique)
        password = ','.join(sorted(clique))
print(password)
