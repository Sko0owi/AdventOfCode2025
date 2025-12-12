from tqdm import tqdm
from copy import copy
import numpy as np
from collections import deque

    
def star1(inputData, DEBUG=False):
    pathsCnt = {}
    neighbours = {}
    visited = {}
    v_ins = {}
    for row in inputData:
        fromV, rest = row[0].strip(":"), row[1:]
        neighbours[fromV] = []
        for toV in rest:
            visited[toV] = 0
            pathsCnt[toV] = 0
            v_ins[toV] = 0
            neighbours[fromV].append(toV)
        pathsCnt[fromV] = 0
        visited[fromV] = 0
        v_ins[fromV] = 0

        print(f"From: {fromV} rest: {rest}")

    q = deque([("you", "")])
    visited["you"] = 1
    while q:
        top,parent = q.popleft()
        if top == "out":
            break
        # print(top)
        print(f"Top: {top}, Parent: {parent}")
        for neighbour in neighbours[top]:
            print(f"neighbour: {neighbour}")
            if neighbour != parent:
                v_ins[neighbour] += 1
                if visited[neighbour] == 0: 
                    visited[neighbour] = 1
                    q.append((neighbour, top))
    
    print(v_ins)
    q = deque([("you")])
    pathsCnt["you"] = 1
    while q:
        top = q.popleft()
        if top == "out":
            break
        # print(top)
        print(f"Top: {top}")
        for neighbour in neighbours[top]:
            print(f"neighbour: {neighbour}")
            v_ins[neighbour] -= 1
            assert v_ins[neighbour] >= 0
            
            pathsCnt[neighbour] += pathsCnt[top]
            if v_ins[neighbour] == 0:
                q.append(neighbour)
    
    print(pathsCnt)

    return pathsCnt["out"]

def star2(inputData, DEBUG=False):
    pathsCnt = {}
    pathsWithFFTCnt = {}
    pathsWithDACCnt = {}
    pathsWithBothCnt = {}
    neighbours = {}
    visited = {}
    v_ins = {}
    for row in inputData:
        fromV, rest = row[0].strip(":"), row[1:]
        neighbours[fromV] = []
        for toV in rest:
            visited[toV] = 0
            pathsCnt[toV] = 0
            pathsWithFFTCnt[toV] = 0
            pathsWithDACCnt[toV] = 0
            pathsWithBothCnt[toV] = 0
            v_ins[toV] = 0
            neighbours[fromV].append(toV)
        pathsCnt[fromV] = 0
        pathsWithFFTCnt[fromV] = 0
        pathsWithDACCnt[fromV] = 0
        pathsWithBothCnt[fromV] = 0
        visited[fromV] = 0
        v_ins[fromV] = 0

        print(f"From: {fromV} rest: {rest}")

    q = deque([("svr", "")])
    visited["svr"] = 1
    while q:
        top,parent = q.popleft()
        if top == "out":
            break
        # print(top)
        print(f"Top: {top}, Parent: {parent}")
        for neighbour in neighbours[top]:
            print(f"neighbour: {neighbour}")
            if neighbour != parent:
                v_ins[neighbour] += 1
                if visited[neighbour] == 0: 
                    visited[neighbour] = 1
                    q.append((neighbour, top))
    
    print(v_ins)
    q = deque([("svr")])
    pathsCnt["svr"] = 1
    while q:
        top = q.popleft()
        if top == "out":
            break

        if top == "dac":
            print("O CIE CHUJ")
            pathsWithDACCnt[top] += pathsCnt[top]
            pathsWithBothCnt[top] += min(pathsWithDACCnt[top], pathsWithFFTCnt[top])
        
        if top == "fft":

            pathsWithFFTCnt[top] += pathsCnt[top]
            pathsWithBothCnt[top] += min(pathsWithDACCnt[top], pathsWithFFTCnt[top])
        

        # print(top)
        print(f"Top: {top}")
        for neighbour in neighbours[top]:
            print(f"neighbour: {neighbour}")
            v_ins[neighbour] -= 1
            assert v_ins[neighbour] >= 0
            
            pathsCnt[neighbour] += pathsCnt[top]
            pathsWithFFTCnt[neighbour] += pathsWithFFTCnt[top]
            pathsWithDACCnt[neighbour] += pathsWithDACCnt[top]
            pathsWithBothCnt[neighbour] += pathsWithBothCnt[top]

            if v_ins[neighbour] == 0:
                q.append(neighbour)
    
    print(pathsCnt)
    print(pathsWithFFTCnt)
    print(pathsWithDACCnt)
    print(pathsWithBothCnt)

    return pathsWithBothCnt["out"]

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

    assert result_example_1 == 5

    result_star_1 = star1(inputData_star_1)
    print(f"For star 1 score is: {result_star_1}")

    with open("input_example_2.txt") as f:
        inputData_example_2 = f.readlines()
        inputData_example_2 = [line.split() for line in inputData_example_2]

    with open("input_star_1.txt") as f:
        inputData_star_2 = f.readlines()
        inputData_star_2 = [line.split() for line in inputData_star_2]

    result_example_2 = star2(inputData_example_2)

    print(f"For example 2 score is: {result_example_2}")

    assert result_example_2 == 2

    result_star_2 = star2(inputData_star_2)
    print(f"For star 2 score is: {result_star_2}")   

