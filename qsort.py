import random

sample_data = []
with open('IntegerArray.txt', 'r') as f:
    for line in f:
        sample_data.append(int(line))


def qsort(array):
    compare_number = 0

    def qsort_recursion(array, start, last):
        nonlocal compare_number
        compare_number += last - start - 1
        array_len = last - start
        if array_len > 1:
            # random selected pivot:
            # pivot = start + int(random.random() * array_len)
            # first index pivot:
            # pivot = start
            # medium of (start, medium, last):
            medium = start + array_len // 2 - \
                1 if array_len % 2 == 0 else (start + last - 1) // 2
            if array[start] > array[last - 1]:
                if array[medium] > array[start]:
                    pivot = start
                else:
                    if array[medium] > array[last - 1]:
                        pivot = medium
                    else:
                        pivot = last - 1
            else:
                if array[medium] > array[last - 1]:
                    pivot = last - 1
                else:
                    if array[medium] > array[start]:
                        pivot = medium
                    else:
                        pivot = start
            # quick sort begin
            array[start], array[pivot] = array[pivot], array[start]
            divider = start + 1
            for i in range(start + 1, last):
                if array[i] < array[start]:
                    array[divider], array[i] = array[i], array[divider]
                    divider += 1
            array[start], array[divider - 1] = array[divider - 1], array[start]
            qsort_recursion(array, start, divider - 1)
            qsort_recursion(array, divider, last)

    qsort_recursion(array, 0, len(array))
    return compare_number

print(qsort(sample_data))
# print(sample_data)
