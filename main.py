import random
from APTA import APTA
from FSM import FSM
from evaluation import Evaluation
from input_reader import import_input, clean_folder, build_adjs_matrix, prepare_data, GetTrainingEvaluationData
import csv
import os, shutil



def start_learning(traningPosExmp, trainingNegExmp):
    apta = APTA()
    apta.build_APTA(traningPosExmp, trainingNegExmp)
    fsm = FSM(apta)
    fsm.run_EDSM_learner()

    return fsm
if __name__ == '__main__':

    clean_folder()
    input_folder = 'input'
    counter = 24
    # inputfile = "input/PosNegExamples.txt"

    for file_name in os.listdir(input_folder):
        input_file_path = os.path.join(input_folder, file_name)
        traningPosExmp, trainingNegExmp, evalPosExmp, evalNegExamp = GetTrainingEvaluationData(input_file_path)


        fsm = start_learning(traningPosExmp, trainingNegExmp)
        # fsm.draw2(f'automata{counter}')

        eval = Evaluation(fsm, evalPosExmp, evalNegExamp)
        true_positive, true_negative, false_positive, false_negative, precision, recall, F_measure, Accuracy = eval.evaluate()
        # print(f'the root: {fsm.apta.root}')

        data = [
            [len(traningPosExmp), len(trainingNegExmp), len(evalPosExmp), len(evalNegExamp), true_positive, true_negative,
             false_positive, false_negative, precision, recall, F_measure, Accuracy]]
        file_path = 'data.csv'
        # Write data to CSV file
        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f'Automata{counter}')
        counter+=1
