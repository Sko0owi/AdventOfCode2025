from tqdm import tqdm
from copy import copy

def star1(inputData):
    sum_numbers = 0
    for batteryBank in tqdm(inputData):
        banned_i = []
        biggest_number = []
        starting_i = 0
        for number_cnt in range(2):
            current_biggest_digit = 0
            current_i = -1
            for i in range(starting_i, len(batteryBank) - 2 + number_cnt + 1):
                if int(batteryBank[i]) > current_biggest_digit and i not in banned_i:
                    current_biggest_digit = int(batteryBank[i])
                    current_i = i

            banned_i.append(current_i)
            biggest_number.append(current_biggest_digit)
            starting_i = current_i + 1
        
        final_number_str = "".join(map(str,biggest_number)).replace('0', '')
        sum_numbers += int(final_number_str)

    return sum_numbers

def star2(inputData):
    sum_numbers = 0
    for batteryBank in tqdm(inputData):
        banned_i = []
        biggest_number = []
        starting_i = 0
        for number_cnt in range(12):
            current_biggest_digit = 0
            current_i = -1
            for i in range(starting_i, len(batteryBank) - 12 + number_cnt + 1):
                if int(batteryBank[i]) > current_biggest_digit and i not in banned_i:
                    current_biggest_digit = int(batteryBank[i])
                    current_i = i

            banned_i.append(current_i)
            biggest_number.append(current_biggest_digit)
            starting_i = current_i + 1
        
        final_number_str = "".join(map(str,biggest_number)).replace('0', '')
        sum_numbers += int(final_number_str)

    return sum_numbers


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

    assert result_example_1 == 357

    result_star_1 = star1(inputData_star_1)
    print(f"For star 1 score is: {result_star_1}")

    inputData_example_2 = copy(inputData_example_1)
    inputData_star_2 = copy(inputData_star_1)

    result_example_2 = star2(inputData_example_2)

    print(f"For example 2 score is: {result_example_2}")

    assert result_example_2 == 3121910778619

    result_star_2 = star2(inputData_star_2)
    print(f"For star 2 score is: {result_star_2}")   