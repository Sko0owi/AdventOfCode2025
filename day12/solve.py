from tqdm import tqdm
from copy import copy
import numpy as np

    
def star1(inputData, DEBUG=False):
    presentAreaCnt = {"0" : 0, "1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0}
    for id in range(6):
        presentID = inputData[id*5].strip(":")
        for presentRowID in range(1,4):
            presentRow = inputData[id*5+presentRowID]
            presentAreaCnt[presentID] += presentRow.count("#")


    impossible_trees = []
    possible_trees = []
    easy_trees = []

    restInput = inputData[6*5:]
    for tree_id, tree in enumerate(restInput):
        treeList = tree.split()
        width, height = list(map(int,treeList[0].strip(":").split("x")))
        presentsOverall = 0
        areaOfPresents = 0
        presentsCount = treeList[1:]
        for i, presentCount in enumerate(presentsCount):
            areaOfPresents += presentAreaCnt[str(i)]*int(presentCount)
            presentsOverall += int(presentCount)
        
        areaOfTree = width*height
        if areaOfTree < areaOfPresents:
            impossible_trees.append(tree_id)
        elif presentsOverall*9 <= areaOfTree:
            easy_trees.append(tree_id)
        else:
            possible_trees.append(tree_id)

    print(f"Impossible trees: {len(impossible_trees)}")
    print(f"Possible trees: {len(possible_trees)}")
    print(f"Easy trees: {len(easy_trees)}")

    return len(possible_trees) + len(easy_trees)

def star2(inputData, DEBUG=False):
    return 0

if __name__ == '__main__':

    inputData_example_1, inputData_example_2 = [], []
    inputData_star_1, inputData_star_2 = [], []

    with open("input_example_1.txt") as f:
        inputData_example_1 = f.readlines()
        inputData_example_1 = [line.strip("\n") for line in inputData_example_1]
    # print(inputData_example_1)

    with open("input_star_1.txt") as f:
        inputData_star_1 = f.readlines()
        inputData_star_1 = [line.strip("\n") for line in inputData_star_1]
    # print(inputData_star_1)

    # only check input for star
    # result_example_1 = star1(inputData_example_1)
    # print(f"For example 1 score is: {result_example_1}")
    # assert result_example_1 == 2 

    result_star_1 = star1(inputData_star_1)
    print(f"For star 1 score is: {result_star_1}")
