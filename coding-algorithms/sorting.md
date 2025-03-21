# Sorting

## Table of Contents

- [Insertion Sort](#insertion-sort)
- [Radix Sort](#radix-sort)
- [Quicksort](#quicksort)
    - [Quickselect](#quickselect)
- [Merge Sort](#merge-sort)
- [Heapsort](#heapsort)

#### First Missing Positive

Given an unsorted integer array `nums`. Return the smallest positive integer that is not present in `nums`. You must implement an algorithm that runs in $\Theta(n)$ time and uses $\Theta(1)$ auxiliary space.

```c++
#include <algorithm>
#include <vector>

using namespace std;

int firstMissingPositive(vector<int>& nums) {
  int n = nums.size();
  for (int i = 0; i < n; i++)
    while (0 < nums[i] && nums[i] <= n && nums[i] != nums[nums[i] - 1])
      swap(nums[i], nums[nums[i] - 1]);
  for (int i = 1; i <= n; i++) if (i != nums[i - 1]) return i;
  return ++n;
}

```

#### Contains Duplicate

You are given an integer array nums and two integers `indexDiff` and `valueDiff`. Find a pair of indices `(i, j)` such that:

- `i != j`
- `abs(i - j) <= indexDiff`
- `abs(nums[i] - nums[j]) <= valueDiff`

Return `true` if such pair exists or `false` otherwise.

```python
import collections
import sys

def containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff):
    valueDiff += 1
    buckets = collections.defaultdict(lambda: sys.maxsize)
    for i, num in enumerate(nums):
        k = num // valueDiff
        if buckets[k] < sys.maxsize or min(abs(num - buckets[k - 1]),
            abs(num - buckets[k + 1])) < valueDiff:
            return True
        buckets[k] = num
        if i >= indexDiff: del buckets[nums[i - indexDiff] // valueDiff]
    return False

```

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

Given an integer array `nums`, return the number of *reverse pairs* in the array. A *reverse pair* is a pair `(i, j)` where:

- `0 <= i < j < nums.length` and
- `nums[i] > 2 * nums[j]`.

```c++
#include <algorithm>
#include <vector>

using namespace std;

int reversePairs(vector<int>& nums) {
  int n = nums.size();
  int i, j;
  int counter = 0;
  for (int width = 1; width < n; width *= 2)
    for (int start = 0; start < n; start += 2 * width) {
      int mid = start + width - 1;
      int end = min(width + mid, n - 1);
      if (mid >= n) break;
      j = ++mid;
      for (i = start; i < mid; i++) {
        while (j <= end && nums[i] > 2LL * nums[j]) j++;
        counter += j - mid;
      }
      i = start, j = mid;
      vector<int> merged;
      while (i < mid && j <= end)
        merged.push_back(nums[i] > nums[j] ? nums[j++] : nums[i++]);
      while (i < mid) merged.push_back(nums[i++]);
      while (j <= end) merged.push_back(nums[j++]);
      copy(merged.begin(), merged.end(), nums.begin() + start);
    }
  return counter;
}

```

#### Count of Smaller Numbers After Self

## Heapsort
