# Sorting Algorithms

## DE

In diesem Sorting-Visualizer werden die vier bekanntesten Sortieralgorithmen implementiert werden:

1. Mergesort
2. Quicksort
3. Bubblesort
4. Heapsort

### Mergesort

- hat eine Performance-Notation von O(n log n)
- ist ein Sortieralgorithmus der auf _divide and conquer_ -also teilen und herrschen- basiert. Das heißt, dass die zu sortierende Zahlenfolge immer wieder geteilt wird. So kann höhere Leistung garantiert werden.
- weitere Informationen unter: https://de.wikipedia.org/wiki/Mergesort

#### Im Code:

- Wir teilen die Nummerliste rekursiv immer weiter in jeweils zwei untergeordnete Listen, bis die Liste nur noch ein Element beinhaltet.

```python
if start_idx == end_idx:
    return
mid = (start_idx + end_idx)//2

split_array(helper_array, start_idx, mid, array, animations)
split_array(helper_array, mid + 1, end_idx, array, animations)
```

- Wir iterieren durch beide untergeordnete Listen (index i, j) und fügen die jeweils die kleine Zahl in die Hauptliste (am index k) hinzu, bis wir durch mindestens eine untergeordnete Liste iteriert haben.

```python
while i <= mid and j <= end_idx:
    if helper_array[i] <= helper_array[j]:
        array[k] = helper_array[i]
        i += 1
    else:
        array[k] = helper_array[j]
        j += 1
    k += 1
```

- Falls noch Elemente in den untergeordneten Listen übrig sind, werden diese noch zur Hauptliste hinzugefügt.

```python
while i <= mid:
    array[k] = helper_array[i]
    i += 1
    k += 1

while j <= end_idx:
    array[k] = helper_array[j]
    j += 1
    k += 1
```

## ENG

This project will include visualizations of the four most well known algorithms:

1. Mergesort
2. Quicksort
3. Bubblesort
4. Heapsort

### Mergesort

- has a Big O Notation of O(n log n)
- is a sorting algorithm that is based on the _divide and conquer_ principle, which means that the array of numbers to sort will be divided into smaller sub-arrays. This guarantees high performance
- more information: https://en.wikipedia.org/wiki/Mergesort

#### In the code:

- We divide the array of numbers recursively into two subarrays until only one element in the array is left.

```python
if start_idx == end_idx:
    return
mid = (start_idx + end_idx)//2

split_array(helper_array, start_idx, mid, array, animations)
split_array(helper_array, mid + 1, end_idx, array, animations)
```

- We iterate through both subarrays (index i, j) and add the smaller values of these indexes to the main array (index k) until we iterated through at least one of the subarrays.

```python
while i <= mid and j <= end_idx:
    if helper_array[i] <= helper_array[j]:
        array[k] = helper_array[i]
        i += 1
    else:
        array[k] = helper_array[j]
        j += 1
    k += 1
```

- If there are elements left in the subarrays, we'll add them to the main array.

```python
while i <= mid:
    array[k] = helper_array[i]
    i += 1
    k += 1

while j <= end_idx:
    array[k] = helper_array[j]
    j += 1
    k += 1
```
