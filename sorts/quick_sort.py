def partition(array, low, high):
    i = (low-1)
    pivot = array[high]

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return (i+1)


def quickSort(array, low, high):
    if low < high:
        # partition index to split array
        part_idx = partition(array, low, high)
        # part_idx not included since it's already at right place
        quickSort(array, low, part_idx-1)
        quickSort(array, part_idx+1, high)

    return array
