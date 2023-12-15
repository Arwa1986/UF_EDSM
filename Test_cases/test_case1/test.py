from APTA import APTA
from FSM import FSM
from matrix_reader import read_matrix, draw


G = read_matrix('test/computeclasses.adjlist')
draw(G, "expected_graph/APTA.png")
apta = APTA()
apta.G = G
fsm = FSM(apta)
# fsm.draw()
fsm.make_set_for_every_state_rooted_at(1)
fsm.make_set_for_every_state_rooted_at(5)
fsm.compute_classes(1,5)
fsm.ds.printSets()
fsm.merge_sets()
fsm.draw()
fsm.make_set_for_every_state_rooted_at(6)
fsm.compute_classes(1,6)
fsm.ds.printSets()
fsm.merge_sets()
fsm.draw()

