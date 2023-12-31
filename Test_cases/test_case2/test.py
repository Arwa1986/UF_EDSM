from APTA import APTA
from FSM import FSM
from matrix_reader import read_matrix, draw


G = read_matrix('test/computeclasses.adjlist')
draw(G, "expected output/APTA.png")
apta = APTA()
apta.G = G
# apta.G.nodes[5]['fillcolor'] = 'lightblue'


apta.set_state_type(1, 'accepted')
# apta.G.nodes[1]['fillcolor'] = '#FA7E7E'
apta.set_state_type(5, 'rejected')
apta.set_state_type(6, 'unlabeled')

fsm = FSM(apta)

# make sets
fsm.make_set_for_every_state_rooted_at(1)
fsm.make_set_for_every_state_rooted_at(5)
fsm.make_set_for_every_state_rooted_at(6)
# union sets
fsm.compute_classes(1,5)
fsm.compute_classes(1,6)
fsm.ds.printSets()

for s in fsm.apta.G.nodes:
    print(f'{s}: {apta.get_state_type(s)}')

# check comaptibility of each set
all_sets = fsm.ds.get_sets()
for representative, _set in all_sets.items():
    print(f"Set with representative {representative}: {_set}")
    compatible, list_type = fsm.is_compatible_type(_set)
    print(f'compatible? = {compatible}, list type= {list_type}')