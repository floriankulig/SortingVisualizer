def bubble_sort_animations(array):
    if len(array) <= 1:
        return
    animations = list()
    bubble_sort(array, animations)
    return animations


def bubble_sort(array, animations):
    for i in range(len(array)):
        for j in range(len(array)-1-i):

            animations.append([j, array[j], j+1, array[j+1]])
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            animations.append([j, array[j], j+1, array[j+1]])
        # append last element, it's already sorted
        animations.append([-(i+1), 0, -(i+1), 0])
    return animations
