import unittest

from Test_cases.compare_graphs.comapre_graphs import Graph_comparision
from matrix_reader import *


class TestGraphsEquality(unittest.TestCase):
    def test_unlabeled_become_accepted(self):
        G1 = read_matrix('G1.adjlist')
        apta1 = APTA()
        apta1.G = G1
        apta1.root = 0
        apta1.set_state_type(0,"accepted")
        fsm1 = FSM(apta1)
        # draw(G1, "refrence.png")

        accepted_traces, rejected_traces = import_input("input/PosNegExamples.txt")
        # building the tree
        apta2 = APTA()
        apta2.build_APTA(accepted_traces, rejected_traces)
        # apta2.draw_multiDigraph()
        # draw(apta2.G, "G.png")
        fsm2 = FSM(apta2)

        GC = Graph_comparision()
        result = GC.are_graphs_equal(fsm1, fsm2)
        self.assertTrue(result)




if __name__ == "__main__":
    unittest.main()
    # G1 = read_matrix('G1.adjlist')
    # # draw(G1, "G1.png")
    # apta1 = APTA()
    # apta1.G = G1
    # apta1.root = 0
    # fsm1 = FSM(apta1)
    #
    # G2 = read_matrix('G2.adjlist')
    # # draw(G2, "G2.png")
    # apta2 = APTA()
    # apta2.G = G2
    # apta2.root = 0
    # fsm2 = FSM(apta2)
    # GC = Graph_comparision()
    # result = GC.are_graphs_equal(fsm1, fsm2)
    # print(result)