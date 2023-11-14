from APTA import APTA
from DISJOINTSETS import DisjointSet
from FSM import FSM
from matrix_reader import read_matrix, draw


G = read_matrix('test.adjlist')
# draw(G, "output/APTA.png")
apta = APTA()
apta.root = 262
apta.G = G
# apta.G.add_node('404')
apta.draw_multiDigraph()
# set colcor
# red_states = [262]
# for s in red_states:
#     apta.set_color(s, 'red')
# apta.set_color(7, 'white')
fsm = FSM(apta)
# fsm.red_states = red_states
# fsm.draw()
# fsm.run_EDSM_learner()
ds = DisjointSet()

# make sets
fsm.make_set_for_every_state_rooted_at(ds, 262)
fsm.make_set_for_every_state_rooted_at(ds, 377)
fsm.make_set_for_every_state_rooted_at(ds, 568)
# fsm.make_set_for_every_state_rooted_at(ds, 404)
# union sets
ds.union(262, 377)
ds.union(262, 568)
ds.print()
fsm.compute_classes2(ds, {262:[262,377,568]})
ds.print()
# print(f' set of 1: {ds.get_set(1)}')
# #
# # fsm.compute_classes(ds, 1,6)
# # ds.print()
# # print(f' set of 1: {ds.get_set(1)}')