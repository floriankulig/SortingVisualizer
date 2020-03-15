def bubble_sort_animations(array):
    if len(array) <= 1:
        return
    animations = list()
    bubble_sort(array, animations)
    return animations


def bubble_sort(array, animations):
    # for every element in the array
    for i in range(len(array)):
        # for every element until the already sorted(i) elements
        for j in range(len(array)-1-i):
            # append to change the colors of the bars we're comparing
            animations.append([j, array[j], j+1, array[j+1]])
            if array[j] > array[j+1]:
                # assign new value to bars
                array[j], array[j+1] = array[j+1], array[j]
            # append again to revert color
            animations.append([j, array[j], j+1, array[j+1]])
        # append last element, it's already sorted
        animations.append([-(i+1), 0, -(i+1), 0])
    return animations
