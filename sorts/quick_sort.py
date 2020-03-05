def quick_sort_animations(array):
    animations = list()
    if len(array) <= 1:
        return
    quick_sort(array, 0, len(array)-1, animations)
    return animations


def make_partition(array, start_idx, end_idx, animations):
    # quicksort with first element as pivot element
    pivot = array[start_idx]
    low = start_idx + 1
    high = end_idx

    while True:

        while low <= high and array[high] >= pivot:
            high -= 1

        while low <= high and array[low] <= pivot:
            low += 1

        if low < high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    
    array[start_idx], array[high] = array[high], array[start_idx]

    
    return high


def quick_sort(array, start_idx, end_idx, animations):
    if start_idx < end_idx:
        # partition index to split array
        part_idx = make_partition(array, start_idx, end_idx, animations)
        # part_idx not included since it's already at right place
        quick_sort(array, start_idx, part_idx-1, animations)
        quick_sort(array, part_idx+1, end_idx, animations)
    return animations
