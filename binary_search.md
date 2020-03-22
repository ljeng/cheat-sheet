## binary_search

[binary_search.**binary_search**(*function*, *lo*, *hi*)](/binary_search.py)

Finds the first index `i` where `lo <= i <= hi` that satisfies `function`.

Examples:

[Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays)
```python
def findMedianSortedArrays(nums1, nums2):
    def median(a, b, extrema):
        k, half = -1 if extrema == max else 0, []
        if a: half += [nums2[j + k]]
        if b: half += [nums1[i + k]]
        return extrema(half)
    nums1, nums2 = sorted([nums1, nums2], key = len)
    m, n = len(nums1), len(nums2)
    full_len = m + n
    half_len = (full_len + 1)//2
    function = lambda x: x and nums1[x - 1] > nums2[half_len - x]
    i = binary_search(function, 0, m)
    j = half_len - i
    median_low = median(i, j, max)
    if full_len%2: return median_low
    else: return (median_low + median(i == m, j == n, min))/2
```

[Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array)
```python
def search(nums, target):
    if nums:
        n = len(nums)
        m = n - 1
        i = binary_search(lambda x: nums[x - 1] > nums[x], 0, m)
        j = binary_search(lambda y: nums[y%n] == target, i, i + m)%n
        return j if nums[j] == target else -1
    return -1
```

[Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array)
```python
def searchRange(nums, target):
    if nums:
        n = len(nums) - 1
        i = binary_search(lambda x: nums[x] >= target, 0, n - 1)
        if nums[i] == target:
            j = binary_search(lambda y: nums[y] > target, i, n) - 1
            return [i, j]
        else: return [-1, -1]
    return [-1, -1]
```

[Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix)
```python
def searchMatrix(matrix, target):
    m = len(matrix[0])
    function = lambda x: matrix[x//m][x%m] >= target
    i = binary_search(function, 0, len(matrix)*m - 1)
    return matrix[i//m][i%m] == target
```


[Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii)
```python
def search(nums, target):
    if nums:
        n = len(nums)
        m = n - 1
        lo, hi = 0, m
        while lo < n and nums[lo] == nums[0]: lo += 1
        while hi and nums[hi] == nums[-1]: hi -= 1
        i = binary_search(lambda x: nums[x - 1] > nums[x], lo, hi)
        j = binary_search(lambda y: nums[y%n] >= target, i, i + m)%n
        return nums[j] == target
    return False
```

[Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array)
```python
def findMin(nums):
    function = lambda x: nums[x - 1] > nums[x]
    i = binary_search(function, 0, len(nums) - 1)
    return nums[i]
```

[Find Peak Element](https://leetcode.com/problems/find-peak-element)
```python
def findPeakElement(nums):
    n = len(nums)
    if n > 2:
        function = lambda x: nums[x - 1] < nums[x] > nums[x + 1]
        i = binary_search(function, 1, n - 2)
        return nums[i]
    else: return max(nums)
```

[H-Index II](https://leetcode.com/problems/h-index-ii)
```python
def hIndex(citations):
    n = len(citations)
    function = lambda x: citations[x] >= n - x
    return binary_search(function, 0, n - 1)
```

[Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence)
```python
def lengthOfLIS(nums):
    tails, size = [0]*len(nums), 0
    for num in nums:
        i = binary_search(lambda x: tails[x] >= x)
        tails[i], size = num, max(size, i + 1)
    return size
```

[Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square)
```python
def isPerfectSquare(num):
    return binary_search(lambda x: x**2 >= num, 1, num)**2 == num
```

[Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum)
```python
def splitArray(nums, m):
    def valid(target):
        subarray_sum = counter = 0
        for num in nums:
            subarray_sum += num
            if subarray_sum > target:
                subarray_sum = num
                counter += 1
                if counter >= m: return False
        return True
    array_sum = sum(nums)
    if m > 1: return binary_search(valid, max(nums), array_sum)
    else: return array_sum
```

[Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas)
```python
def minEatingSpeed(piles, H):
    def can_eat(K):
        hours = 0
        for pile in piles:
            hours += pile//K
            if pile%K: hours += 1
        return hours <= H
    return binary_search(can_eat, 1, max(piles))
```

[Find Positive Integer Solution for a Given Equation](https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation)
```python
def findSolution(customfunction, z):
    lo, hi, pairs = 1, 1001, []
    for x in range(1, 1001):
        if not customfunction.f(x, lo) < customfunction.f(x, hi) < z:
            y = binary_search(lambda b: customfunction.f(x, b) >= z, lo, hi)
            value = customfunction.f(x, y)
            if value >= z:
                if value == z: pairs += [[x, y]]
                hi = y
            else: lo = y
    return pairs
```

[Find the Smallest Divisor Given a Threshold](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold)
```python
def smallestDivisor(nums, threshold):
    function = lambda x: sum((i + x - 1)//x for i in nums) <= threshold
    return binary_search(function, 1, max(nums))
```
