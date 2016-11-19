import random

sample_data = []
with open('IntegerArray.txt', 'r') as f:
    for line in f:
        sample_data.append(int(line))


def random_selet(array, target):
    array_len = len(array)
    if array_len == 1:
        return array[0]
    pivot = int(random.random() * array_len)
    array[0], array[pivot] = array[pivot], array[0]
    divier_index = 1
    for i in range(1, len(array)):
        if array[i] < array[0]:
            array[i], array[divier_index] = array[divier_index], array[i]
            divier_index += 1
    inposition = divier_index - 1
    array[0], array[inposition] = array[inposition], array[0]
    if inposition == target:
        return array[inposition]
    elif inposition > target:
        return random_selet(array[:inposition], target)
    elif inposition < target:
        return random_selet(array[inposition + 1:], target - inposition - 1)

for j in range(5):
    print(random_selet(sample_data, 2))
