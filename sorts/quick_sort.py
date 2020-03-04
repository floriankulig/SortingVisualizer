def quick_sort_animations(array):
    animations = list()
    if len(array) <= 1:
        return
    quick_sort(array, 0, len(array)-1, animations)
    return animations


def make_partition(array, low, high, animations):
    i = (low-1)
    pivot = array[high]

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            animations.append([i, j])
            animations.append([i, j])
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return (i+1)


def quick_sort(array, low, high, animations):
    if low < high:
        # partition index to split array
        part_idx = make_partition(array, low, high, animations)
        # part_idx not included since it's already at right place
        quick_sort(array, low, part_idx-1, animations)
        quick_sort(array, part_idx+1, high, animations)

    return animations
