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

```cpp
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

## [Insertion Sort](code/sorting.cpp#L7)

```cpp
#include <algorithm>
#include <vector>

using namespace std;

void InsertionSort(vector<int>& a) {
  for (int i = 1; i < a.size(); i++)
    for (int j = i; j && a[j - 1] > a[j]; swap(a[j], a[--j]));
}

```

## [Radix Sort](code/sorting.py)

```python
from itertools import chain
import math

def radixSort(array, w):
    for i in range(int(round(math.log(max(map(abs, arr)), w)) + 1)):
        buckets = [[] for _ in range(w)]
        for element in array: buckets[element // w**i % w].append(element)
        array = list(chain(*buckets))
    concatenated_buckets = [[], []]
    for element in array: concatenated_buckets[element > 0].append(element)
    return list(chain(*concatenated_buckets))

```

## [Quicksort](code/sorting.cpp#L12)

```c++
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

void Quicksort(vector<int>& a) {
  stack<pair<int, int>> ranges;
  ranges.emplace(0, a.size() - 1);
  int i, j;
  while (!ranges.empty()) {
    auto [lo, hi] = ranges.top();
    ranges.pop();
    if (lo < hi) {
      for (i = lo - 1, j = lo; j < hi; j++)
        if (a[j] < a[hi])
          swap(a[++i], a[j]);
      swap(a[++i], a[hi]);
      ranges.emplace(lo, i - 1);
      ranges.emplace(i + 1, hi);
    }
  }
}

```

### Quickselect

```python
def quickselect(arr, k):
    smaller, larger = [element for element in arr if element < arr[0]], [element for element in arr if element > arr[0]]
    n = len(arr) - len(larger)
    if k <= len(smaller): return quickselect(smaller, k)
    elif k > n: return quickselect(larger, k - n)
    else: return arr[0]
```

## [Merge Sort](code/sorting.cpp#L30)

```cpp
#include <algorithm>
#include <vector>

using namespace std;

void MergeSort(vector<int>& a) {
  int n = a.size();
  vector<int> b(n);
  int k;
  for (int width = 1; width < n; width *= 2) {
    for (int start = 0; start < n; start += 2 * width) {
      int mid = min(start + width, n), end = min(start + 2 * width, n);
      int left = start, right = mid;
      for (k = start;
         left < mid && right < end;
         b[k++] = a[left] > a[right] ? a[right++] : a[left++]);
      while (left < mid) b[k++] = a[left++];
      while (right < end) b[k++] = a[right++];
    }
    copy(b.begin(), b.end(), a.begin());
  }
}

```

#### Reverse Pairs

Given an integer array `nums`, return the number of *reverse pairs* in the array. A *reverse pair* is a pair `(i, j)` where:

- `0 <= i < j < nums.length` and
- `nums[i] > 2 * nums[j]`.

```cpp
#include <algorithm>
#include <vector>

using namespace std;

int reversePairs(vector<int>& nums) {
  int n = nums.size(), i, j, counter = 0;
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

```python
import sortedcontainers

def reversePairs(nums):
    sorted_nums = sortedcontainers.SortedList(key=lambda x: -x)
    counter = 0
    for num in nums:
        counter += sorted_nums.bisect_left(2 * num)
        sorted_nums.add(num)
    return counter

```

#### Count of Smaller Numbers after Self

Given an integer array `nums`, return an integer array `counts` where `counts[i]` is the number of smaller elements to the right of `nums[i]`.

```cpp
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

vector<int> countSmaller(vector<int>& nums) {
  int n = nums.size();
  vector<pair<int, int>> index_num(n);
  for (int i = 0; i < n; i++) index_num[i] = make_pair(i, nums[i]);
  vector<int> counts(n--);
  for (int m = 1; m <= n; m *= 2) for (int lo = 0; lo <= n; lo += 2 * m) {
    int mid = min(lo + m - 1, n), hi = min(lo + 2 * m - 1, n);
    if (mid < hi) {
      int i = lo, j = ++mid;
      int count = 0;
      vector<pair<int, int>> merge;
      while (i < mid && j <= hi) {
        if (index_num[i].second > index_num[j].second) {
          count++;
          merge.push_back(index_num[j++]);
        }
        else {
          counts[index_num[i].first] += count;
          merge.push_back(index_num[i++]);
        }
      }
      while (i < mid) {
        counts[index_num[i].first] += count;
        merge.push_back(index_num[i++]);
      }
      copy(merge.begin(), merge.end(), index_num.begin() + lo);
    }
  }
  return counts;
}

```

```python
import sortedcontainers

def countSmaller(nums):
    n = len(nums)
    sorted_nums = sortedcontainers.SortedList()
    counts = [0] * n
    for i in reversed(range(n)):
        counts[i] = sorted_nums.bisect_left(nums[i])
        sorted_nums.add(nums[i])
    return counts

```

## [Heapsort](code/sorting.cpp#L48)

```cpp
#include <algorithm>
#include <vector>

using namespace std;

void HeapSort(vector<int>& a) {
  int count = a.size();
  int start = count >> 1, end = count;
  while (end > 1) {
    if (start) start--;
    else swap(a[0], a[--end]);
    int root = start;
    while (true) {
      int child = 2 * root;
      if (++child >= end) break;
      child += child + 1 < end && a[child] < a[child + 1];
      if (a[root] < a[child]) {
        swap(a[root], a[child]);
        root = child;
      }
      else break;
    }
  }
}

```
