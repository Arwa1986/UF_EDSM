import random
from APTA import APTA
from FSM import FSM
from evaluation import Evaluation
from input_reader import import_input, clean_folder

def split_dataset(accepted_traces, rejected_traces):
    testing_PosSize = round(len(accepted_traces) * 0.3)
    training_PosSize = len(accepted_traces) - testing_PosSize

    train_positive_traces = random.sample(accepted_traces, training_PosSize)

    # test_positive_traces = random.choices(accepted_traces, k=testing_PosSize)
    test_positive_traces = []
    for trace in accepted_traces:
        if trace not in train_positive_traces:
            test_positive_traces.append(trace)

    testing_NegSize = round(len(rejected_traces) * 0.3)
    training_NegSize = len(rejected_traces) - testing_NegSize
    train_negative_traces = random.sample(rejected_traces, training_NegSize)
    # test_negative_traces = random.choices(rejected_traces, k=testing_NegSize)
    test_negative_traces = [trace for trace in rejected_traces if trace not in train_negative_traces]

    return train_positive_traces, train_negative_traces, test_positive_traces, test_negative_traces

def write_to_file(traningPosExmp, trainingNegExmp, evalPosExmp, evalNegExamp):
    f = open("input/traces.txt", "w")
    f.write(f"training positive:\n")
    for examp in traningPosExmp:
        f.write(f'{examp}\n')

    f.write(f"training negative:\n")
    for examp in trainingNegExmp:
        f.write(f'{examp}\n')

    f.write(f"evaluation positive:\n")
    for examp in evalPosExmp:
        f.write(f'{examp}\n')

    f.write(f"evaluation negative:\n")
    for examp in evalNegExamp:
        f.write(f'{examp}\n')


    f.close()

if __name__ == '__main__':
    clean_folder()
    k, accepted_traces, rejected_traces, BL, SP = import_input("input/PosNegExamples.txt")
    traningPosExmp, trainingNegExmp, evalPosExmp, evalNegExamp = split_dataset(accepted_traces, rejected_traces)
    # # traningPosExmp, trainingNegExmp, evalPosExmp, evalNegExamp  = import_input("input/traces.txt")
    #
    write_to_file(traningPosExmp, trainingNegExmp, evalPosExmp, evalNegExamp)
    print(f'..........Training.............')
    print(f'number of Positive Examples: {len(traningPosExmp)}')
    print(f'number of Negative Examples: {len(trainingNegExmp)}')
    # building the tree
    apta = APTA()
    apta.build_APTA(traningPosExmp, trainingNegExmp)
    # apta.build_APTA(accepted_traces, rejected_traces)
    fsm = FSM(apta)
    fsm.draw()
    fsm.run_EDSM_learner()

    print(f'...............EVALUATION................')
    print(f'..................EDSM...................')
    print(f'number of Positive Examples: {len(evalPosExmp)}')
    print(f'number of Negative Examples: {len(evalNegExamp)}')
    eval = Evaluation(fsm, evalPosExmp, evalNegExamp)
    precision = eval.evaluate()
    print(f'the root: {fsm.apta.root}')


