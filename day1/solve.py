
class InputData:
    def __init__(self, rotation, value):
        self.rotation = rotation
        self.value = value
    def __repr__(self):
        return f"Rotation: {self.rotation}, Value: {self.value}"

input_list = []
input_data_list = []
with open("input_example.txt") as f:
    input_list = f.readlines()
    input_list = [line.strip() for line in input_list]
    for input in input_list:
        input_data_list.append(InputData(input[0], int(input[1:])))

print(input_list[:5])
print(input_data_list[:5])

class Lock:
    def __init__(self):
        self.position = 50
        self.current_password = 0

    def _rotate_left(self, value):
        new_position = self.position
        while value:
            new_position -= 1
            if new_position == -1:
                new_position = 99

            if new_position == 0:
                self.current_password += 1

            value -= 1
        
        self.position = new_position

    def _rotate_right(self, value):
        new_position = self.position
        while value:
            new_position += 1
            if new_position == 100:
                new_position = 0

            if new_position == 0:
                self.current_password += 1

            value -= 1
        
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
    

lock = Lock()
print(lock)

for input_data in input_data_list:
    lock.rotate_lock(input_data.rotation, input_data.value)
    print(lock)


print(lock.current_password)