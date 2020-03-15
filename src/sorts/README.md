# Sorting Algorithms

## DE

In diesem Sorting-Visualizer sind die bekanntesten Sortieralgorithmen implementiert:

1. Mergesort
2. Quicksort
3. Bubblesort

### Mergesort

- hat eine Big O (Performance) Notation von O(n log n)
- ist ein Sortieralgorithmus der auf _divide and conquer_ -also teilen und herrschen- basiert. Das heißt, dass die zu sortierende Zahlenfolge immer wieder geteilt wird. So kann höhere Leistung garantiert werden.
- weitere [Informationen](https://de.wikipedia.org/wiki/Mergesort)

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

### Quicksort

- hat eine durchschnittliche Big O (Performance) Notation von O(n log n), im schlechtesten Fall aber O(n²)
- ist ein Sortieralgorithmus der auf _divide and conquer_ -also teilen und herrschen- basiert. Das heißt, dass die zu sortierende Zahlenfolge immer wieder geteilt wird. So kann höhere Leistung garantiert werden.
- weitere [Informationen](https://de.wikipedia.org/wiki/Quicksort)

#### Im Code:

- Wir führen den eigentlichen Algorithmus in der Liste durch; danach wird der Prozess jeweils mit der linken und rechten Hälfte rekursiv wiederholt.

```python
part_idx = make_partition(array, start_idx, end_idx)
quick_sort(array, start_idx, part_idx-1)
quick_sort(array, part_idx+1, end_idx)
```

- In dieser Version des Quicksort nehmen wir das erste Element als Pivot.

```python
pivot = array[start_idx]
```

- Wir iterieren rückwärts durch die Liste bis sich die beiden Vergleichs-Indexe überschnitten haben oder der größere Index (high) ein Element an seiner Stelle hat, das kleiner als das Pivot ist.

```python
while low <= high and array[high] >= pivot:
    high -= 1
```

- Wir iterieren durch die Liste bis sich die beiden Vergleichs-Indexe überschnitten haben oder der kleiner Index (low) ein Element an seiner Stelle hat, das größer als das Pivot ist.

```python
while low <= high and array[low] <= pivot:
    low += 1
```

- Wenn die beide Indexe sich noch nicht überschnitten haben, tauschen wir deren Werte.

```python
if low < high:
    array[low], array[high] = array[high], array[low]
```

- Anschließend tauschen wir das Pivot-Element und der größeren Index high. Dies hat zur Folge, dass alle Werte links des Pivot-Elements kleiner und alle rechts des Pivot-Elements größer als es selbst sind.Anschließend geben wir den Index des Pivot-Elements zurück, den wir für die Rekursion benötigen.

```python
array[start_idx], array[high] = array[high], array[start_idx]
return high
```

## ENG

This project includes visualizations of the most well known algorithms:

1. Mergesort
2. Quicksort
3. Bubblesort

### Mergesort

- has a Big O Notation of O(n log n)
- is a sorting algorithm that is based on the _divide and conquer_ principle, which means that the array of numbers to sort will be divided into smaller sub-arrays. This guarantees high performance
- more [information](https://en.wikipedia.org/wiki/Mergesort)

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

### Quicksort

- has an average Big O Notation of O(n log n), in the worst case it is O(n²)
- is a sorting algorithm based on the _divide and conquer_ principle, which means that the array of numbers to sort will be divided into smaller sub-arrays. This guarantees high performance
- weitere [Informationen](https://en.wikipedia.org/wiki/Quicksort)

#### In the code:

- We perform the actual algorithm; after that we repeat the process recursively with the left and right half until there's only one element left in the array.

```python
part_idx = make_partition(array, start_idx, end_idx)
quick_sort(array, start_idx, part_idx-1)
quick_sort(array, part_idx+1, end_idx)
```

- In this version of the quicksort, we pick the first element of the given array as the pivot

```python
pivot = array[start_idx]
```

- We iterate through the array backwards until the both indices which we are comparing surpassed eachother or until the bigger index (high) has an element at its position, which is smaller than the pivot.

```python
while low <= high and array[high] >= pivot:
    high -= 1
```

- We iterate through the array until the both indices which we are comparing surpassed eachother or until the smaller index (low) has an element at its position, which is bigger than the pivot.

```python
while low <= high and array[low] <= pivot:
    low += 1
```

- If the two indices didn't bypass eachother, we swap them.

```python
if low < high:
    array[low], array[high] = array[high], array[low]
```

- After that, we swap the pivot element and the bigger index. This guarantuees that every element left of the pivot is smaller than itself and every element to the right is bigger. Then, we return the bigger index(now where the pivot is), which we need for the recursion.

```python
array[start_idx], array[high] = array[high], array[start_idx]
return high
```
