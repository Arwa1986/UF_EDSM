from APTA import APTA
from DISJOINTSETS import DisjointSet
from FSM import FSM
from matrix_reader import read_matrix, draw


G = read_matrix('computeclasses.adjlist')
draw(G, "output/APTA.png")
apta = APTA()
apta.root = 1
apta.G = G
# set colcor
red_states = [1,6,3,8]
for s in red_states:
    apta.set_color(s, 'red')
apta.set_color(7, 'white')
fsm = FSM(apta)
fsm.red_states = red_states
fsm.draw()
fsm.run_EDSM_learner()
# ds = DisjointSet()
#
# # make sets
# fsm.make_set_for_every_state_rooted_at(ds, 1)
# fsm.make_set_for_every_state_rooted_at(ds, 5)
# fsm.make_set_for_every_state_rooted_at(ds, 6)
# # # union sets
# # fsm.compute_classes(ds, 1,5)
# # ds.print()
# # print(f' set of 1: {ds.get_set(1)}')
# #
# # fsm.compute_classes(ds, 1,6)
# # ds.print()
# # print(f' set of 1: {ds.get_set(1)}')