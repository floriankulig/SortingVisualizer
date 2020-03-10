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
        # iterate through array reversed until element is smaller than pivot
        while low <= high and array[high] >= pivot:
            high -= 1

        # iterate through array until element is bigger than pivot
        while low <= high and array[low] <= pivot:
            low += 1

        ''' swap low and high element if didn't bypass eachother
            (smaller element than pivot will be left and vice versa)'''
        if low < high:
            array[low], array[high] = array[high], array[low]
            # append for color change (make clear which values we're swapping)
            animations.append([low, high])
            # append both indices to get them their new values
            animations.append([low, array[low], high, array[high]])
            # append second time to revert color
            animations.append([low, high])

        else:
            break

    '''swap pivot element with high_idx element so every element to the
    left of pivot is smaller and elements to the right are bigger than
    pivot'''
    array[start_idx], array[high] = array[high], array[start_idx]
    # append for color change (make clear which values we're swapping)
    animations.append([start_idx, high])
    # append both indices to get them their new values
    animations.append([high, array[high], start_idx, array[start_idx]])
    # append second time to revert color
    animations.append([start_idx, high])

    '''return high element (now where pivot is) to recursively split array
    in "quick_sort" function
    element with index of high is now at its right spot
    append it to animations list to apply a final color'''
    return high


def quick_sort(array, start_idx, end_idx, animations):
    if start_idx < end_idx:
        # partition index to split array
        part_idx = make_partition(array, start_idx, end_idx, animations)
        # part_idx not included since it's already at right place
        quick_sort(array, start_idx, part_idx-1, animations)
        quick_sort(array, part_idx+1, end_idx, animations)
    return animations
