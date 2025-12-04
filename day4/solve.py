from tqdm import tqdm
import numpy as np


    
inputData = []
with open("input_1.txt") as f:
    inputData = f.readlines()
    inputData = [line.strip() for line in inputData]


print(inputData)

good_papers = 0

changed = True
while changed:
    changed = False
    mask = np.zeros((len(inputData), len(inputData[0])))
    for y, row in enumerate(inputData):
        new_str = list(row)
        for x, elem in enumerate(row):
            count_paper = 0
            for delta_x in range(-1,2):
                for delta_y in range(-1,2):
                    new_x = x + delta_x
                    new_y = y + delta_y
                    if new_x < 0 or new_x >= len(row):
                        continue
                    if new_y < 0 or new_y >= len(inputData):
                        continue
                    if delta_x == 0 and delta_y == 0:
                        continue
                    count_paper += 1 if inputData[new_y][new_x] == '@' else 0

            # print(count_paper)
            if count_paper < 4 and elem == '@':
                good_papers += 1
                mask[y][x] = 1
                new_str[x] = '.'
                inputData[y] = "".join(new_str)
                changed = True
                # print(y,x)
    for y in range(len(inputData)):
        new_str = list(inputData[y])
        for x in range(len(inputData[0])):
            if mask[y][x]:
                new_str[x] = "."
        
        inputData[y] = "".join(new_str)

for row in inputData:
    print(row)
# print(inputData)
print(good_papers)
