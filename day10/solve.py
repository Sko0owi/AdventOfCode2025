from tqdm import tqdm
from copy import copy
import numpy as np
import queue  

from pulp import LpProblem, LpVariable, LpMinimize, LpInteger, lpSum, LpStatusOptimal


def use_edge(edge, current_state):
    new_state = copy(current_state)
    for edge_id in edge:
        if edge_id.isnumeric():
            new_state[int(edge_id)] = 1 if new_state[int(edge_id)] == 0 else 0
    return new_state 
    
def star1(inputData, DEBUG=False):

    result = 0
    for row in tqdm(inputData):
        goal=row[0].replace("[","").replace("]","")
        _ = list(map(int,row[len(row) - 1].replace("{","").replace("}","").split(",")))

        edges = row[1 : len(row)-1]

        goal_state = np.zeros(len(goal))
        for i, goal_bit in enumerate(goal):
            if goal_bit == ".":
                goal_state[i] = 0
            else:
                goal_state[i] = 1


        edges_parsed = []
        for edge in edges:
            edge = list(map(int,edge.replace("(","").replace(")","").split(",")))
            edges_parsed.append(edge)


        start_state = np.zeros(len(goal))
        visited_states = [list(start_state)]
        q = queue.Queue()  
        q.put((0,start_state))
        while not q.empty():

            depth, current_state = q.get()

            if (current_state == goal_state).all():
                result += depth
                break

            for edge in edges:
                new_state = use_edge(edge, current_state)
                if list(new_state) not in visited_states:
                    q.put((depth+1, new_state))
                    visited_states.append(list(new_state))

    return result


def star2(inputData, DEBUG=False):
    result = 0
    for row in tqdm(inputData):
        _ =row[0].replace("[","").replace("]","")
        voltage = list(map(int,row[len(row) - 1].replace("{","").replace("}","").split(",")))

        edges = row[1 : len(row)-1]
        voltage_state = np.zeros(len(voltage))
        for i, voltage_bit in enumerate(voltage):
            
            voltage_state[i] = int(voltage_bit)

        print(voltage_state)


        edges_parsed = []
        for edge in edges:
            edge = list(map(int,edge.replace("(","").replace(")","").split(",")))
            edges_parsed.append(edge)
        print(edges_parsed)
        
        prob = LpProblem("joltage", LpMinimize)

        x = [LpVariable(f"x_{j}", lowBound=0, cat=LpInteger) for j in range(len(edges_parsed))]

        prob += lpSum(x)

        for i in range(len(voltage)):
            prob += lpSum(x[j] for j, btn in enumerate(edges_parsed) if i in btn) == voltage_state[i]

        status = prob.solve()
        if status != 1:  # LpStatusOptimal
            raise RuntimeError("brak optymalnego rozwiązania")

        presses = [int(v.value()) for v in x]
        result += sum(presses)

    return result


if __name__ == '__main__':

    inputData_example_1, inputData_example_2 = [], []
    inputData_star_1, inputData_star_2 = [], []

    with open("input_example_1.txt") as f:
        inputData_example_1 = f.readlines()
        inputData_example_1 = [line.split() for line in inputData_example_1]
    # print(inputData_example_1)

    with open("input_star_1.txt") as f:
        inputData_star_1 = f.readlines()
        inputData_star_1 = [line.split() for line in inputData_star_1]
    # print(inputData_star_1)

    result_example_1 = star1(inputData_example_1)

    print(f"For example 1 score is: {result_example_1}")

    assert result_example_1 == 7

    result_star_1 = star1(inputData_star_1)
    print(f"For star 1 score is: {result_star_1}")

    with open("input_example_1.txt") as f:
        inputData_example_2 = f.readlines()
        inputData_example_2 = [line.split() for line in inputData_example_2]

    with open("input_star_1.txt") as f:
        inputData_star_2 = f.readlines()
        inputData_star_2 = [line.split() for line in inputData_star_2]

    result_example_2 = star2(inputData_example_2)

    print(f"For example 2 score is: {result_example_2}")

    assert result_example_2 == 33

    result_star_2 = star2(inputData_star_2)
    print(f"For star 2 score is: {result_star_2}")   

