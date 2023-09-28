from APTA import APTA
from FSM import FSM
from matrix_reader import read_matrix, draw
import networkx as nx

from DISJOINTSETS import DisjointSet
G = read_matrix('computeclasses.adjlist')
draw(G, "output/APTA.png")
apta = APTA()
apta.G = G
apta.root = 1
fsm = FSM(apta)
# fsm.draw()
states=[1,6,3,7,8]
ds =DisjointSet()
ds.s1 = 6
ds.s2 = 7
for s in states:
    fsm.make_set_for_every_state_rooted_at(ds, s)
ds.print()
# fsm.make_set_for_every_state_rooted_at(5)
fsm.compute_classes(ds, 6 ,7)
print(f'scour={fsm.compute_scour(ds)}')
ds.print()
fsm.merge_sets(ds)
fsm.draw()
# fsm.make_set_for_every_state_rooted_at(6)
# fsm.compute_classes(1,6)
# fsm.ds.print()
# fsm.merge_sets()
# fsm.draw()

