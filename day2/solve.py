from tqdm import tqdm

class InputData:
    def __init__(self, lowerBound, upperBound):
        self.lowerBound = lowerBound
        self.upperBound = upperBound

    
inputDataList = []
with open("input_example.txt") as f:
    content = f.read().split(",")
    for rangeIDs in content:
        lowerBound, upperBound = rangeIDs.split('-')
        # print(lowerBound, upperBound)
        inputDataList.append(InputData(lowerBound, upperBound))


    # print(content)

# def generatePossibleWrongIDs():

#     invalidIDs = set()

#     for number1 in range(10):
#         for number2 in range(10):
#             for number3 in range(10):
#                 for number4 in range(10):
#                     for number5 in range(10):
                        
#                         number1Str = str(number1)
#                         number2Str = str(number2)
#                         number3Str = str(number3)
#                         number4Str = str(number4)
#                         number5Str = str(number5)

#                         if number1 == 0:
#                             continue

#                         numberLen1 = number1Str 
#                         numberLen2 = number1Str + number2Str
#                         numberLen3 = number1Str + number2Str + number3Str
#                         numberLen4 = number1Str + number2Str + number3Str + number4Str
#                         numberLen5 = number1Str + number2Str + number3Str + number4Str + number5Str
                        
#                         invalidIDs.add(numberLen1 + numberLen1)
#                         invalidIDs.add(numberLen2 + numberLen2)
#                         invalidIDs.add(numberLen3 + numberLen3)
#                         invalidIDs.add(numberLen4 + numberLen4)
#                         invalidIDs.add(numberLen5 + numberLen5)

#     return list(invalidIDs)


# invalidIDs = generatePossibleWrongIDs()

# print(invalidIDs)

def isPatternCorrect(numberStr, pattern):
    patternLen = len(pattern)
    if len(numberStr) % patternLen != 0:
        return False
    for i in range(0, len(numberStr), patternLen):
        range_to_check = numberStr[i:i+patternLen]
        if range_to_check != pattern:
            return False
    return True

def checkForPattern(numberStr):
    for patterLen in range(1,(len(numberStr)//2) + 1):
        prefix = numberStr[:patterLen]
        if isPatternCorrect(numberStr, prefix):
            return True
        
ans = 0
for rangeIDs in tqdm(inputDataList):
    lowerBound = int(rangeIDs.lowerBound)
    upperBound = int(rangeIDs.upperBound)

    for i in range(lowerBound, upperBound+1):
        if checkForPattern(str(i)):
            ans += i
        # print(i)

print(ans)


# ans = 0
# for rangeIDs in inputDataList:
#     for invalidID in invalidIDs:
#         if int(rangeIDs.lowerBound) <= int(invalidID) and int(invalidID) <= int(rangeIDs.upperBound):
#             ans += int(invalidID)
