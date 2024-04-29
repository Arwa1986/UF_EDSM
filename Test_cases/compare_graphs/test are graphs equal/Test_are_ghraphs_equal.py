import unittest

from Test_cases.compare_graphs.comapre_graphs import Graph_comparision
from matrix_reader import *


class TestGraphsEquality(unittest.TestCase):
    def test_graph_with_self_loop(self):
        G1 = read_matrix('G1.adjlist')
        # draw(G1, "G1.png")
        apta1 = APTA()
        apta1.G = G1
        apta1.root = 0
        fsm1 = FSM(apta1)

        G2 = read_matrix('G2.adjlist')
        # draw(G2, "G2.png")
        apta2 = APTA()
        apta2.G = G2
        apta2.root = 0
        fsm2 = FSM(apta2)

        GC = Graph_comparision()
        result = GC.are_graphs_equal(fsm1, fsm2)
        self.assertTrue(result)

    def test_graph_with_different_acceptance_conditions(self):
        G1 = read_matrix('G1.adjlist')
        draw(G1, "G1.png")
        apta1 = APTA()
        apta1.G = G1
        apta1.root = 0
        fsm1 = FSM(apta1)

        G2 = read_matrix('G22.adjlist')
        draw(G2, "G22.png")
        apta2 = APTA()
        apta2.G = G2
        apta2.root = 0
        fsm2 = FSM(apta2)

    def test_graph_with_different_target_states(self):
        G1 = read_matrix('G1.adjlist')
        draw(G1, "G1.png")
        apta1 = APTA()
        apta1.G = G1
        apta1.root = 0
        fsm1 = FSM(apta1)

        G2 = read_matrix('G222.adjlist')
        draw(G2, "G222.png")
        apta2 = APTA()
        apta2.G = G2
        apta2.root = 0
        fsm2 = FSM(apta2)

        GC = Graph_comparision()
        result = GC.are_graphs_equal(fsm1, fsm2)
        self.assertFalse(result)

    def test_graph_with_different_numOf_transitions(self):
        G1 = read_matrix('G11.adjlist')
        draw(G1, "G11.png")
        apta1 = APTA()
        apta1.G = G1
        apta1.root = 0
        fsm1 = FSM(apta1)

        G2 = read_matrix('G22222.adjlist')
        draw(G2, "G22222.png")
        apta2 = APTA()
        apta2.G = G2
        apta2.root = 0
        fsm2 = FSM(apta2)

        GC = Graph_comparision()
        result = GC.are_graphs_equal(fsm1, fsm2)
        self.assertFalse(result)

    def test_graph_with_different_numOf_states(self):
        G1 = read_matrix('G1.adjlist')
        draw(G1, "G1.png")
        apta1 = APTA()
        apta1.G = G1
        apta1.root = 0
        fsm1 = FSM(apta1)

        G2 = read_matrix('G2222.adjlist')
        draw(G2, "G2222.png")
        apta2 = APTA()
        apta2.G = G2
        apta2.root = 0
        fsm2 = FSM(apta2)

        GC = Graph_comparision()
        result = GC.are_graphs_equal(fsm1, fsm2)
        self.assertFalse(result)

    def test_graph_with_no_leaves(self):
        G1 = read_matrix('G111.adjlist')
        draw(G1, "G111.png")
        apta1 = APTA()
        apta1.G = G1
        apta1.root = 0
        fsm1 = FSM(apta1)

        G2 = read_matrix('G222222.adjlist')
        draw(G2, "G222222.png")
        apta2 = APTA()
        apta2.G = G2
        apta2.root = 0
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