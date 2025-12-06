from tqdm import tqdm
from copy import copy
import numpy as np

    
def star1(inputData, DEBUG=False):
    operations = []
    
    numbers = np.zeros((len(inputData)-1, len(inputData[0])), dtype=int)

    for i, line in enumerate(inputData[:len(inputData)-1]):
        for j, number in enumerate(line):

            numbers[i][j] = int(number)
    
    for i, line in enumerate(inputData[len(inputData)-1:]):
        for j, op in enumerate(line):
            operations.append(op)
    if DEBUG: print(numbers)
    if DEBUG: print(operations)

    sum_problems = 0
    for i in range(len(inputData[0])):
        addition = False
        if operations[i] == '+':
            addition = True
        elif operations[i] == '*':
            addition = False
        else:
            raise AssertionError("something went wrong")
        
        sub_problem = numbers[0][i]
        for j in range(1, len(inputData)-1):
            if addition:
                sub_problem = sub_problem + numbers[j][i]
            else:
                sub_problem = sub_problem * numbers[j][i]

        sum_problems += sub_problem

    return sum_problems

def star2(inputData, DEBUG=False):
    
    operations = []
    numbers = []

    current_numbers = []
    for j in range(len(inputData[0])):
        numberStr = ""
        for i in range(len(inputData) - 1):
            numberStr += inputData[i][j]
        numberStr = numberStr.strip()
        if numberStr != "":
            current_numbers.append(int(numberStr))
        else:
            numbers.append(copy(current_numbers))
            current_numbers.clear()

    numbers.append(copy(current_numbers))

    for i, line in enumerate(inputData[len(inputData)-1:]):
        for j, op in enumerate(line):
            if op != " ":
                operations.append(op)

    sum_problems = 0
    for i in range(len(numbers)):
        addition = False
        if operations[i] == '+':
            addition = True
        elif operations[i] == '*':
            addition = False
        else:
            raise AssertionError("something went wrong")
        
        sub_problem = int(numbers[i][0])
        for j in range(1, len(numbers[i])):
            if addition:
                sub_problem = sub_problem + int(numbers[i][j])
            else:
                sub_problem = sub_problem * int(numbers[i][j])
        sum_problems += sub_problem

    return sum_problems



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

    assert result_example_1 == 4277556

    result_star_1 = star1(inputData_star_1)
    print(f"For star 1 score is: {result_star_1}")

    with open("input_example_1.txt") as f:
        inputData_example_2 = f.readlines()
        inputData_example_2 = [line.strip("\n") for line in inputData_example_2]

    with open("input_star_1.txt") as f:
        inputData_star_2 = f.readlines()
        inputData_star_2 = [line.strip("\n") for line in inputData_star_2]

    result_example_2 = star2(inputData_example_2)

    print(f"For example 2 score is: {result_example_2}")

    assert result_example_2 == 3263827

    result_star_2 = star2(inputData_star_2)
    print(f"For star 2 score is: {result_star_2}")   

