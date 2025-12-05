from tqdm import tqdm
from copy import copy


class InputData:
    def __init__(self, lowerBound, upperBound):
        self.lowerBound = lowerBound
        self.upperBound = upperBound

def star1(inputData):

    def generatePossibleWrongIDs():

        invalidIDs = set()

        for number1 in range(10):
            for number2 in range(10):
                for number3 in range(10):
                    for number4 in range(10):
                        for number5 in range(10):
                            
                            number1Str = str(number1)
                            number2Str = str(number2)
                            number3Str = str(number3)
                            number4Str = str(number4)
                            number5Str = str(number5)

                            if number1 == 0:
                                continue

                            numberLen1 = number1Str 
                            numberLen2 = number1Str + number2Str
                            numberLen3 = number1Str + number2Str + number3Str
                            numberLen4 = number1Str + number2Str + number3Str + number4Str
                            numberLen5 = number1Str + number2Str + number3Str + number4Str + number5Str
                            
                            invalidIDs.add(numberLen1 + numberLen1)
                            invalidIDs.add(numberLen2 + numberLen2)
                            invalidIDs.add(numberLen3 + numberLen3)
                            invalidIDs.add(numberLen4 + numberLen4)
                            invalidIDs.add(numberLen5 + numberLen5)

        return list(invalidIDs)

    invalidIDs = generatePossibleWrongIDs()
    sumOfInvalidIDs = 0
    for invalidID in tqdm(invalidIDs):
        for rangeIDs in inputData:
            lowerBound = int(rangeIDs.lowerBound)
            upperBound = int(rangeIDs.upperBound)
            if lowerBound <= int(invalidID) and int(invalidID) <= upperBound:
                sumOfInvalidIDs += int(invalidID)
    return sumOfInvalidIDs

def star2(inputData):
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
            
    sumOfInvalidIDs = 0
    for rangeIDs in tqdm(inputData):
        lowerBound = int(rangeIDs.lowerBound)
        upperBound = int(rangeIDs.upperBound)

        for i in range(lowerBound, upperBound+1):
            if checkForPattern(str(i)):
                sumOfInvalidIDs += i

    return sumOfInvalidIDs


if __name__ == '__main__':

    inputData_example_1, inputData_example_2 = [], []
    inputData_star_1, inputData_star_2 = [], []

    with open("input_example_1.txt") as f:
        content = f.read().split(",")
        for rangeIDs in content:
            lowerBound, upperBound = rangeIDs.split('-')
            inputData_example_1.append(InputData(lowerBound, upperBound))
    # print(inputData_example_1)

    with open("input_star_1.txt") as f:
        content = f.read().split(",")
        for rangeIDs in content:
            lowerBound, upperBound = rangeIDs.split('-')
            inputData_star_1.append(InputData(lowerBound, upperBound))
    # print(inputData_star_1)

    result_example_1 = star1(inputData_example_1)

    print(f"For example 1 score is: {result_example_1}")

    assert result_example_1 == 1227775554

    result_star_1 = star1(inputData_star_1)
    print(f"For star 1 score is: {result_star_1}")

    inputData_example_2 = copy(inputData_example_1)
    inputData_star_2 = copy(inputData_star_1)

    result_example_2 = star2(inputData_example_2)

    print(f"For example 2 score is: {result_example_2}")

    assert result_example_2 == 4174379265

    result_star_2 = star2(inputData_star_2)
    print(f"For star 2 score is: {result_star_2}")   