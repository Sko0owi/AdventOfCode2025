from tqdm import tqdm
from copy import copy
import numpy as np


directions = [(-1,-1), (-1,0), (-1,1), (0, -1), (0,1), (1, -1), (1,0), (1,1)]


def star1(inputData):
    for i, row in enumerate(inputData):
        inputData[i] = list(row)

    good_papers = 0
    for y, row in enumerate(inputData):
        for x, elem in enumerate(row):
            count_paper = 0

            for delta_x, delta_y in directions:
                new_x = x + delta_x
                new_y = y + delta_y
                if new_x < 0 or new_x >= len(row):
                    continue
                if new_y < 0 or new_y >= len(inputData):
                    continue
                count_paper += 1 if inputData[new_y][new_x] == '@' else 0

            if count_paper < 4 and elem == '@':
                good_papers += 1

    return good_papers


def star2(inputData):
    for i, row in enumerate(inputData):
        inputData[i] = list(row)

    good_papers = 0
    changed = True
    while changed:
        changed = False
        for y, row in enumerate(inputData):
            for x, elem in enumerate(row):
                count_paper = 0

                for delta_x, delta_y in directions:
                    new_x = x + delta_x
                    new_y = y + delta_y
                    if new_x < 0 or new_x >= len(row):
                        continue
                    if new_y < 0 or new_y >= len(inputData):
                        continue
                    count_paper += 1 if inputData[new_y][new_x] == '@' else 0

                if count_paper < 4 and elem == '@':
                    good_papers += 1
                    row[x] = '.'
                    changed = True

    return good_papers



if __name__ == '__main__':

    inputData_example_1, inputData_example_2 = [], []
    inputData_star_1, inputData_star_2 = [], []

    with open("input_example_1.txt") as f:
        inputData_example_1 = f.readlines()
        inputData_example_1 = [line.strip() for line in inputData_example_1]
    # print(inputData_example_1)

    with open("input_star_1.txt") as f:
        inputData_star_1 = f.readlines()
        inputData_star_1 = [line.strip() for line in inputData_star_1]
    # print(inputData_star_1)

    result_example_1 = star1(inputData_example_1)

    print(f"For example 1 score is: {result_example_1}")

    assert result_example_1 == 13

    result_star_1 = star1(inputData_star_1)
    print(f"For star 1 score is: {result_star_1}")

    inputData_example_2 = copy(inputData_example_1)
    inputData_star_2 = copy(inputData_star_1)

    result_example_2 = star2(inputData_example_2)

    print(f"For example 2 score is: {result_example_2}")

    assert result_example_2 == 43

    result_star_2 = star2(inputData_star_2)
    print(f"For star 2 score is: {result_star_2}")   
