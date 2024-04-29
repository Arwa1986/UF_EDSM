
import networkx as nx

# from utility import *
from main import *

def read_matrix(fname):
    # print('start')
    G = nx.MultiDiGraph()
    f = open(fname)

    for line in f.readlines():
        color = ''
        shape = 'oval'
        x = line.split()
        frm, to, lbl = eval(x[0]), eval(x[1]), x[2]
        if len(x)==4:
            if    x[3] == 'rejected':
                color = '#FA7E7E'
                ntype = 'rejected'
                shape = 'square'
            elif  x[3] == 'accepted':
                color = 'lightblue'
                ntype = 'accepted'
                shape = 'doublecircle'
            else:
                color = 'white'
                ntype = 'unlabeled'
                shape = 'oval'

        ntype = 'unlabeled' if len(x)==3 else x[3]
        G.add_node(frm, label=frm)
        # G.add_node(to, label=to)
        G.add_node(to, label=to, type=ntype, style='filled', fillcolor=color, shape=shape)
        G.add_edge(frm, to, label=lbl, weight='1')
        # print(frm, to, lbl)

    f.close()

    # print('done')
    return G


def graph_to_string(graph):
    # create file named "matrixOfRefrencedAuotmata.adjlist"
    # W: will overwirte any previous contents
    f = open("input/LearnedAuotmata_string.txt", "w")

    for state in graph.nodes:
        out_edges = graph.out_edges(state, keys=True)
        for edge in out_edges:
            lbl = graph.get_edge_data(edge[0], edge[1], edge[2])["label"]
            row = f'{edge[0]}-{lbl}->{edge[1]}\n'
            f.write(row)

    f.close()

def draw(G, filename):
    p = nx.drawing.nx_pydot.to_pydot(G)
    p.write_png(filename)


if __name__ == '__main__':
    # clean_folder()
    #
    # #test_solve determinism
    # G = read_matrix('test/computeclasses.adjlist')
    # draw(G, "Test_cases/test_case1/expected_graph/APTA.png")

    graph = nx.MultiDiGraph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_edge(1, 2, label='a')
    graph.add_edge(1, 3, label='b')
    graph.add_edge(3, 2, label='a')
    graph.add_edge(2, 4, label='a')
    graph.add_edge(4, 1, label='b')
    graph.add_edge(3, 4, label='b')
    graph.add_edge(2, 1, label='b')

    # draw(graph, "input/graph1.png")
    graph_to_string(graph)