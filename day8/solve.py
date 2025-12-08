from tqdm import tqdm
from copy import copy
import numpy as np

class Cable:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return f"cable x: {self.x}, y: {self.y}, z: {self.z}"

def euclidean_dist(cable1 : Cable, cable2 : Cable):
    dist = np.sqrt((cable1.x - cable2.x) ** 2 + (cable1.y - cable2.y) ** 2 + (cable1.z - cable2.z) ** 2)
    return dist 
    
def find(a, parents):
    if parents[a] == a:
        return a
    value = find(parents[a], parents)
    parents[a] = value
    return value

def union(a, b, parents, sizes):
    a = find(a, parents)
    b = find(b, parents)

    if a == b:
        return parents, sizes
    
    if sizes[a] < sizes[b]:
        sizes[b] += sizes[a]
        parents[a] = b
    else:
        sizes[a] += sizes[b]
        parents[b] = a

    return parents, sizes
    
    

def star1(inputData, DEBUG=False):

    cable_list = []
    for cable in inputData:
        cable_list.append(Cable(int(cable[0]), int(cable[1]), int(cable[2])))

    distances = []
    for i in range(len(cable_list)):
        for j in range(i + 1, len(cable_list)):
            if i == j: continue
            distances.append((euclidean_dist(cable_list[i], cable_list[j]), (i,j)))

    distances.sort()

    parents = []
    sizes = []
    for i in range(len(cable_list)):
        sizes.append(1)
        parents.append(i)

    loop_max = 10 if DEBUG else 1000
    for _, (x, y) in  distances[:loop_max]:
        parents, sizes = union(x, y, parents, sizes)

    sizes.sort(reverse=True)

    ans = sizes[0] * sizes[1] * sizes[2]


    return ans
def star2(inputData, DEBUG=False):
    
    cable_list = []
    for cable in inputData:
        cable_list.append(Cable(int(cable[0]), int(cable[1]), int(cable[2])))
    

    distances = []
    for i in range(len(cable_list)):
        for j in range(i + 1, len(cable_list)):
            if i == j: continue
            distances.append((euclidean_dist(cable_list[i], cable_list[j]), (i,j)))

    distances.sort()

    parents = []
    sizes = []
    for i in range(len(cable_list)):
        sizes.append(1)
        parents.append(i)


    for distance, (x, y) in  distances:
        parents, sizes = union(x, y, parents, sizes)
        if len(sizes) in sizes:
            return cable_list[x].x * cable_list[y].x


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

    result_example_1 = star1(inputData_example_1, DEBUG=True)

    print(f"For example 1 score is: {result_example_1}")

    assert result_example_1 == 40

    result_star_1 = star1(inputData_star_1)
    print(f"For star 1 score is: {result_star_1}")

    with open("input_example_1.txt") as f:
        inputData_example_2 = f.readlines()
        inputData_example_2 = [line.strip().split(",") for line in inputData_example_2]

    with open("input_star_1.txt") as f:
        inputData_star_2 = f.readlines()
        inputData_star_2 = [line.strip().split(",") for line in inputData_star_2]

    result_example_2 = star2(inputData_example_2)

    print(f"For example 2 score is: {result_example_2}")

    assert result_example_2 == 25272

    result_star_2 = star2(inputData_star_2)
    print(f"For star 2 score is: {result_star_2}")   

