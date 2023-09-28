
import networkx as nx

# from utility import *
from main import *

#
# def is_merged(G, lre):
#     merged = False
#     merge_list = []
#     for e in lre:
#         if e[1] in G:
#             merge_list.append(e[1])
#
#     if len(merge_list) <= 1:
#         merged = True
#
#     return merged, merge_list


def read_matrix(fname):
    print('start')
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
        print(frm, to, lbl)

    f.close()

    print('done')
    return G



def draw(G, filename):
    p = nx.drawing.nx_pydot.to_pydot(G)
    p.write_png(filename)


if __name__ == '__main__':
    clean_folder()

    #test_solve determinism
    G = read_matrix('test/computeclasses.adjlist')
    draw(G, "Test_cases/test_case1/expected_graph/APTA.png")
