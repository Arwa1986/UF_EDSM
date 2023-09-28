from APTA import APTA
from FSM import FSM
from input_reader import import_input, clean_folder

if __name__ == '__main__':
    clean_folder()
    k, accepted_traces, rejected_traces, BL, SP = import_input("test/input.txt")
    # building the tree
    apta = APTA()
    apta.build_APTA(accepted_traces, rejected_traces)
    apta.draw_multiDigraph()

    fsm = FSM(apta)
    # fsm.run_EDSM_learner(apta.root)
    fsm.draw()
    # fsm.compute_classes(1,5)
    fsm.run_EDSM_learner()
    # fsm.apta.delete_rejected_leaf_nodes()
    fsm.draw()
    


