from matrix_reader import *


def are_graphs_equal(fsm1, fsm2):
    # Check if the number of nodes is the same
    if len(set(fsm1.apta.G.nodes)) != len(set(fsm2.apta.G.nodes)):
        return False

    # get the edge sets of both graphs
    edges1 = fsm1.apta.G.edges
    edges2 = fsm2.apta.G.edges

    # Check if the number of edges is the same
    if len(edges1) != len(edges2):
        return False

    s1 = fsm1.apta.root
    s2 = fsm2.apta.root

    # list to keep track of all visited nodes of the first graph
    fsm1_visited = []
    # if not all states in fsm2 are visited:
    s1_outEdges = fsm1.apta.get_out_edges_asDictionary(s1)
    s2_outEdges = fsm2.apta.get_out_edges_asDictionary(s2)
    # check the Acceptance condition of the pair
    if fsm1.apta.G.nodes[s1]['type'] != fsm1.apta.G.nodes[s2]['type']:
        return False
    # Check if the number of edges and labels (of the current state) are the same
    if s2_outEdges.keys() != s2_outEdges.keys():
        return False
    else:
        fsm1_currentState_selfloop = []
        fsm1_currentState_sameTargetState=[]
        for key in s1_outEdges:
            # if the state in the first graph has a selfloop
            # but the second hasn't for the same label
            # then exit with false

            if s1_outEdges[key] == s1:
                fsm1_currentState_selfloop.append(key)
            fsm1_currentState_sameTargetState = find_keys_by_value(s1_outEdges, key)



        for label in fsm1_currentState_selfloop:
           if s2_outEdges[key] != s2:
               return False

    return True

def find_keys_by_value(input_dict, input_key):
    """
    Find keys in a dictionary that have the same value as the given key.

    Parameters:
    - input_dict (dict): The input dictionary.
    - input_key (hashable): The key to compare values against.

    Returns:
    - List: A list of keys with the same value as the given key.
    """
    # TO DO: try disjoint sets
    return [key for key, value in input_dict.items() if value == input_dict[input_key] and key!= input_key]



if __name__ == "__main__":
    # G1 = read_matrix('matrix1.adjlist')
    # draw(G1, "matrix1.png")
    # apta1 = APTA()
    # apta1.G = G1
    # fsm1 = FSM(apta1)

    # G2 = read_matrix('matrix2.adjlist')
    # draw(G2, "matrix2.png")
    # apta2 = APTA()
    # apta2.G = G2
    # fsm2 = FSM(apta2)
    # print(f'Are Graphs equals?{are_graphs_equal(fsm1, fsm2)}')

    # --- get out edges as Dictionary ---
    # test case 1
    # nodes = fsm1.apta.G.nodes
    # for s in nodes:
    #     print(f'{s}={fsm1.apta.get_out_edges_asDictionary(s)}')


    # test case 1
    # output should be True
    # dict1 = {'a':'S0', 'b':'S4'}
    # dict2 = {'b':'S3', 'a':'S5'}
    #
    # if dict1.keys() == dict2.keys():
    #     print('True')
    # else:
    #     print('False')

    # test case 2
    # output should be False
    # dict1 = {'a': 'S0', 'b': 'S4'}
    # dict2 = {'b': 'S3', 'a': 'S5', 'c':'S0'}
    #
    # if dict1.keys() == dict2.keys():
    #     print('True')
    # else:
    #     print('False')

    # Example usage
    my_dict = {
        'a': 1,
        'b': 2,
        'c': 1,
        'd': 3,
    }

    result = find_keys_by_value(my_dict, 'a')
    print(f"Keys with the same value as 'a': {result}")