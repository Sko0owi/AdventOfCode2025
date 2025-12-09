from tqdm import tqdm
from copy import copy
import numpy as np

    
def star1(inputData, DEBUG=False):
    # print(inputData)
    biggestArea = 0
    for i in range(len(inputData)):
        for j in range(i+1, len(inputData)):
            firstCorner = inputData[i]
            secondCorner = inputData[j]

            currentArea = (abs(int(firstCorner[0]) - int(secondCorner[0])) + 1) * (abs(int(firstCorner[1]) - int(secondCorner[1])) + 1)
            biggestArea = max(currentArea, biggestArea)
    return biggestArea

def build_edges(points):
    n = len(points)
    return [(points[i], points[(i+1)%n]) for i in range(n)]

def is_on_boundary(pt, points, edges):
    x,y = pt
    if pt in points:
        return True
    for (ax,ay),(bx,by) in edges:
        if ax == bx == x:
            if min(ay,by) <= y <= max(ay,by):
                return True
        if ay == by == y:
            if min(ax,bx) <= x <= max(ax,bx):
                return True
    return False


def point_in_poly(pt, points, edges):
    if is_on_boundary(pt, points, edges):
        return True
    x,_ = pt
    inside = False
    n = len(points)
    for i in range(n):
        x1,_ = points[i]
        x2,_ = points[(i+1)%n]

        if x1 != x2:
            continue
        if x1 > x:
            inside = not inside
    return inside

def rectangle_area_if_valid(p1, p2, points, edges):
    x1,y1 = p1
    x2,y2 = p2

    if x1 == x2 or y1 == y2: return 0

    xL,xR = sorted((x1,x2))
    yT,yB = sorted((y1,y2))

    C = (x1,y2)
    D = (x2,y1)
    if not point_in_poly(C, points, edges): return 0
    if not point_in_poly(D, points, edges): return 0

    for (ax,ay),(bx,by) in edges:
        if ax==bx:
            x=ax
            if xL < x < xR:
                miny,maxy = sorted((ay, by))
                if maxy > yT and miny < yB:
                    return 0
        elif ay==by:
            y=ay
            if yT < y < yB:
                minx,maxx = sorted((ax, bx))
                if maxx > xL and minx < xR:
                    return 0
                
    width = abs(x1-x2)+1
    height = abs(y1-y2)+1
    return width*height


def star2(inputData, DEBUG=False):
    
    biggestArea = 0

    edges = build_edges(inputData)
    for i in tqdm(range(len(inputData))):
        for j in range(i+1, len(inputData)):
            currentCorner = inputData[i]
            nextCorner = inputData[j]

            area = rectangle_area_if_valid(currentCorner,nextCorner,inputData,edges)
            biggestArea = max(biggestArea, area)

    return biggestArea

if __name__ == '__main__':

    inputData_example_1, inputData_example_2 = [], []
    inputData_star_1, inputData_star_2 = [], []

    with open("input_example_1.txt") as f:
        inputData_example_1 = f.readlines()
        inputData_example_1 = [line.strip().split(",") for line in inputData_example_1]
    # print(inputData_example_1)

    with open("input_star_1.txt") as f:
        inputData_star_1 = f.readlines()
        inputData_star_1 = [line.strip().split(",") for line in inputData_star_1]
    # print(inputData_star_1)

    result_example_1 = star1(inputData_example_1)

    print(f"For example 1 score is: {result_example_1}")

    assert result_example_1 == 50

    result_star_1 = star1(inputData_star_1)
    print(f"For star 1 score is: {result_star_1}")

    with open("input_example_1.txt") as f:
        inputData_example_2 = f.readlines()
        inputData_example_2 = [list(map(int,line.strip().split(","))) for line in inputData_example_2]

    with open("input_star_1.txt") as f:
        inputData_star_2 = f.readlines()
        inputData_star_2 = [list(map(int,line.strip().split(","))) for line in inputData_star_2]

    result_example_2 = star2(inputData_example_2)

    print(f"For example 2 score is: {result_example_2}")

    assert result_example_2 == 24

    result_star_2 = star2(inputData_star_2)
    print(f"For star 2 score is: {result_star_2}")   

