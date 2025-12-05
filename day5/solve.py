from tqdm import tqdm
from copy import copy
import numpy as np

    
def star1(inputData, DEBUG=False):
    seperator = inputData.index("")
    freshRanges = inputData[:seperator]
    ingredients = inputData[seperator+1:]

    freshIngredients = 0
    for ingredient in ingredients:
        for freshRange in freshRanges:
            lowerBound, upperBound = freshRange.split('-')
            if int(lowerBound) <= int(ingredient) and int(ingredient) <= int(upperBound):
                if DEBUG: print(f"for ingredient {ingredient} we found range {freshRange}")
                freshIngredients += 1
                break
    return freshIngredients

def star2(inputData, DEBUG=False):
    seperator = inputData.index("")
    freshRanges = inputData[:seperator]
    ingredients = inputData[seperator+1:]

    lower_upper_bounds = []
    for freshRange in freshRanges:
        lowerBound, upperBound = freshRange.split('-')
        lower_upper_bounds.append((int(lowerBound), int(upperBound)))

    if DEBUG: print(lower_upper_bounds)

    lower_upper_bounds.sort()

    freshIngredients = 0
    currentIngredient = 0
    for i, (lowerBound, upperBound) in enumerate(lower_upper_bounds):
        if DEBUG: 
            print(i, lowerBound, upperBound)
            print("Debug: ", upperBound, max(lowerBound, currentIngredient), upperBound - max(lowerBound, currentIngredient))
        freshIngredients += max(0, upperBound - max(lowerBound, currentIngredient) + 1)
        currentIngredient = max(upperBound + 1, currentIngredient)

    return freshIngredients




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

    assert result_example_1 == 3

    result_star_1 = star1(inputData_star_1)
    print(f"For star 1 score is: {result_star_1}")


    inputData_example_2 = copy(inputData_example_1)
    inputData_star_2 = copy(inputData_star_1)

    result_example_2 = star2(inputData_example_2)

    print(f"For example 2 score is: {result_example_2}")

    assert result_example_2 == 14

    result_star_2 = star2(inputData_star_2)
    print(f"For star 2 score is: {result_star_2}")   

