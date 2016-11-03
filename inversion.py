sample_data = []
with open('IntegerArray.txt', 'r') as f:
    for line in f:
        sample_data.append(int(line))

# print(sample_data)


def count_inversion(array):
    inversion = 0

    def recursion(array):
        nonlocal inversion

        def sort_and_merge(left, right):
            nonlocal inversion
            i, j = 0, 0
            merged_array = []
            while i < len(left) or j < len(right):
                # print(inversion)
                if left[i] < right[j]:
                    merged_array.append(left[i])
                    i += 1
                else:
                    merged_array.append(right[j])
                    inversion += len(left) - i
                    j += 1
                if i == len(left):
                    merged_array += right[j:]
                    break
                if j == len(right):
                    merged_array += left[i:]
                    break
            return merged_array
        array_length = len(array)
        if array_length <= 2:
            if array_length == 1:
                return array
            if array[0] < array[1]:
                return array
            else:
                inversion += 1
                return [array[1], array[0]]
        else:
            left_array = recursion(array[:array_length // 2])
            right_array = recursion(array[array_length // 2:])
            sorted_array = sort_and_merge(left_array, right_array)
            # print(sorted_array)
            return sorted_array
    recursion(array)
    return inversion
print(count_inversion(sample_data))
