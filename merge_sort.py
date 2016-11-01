def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        array_len = len(array)
        left = merge_sort(array[:array_len // 2])
        right = merge_sort(array[array_len // 2:])
        i, j = 0, 0
        merged_array = []
        while i < len(left) or j < len(right):
            if left[i] < right[j]:
                merged_array.append(left[i])
                i += 1
            else:
                merged_array.append(right[j])
                j += 1
            if i == len(left):
                merged_array += (right[j:])
                break
            if j == len(right):
                merged_array += (left[i:])
                break
    return merged_array


print(merge_sort([5, 4, 3, 2, 3, 5, 324, 121, 2, 44, 1, 0]))
