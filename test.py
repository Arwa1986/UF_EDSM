from APTA import APTA
from DISJOINTSETS import DisjointSet
from FSM import FSM
from matrix_reader import read_matrix, draw


G = read_matrix('test/computeclasses.adjlist')
draw(G, "output/APTA.png")
apta = APTA()
apta.G = G
# apta.G.nodes[5]['fillcolor'] = 'lightblue'


apta.set_state_type(1, 'accepted')
# apta.G.nodes[1]['fillcolor'] = '#FA7E7E'
apta.set_state_type(5, 'rejected')
apta.set_state_type(6, 'unlabeled')

fsm = FSM(apta)
ds = DisjointSet()

# make sets
fsm.make_set_for_every_state_rooted_at(ds, 1)
fsm.make_set_for_every_state_rooted_at(ds, 5)
fsm.make_set_for_every_state_rooted_at(ds, 6)
# # union sets
# fsm.compute_classes(ds, 1,5)
# ds.print()
# print(f' set of 1: {ds.get_set(1)}')
#
# fsm.compute_classes(ds, 1,6)
# ds.print()
# print(f' set of 1: {ds.get_set(1)}')
ds.union(1, 5)
work_to_do={}
work_to_do[ds.find(1)] = ds.get_set(1)
print(f'work to do: {work_to_do}')
ds.union(1, 6)
work_to_do[ds.find(1)] = ds.get_set(1)
print(f'work to do: {work_to_do}')