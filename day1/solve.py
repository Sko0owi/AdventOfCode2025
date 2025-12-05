from copy import copy


class InputData:
    def __init__(self, rotation, value):
        self.rotation = rotation
        self.value = value
    def __repr__(self):
        return f"Rotation: {self.rotation}, Value: {self.value}"

class Lock:
    def __init__(self, star):
        self.position = 50
        self.current_password = 0
        self.star = star

    def _rotate_left(self, value):
        new_position = self.position
        while value:
            new_position -= 1
            if new_position == -1:
                new_position = 99

            if self.star == 2 and new_position == 0:
                self.current_password += 1

            value -= 1

        if self.star == 1 and new_position == 0:
            self.current_password += 1
        self.position = new_position

    def _rotate_right(self, value):
        new_position = self.position
        while value:
            new_position += 1
            if new_position == 100:
                new_position = 0

            if self.star == 2 and new_position == 0:
                self.current_password += 1

            value -= 1
        
        if self.star == 1 and new_position == 0:
            self.current_password += 1
        self.position = new_position
    
    def rotate_lock(self, rotation, value):
        if rotation == 'L':
            self._rotate_left(value)
        elif rotation == 'R':
            self._rotate_right(value)
        else:
            raise ValueError

    def __repr__(self):
        return f"Current value is {self.position}"
    
def star1(inputData, DEBUG=False):

    inputDataList = []
    for input in inputData:
        inputDataList.append(InputData(input[0], int(input[1:])))

    lock = Lock(star=1)

    for input_data in inputDataList:
        lock.rotate_lock(input_data.rotation, input_data.value)
        if DEBUG: print(lock)

    return lock.current_password

def star2(inputData, DEBUG=False):
    inputDataList = []
    for input in inputData:
        inputDataList.append(InputData(input[0], int(input[1:])))

    lock = Lock(star=2)

    for input_data in inputDataList:
        lock.rotate_lock(input_data.rotation, input_data.value)
        if DEBUG: print(lock)

    return lock.current_password




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

    assert result_example_2 == 6

    result_star_2 = star2(inputData_star_2)
    print(f"For star 2 score is: {result_star_2}")   