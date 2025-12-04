from tqdm import tqdm


    
inputData = []
with open("input_1.txt") as f:
    inputData = f.readlines()
    inputData = [line.strip() for line in inputData]


print(inputData)

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

    print(biggest_number)
    
    final_number_str = "".join(map(str,biggest_number)).replace('0', '')
    print(int(final_number_str))
    sum_numbers += int(final_number_str)

print(sum_numbers)

