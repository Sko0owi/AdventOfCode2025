from tqdm import tqdm
from copy import copy
import numpy as np

    
def star1(inputData, DEBUG=False):
    return 0

def star2(inputData, DEBUG=False):
    return 0

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

    assert result_example_1 == 0

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

    assert result_example_2 == 0

    result_star_2 = star2(inputData_star_2)
    print(f"For star 2 score is: {result_star_2}")   

