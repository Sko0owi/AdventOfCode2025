from tqdm import tqdm
from copy import copy
import numpy as np


def printDP(dp):
    for i in range(0, len(dp)):
        for j, char in enumerate(dp[i]):
            if dp[i][j] == 0:
                print(".", end="")
            elif dp[i][j] == 1:
                print("|", end="")
            elif dp[i][j] == 2:
                print("^", end="")
            else:
                raise ArithmeticError("WTF")
        print()
    
def star1(inputData, DEBUG=False):

    dp = np.full((len(inputData), len(inputData[0])), -1)

    for i, char in enumerate(inputData[0]):
        if char == 'S':
            dp[0][i] = 1
        else:
            dp[0][i] = 0

    cnt_splitted = 0
    for i in range(1, len(inputData)):
        for j, char in enumerate(inputData[i]):
            if char == '.' and dp[i][j] == -1:
                dp[i][j] = dp[i-1][j]
            elif char == '^' and dp[i-1][j] == 1:
                cnt_splitted += 1
                dp[i][j] = 2
                dp[i][j-1] = 1
                dp[i][j+1] = 1
            elif dp[i][j] == -1:
                dp[i][j] = 0

    return cnt_splitted

def star2(inputData, DEBUG=False):
    
    dp = np.full((len(inputData), len(inputData[0])), -1)

    for i, char in enumerate(inputData[0]):
        if char == 'S':
            dp[0][i] = 1
        else:
            dp[0][i] = 0

    for i in range(1, len(inputData)):
        for j, char in enumerate(inputData[i]):
            if char == '.':
                if dp[i][j] == -1:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] += dp[i-1][j]
            elif char == '^':

                if dp[i-1][j] > 0:
                    dp[i][j] = 0
                    
                    dp[i][j-1] += dp[i-1][j]
                    
                    dp[i][j+1] = dp[i-1][j]
                else:
                    dp[i][j] = 0
                

    print(dp)

    sum_timelines = 0
    for i in range(len(inputData[0])):
        sum_timelines += dp[len(inputData) - 1][i]
    return sum_timelines



if __name__ == '__main__':

    inputData_example_1, inputData_example_2 = [], []
    inputData_star_1, inputData_star_2 = [], []

    with open("input_example_1.txt") as f:
        inputData_example_1 = f.readlines()
        inputData_example_1 = [line.strip() for line in inputData_example_1]
    print(inputData_example_1)

    with open("input_star_1.txt") as f:
        inputData_star_1 = f.readlines()
        inputData_star_1 = [line.strip() for line in inputData_star_1]
    # print(inputData_star_1)

    result_example_1 = star1(inputData_example_1)

    print(f"For example 1 score is: {result_example_1}")

    assert result_example_1 == 21

    result_star_1 = star1(inputData_star_1)
    print(f"For star 1 score is: {result_star_1}")

    inputData_example_2 = copy(inputData_example_1)
    inputData_star_2 = copy(inputData_star_1)

    result_example_2 = star2(inputData_example_2)

    print(f"For example 2 score is: {result_example_2}")

    assert result_example_2 == 40

    result_star_2 = star2(inputData_star_2)
    print(f"For star 2 score is: {result_star_2}")   

