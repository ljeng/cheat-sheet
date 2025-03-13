# Sorting

## Table of Contents

- [Insertion Sort](#insertion-sort)
- [Radix Sort](#radix-sort)
- [Quicksort](#quicksort)
    - [Quickselect](#quickselect)
- [Merge Sort](#merge-sort)
- [Heapsort](#heapsort)

#### First Missing Positive

#### Contains Duplicate

## Insertion Sort

## Radix Sort

```python
import math
import itertools


def radix_sort(arr, w):
    # w is the number of buckets
    for i in range(int(round(math.log(max(map(abs, arr)), w)) + 1)):
        buckets = [[] for j in range(w)]
        for element in arr: buckets[element//w**i%w] += [element]
        arr = list(itertools.chain(*buckets))
    return [element for element in arr if element < 0] + [element for element in arr if element >= 0]
```

## Quicksort

### Quickselect

```python
def quickselect(arr, k):
    smaller, larger = [element for element in arr if element < arr[0]], [element for element in arr if element > arr[0]]
    n = len(arr) - len(larger)
    if k <= len(smaller): return quickselect(smaller, k)
    elif k > n: return quickselect(larger, k - n)
    else: return arr[0]
```

## Merge Sort

#### Reverse Pairs

#### Count of Smaller Numbers After Self

## Heapsort
