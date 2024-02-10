from APTA import APTA
from DISJOINTSETS import DisjointSet
from FSM import FSM
from matrix_reader import read_matrix, draw
import unittest

class TestCompute_scour(unittest.TestCase):
    # def test_compute_score(self):
    #     # data
    #     G = read_matrix('computeclasses.adjlist')
    #     apta = APTA()
    #     apta.G = G
    #     apta.root = 1
    #     fsm = FSM(apta)
    #
    #     ds = DisjointSet()
    #     # make sets
    #     for state in G.nodes:
    #         ds.make_set(state)
    #
    #     # union sets
    #     fsm.compute_classes(ds, 1,5)
    #     fsm.compute_classes(ds, 1,6)
    #     # fsm.ds.printSets()
    #     result = fsm.compute_scour(ds)
    #     self.assertEqual(result, 4)

    def test_compute_score2(self):
        # data
        G = read_matrix('computeclasses.adjlist')
        apta = APTA()
        apta.G = G
        apta.root = 1
        fsm = FSM(apta)

        ds = DisjointSet()
        # make sets
        for state in G.nodes:
            ds.make_set(state)

        # union sets
        ds.union(1,5)
        # fsm.compute_classes2(ds, {1:[1,5]})
        ds.union(1,6)
        # fsm.compute_classes2(ds, {1:[1, 5, 6]})
        ds.union(2,7)
        ds.union(4,8)
        ds.union(3,10)
        ds.print()
        result = fsm.compute_scour(ds)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()
#
# G = read_matrix('computeclasses.adjlist')
# # draw(G, "APTA.png")
# apta = APTA()
# apta.G = G
# # apta.G.nodes[5]['fillcolor'] = 'lightblue'
#
#
# apta.set_state_type(1, 'accepted')
# # apta.G.nodes[1]['fillcolor'] = '#FA7E7E'
# apta.set_state_type(5, 'rejected')
# apta.set_state_type(6, 'unlabeled')
# apta.draw_multiDigraph()
# fsm = FSM(apta)
# # fsm.draw()
# # make sets
# fsm.make_set_for_every_state_rooted_at(1)
# fsm.make_set_for_every_state_rooted_at(5)
# fsm.make_set_for_every_state_rooted_at(6)
# # union sets
# fsm.compute_classes(1,5)
# fsm.compute_classes(1,6)
# fsm.ds.printSets()
#
# print(f'merging scour for state 1, 5 and 6: {fsm.compute_scour()}')