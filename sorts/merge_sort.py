def merge_sort_animations(array):
    animations = []
    if len(array) == 1:
        return array
    # copies array
    helper_array = array[:]
    split_array(array, 0, len(array)-1, helper_array, animations)
    return animations


def split_array(array, start_idx, end_idx, helper_array, animations):
    # exit condition when arraysize is 1
    if start_idx == end_idx:
        return
    mid = (start_idx + end_idx)//2

    split_array(helper_array, start_idx, mid, array, animations)
    split_array(helper_array, mid + 1, end_idx, array, animations)

    actual_merge(array, start_idx, mid, end_idx, helper_array, animations)


def actual_merge(array,
                 start_idx,
                 mid,
                 end_idx,
                 helper_array,
                 animations):
    i = k = start_idx
    j = mid + 1

    while i <= mid and j <= end_idx:
        # Append for color change
        animations.append([i, j])

        if helper_array[i] <= helper_array[j]:
            animations.append([i, j])
            animations.append([k, helper_array[i], j])
            array[k] = helper_array[i]
            i += 1
        else:
            animations.append([i, j])
            animations.append([k, helper_array[j], j])
            array[k] = helper_array[j]
            j += 1
        k += 1

    while i <= mid:
        # Append for color change
        animations.append([i, i])
        animations.append([i, i])

        animations.append([k, helper_array[i], j])
        array[k] = helper_array[i]
        i += 1
        k += 1

    while j <= end_idx:
        # Append for color change
        animations.append([j, j])
        animations.append([j, j])

        animations.append([k, helper_array[j], j])
        array[k] = helper_array[j]
        j += 1
        k += 1

    return animations
