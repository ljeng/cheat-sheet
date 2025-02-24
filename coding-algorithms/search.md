## Search

### [search.**binary**(*lo*, *hi*, *function*)](/search.py)

Find the first index `i` where `lo <= i <= hi` that satisfies `function`.

[Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays)
```python
def findMedianSortedArrays(nums1, nums2):

    def median(a, b, extrema):
        k = -1 * (extrema == max)
        half = []
        if a:
            half += [nums2[j + k]]
        if b:
            half += [nums1[i + k]]
        return extrema(half)

    nums1, nums2 = sorted([nums1, nums2], key=len)
    m, n = len(nums1), len(nums2)
    sum_len = m + n
    mean_len = (sum_len + 1)//2
    i = binary(0, m,
        lambda x: x and nums1[x - 1] > nums2[mean_len - x]
    )
    j = sum_len - i
    return median_low if sum_len%2 else (median_low
        + median(i == m, j == n, min)
    )/2
```

[Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array)
```python
def search(nums, target):
    if nums:
        n = len(nums)
        m = n - 1
        i = binary(0, m, lambda x: nums[x - 1] > nums[x])
        j = binary(i, i + m, lambda y: nums[y%n] == target)%n
        return j if nums[j] == target else -1
    return -1
```

[Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array)
```python
def searchRange(nums, target):
    if nums:
        n = len(nums) - 1
        i = binary(0, n - 1, lambda x: nums[x] >= target)
        if nums[i] == target:
            j = binary(i, n, lambda y: nums[y] > target) - 1
            return [i, j]
        else:
            return [-1, -1]
    return [-1, -1]
```

[Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix)
```python
def searchMatrix(matrix, target):
    m = len(matrix[0])
    i = binary(0, len(matrix)*m - 1,
        lambda x: matrix[x//m][x%m] >= target
    )
    return matrix[i//m][i%m] == target
```


[Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii)
```python
def search(nums, target):
    if nums:
        n = len(nums)
        m = n - 1
        lo, hi = 0, m
        while lo < n and nums[lo] == nums[0]:
            lo += 1
        while hi and nums[hi] == nums[-1]:
            hi -= 1
        i = binary(lo, hi, lambda x: nums[x - 1] > nums[x])
        return nums[binary(i, i + m,
            lambda y: nums[y%n] >= target
        )%n] == target
    return False
```

[Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array)
```python
def findMin(nums):
    return nums[binary(0, len(nums) - 1,
        lambda x: nums[x - 1] > nums[x]
    )]
```

[Find Peak Element](https://leetcode.com/problems/find-peak-element)
```python
def findPeakElement(nums):
    n = len(nums)
    if n > 2:
        i = binary(1, n - 2,
            lambda x: nums[x - 1] < nums[x] > nums[x + 1]
        )
        return nums[i]
    else:
        return max(nums)
```

[H-Index II](https://leetcode.com/problems/h-index-ii)
```python
def hIndex(citations):
    n = len(citations)
    return binary(0, n - 1, lambda x: citations[x] >= n - x)
```

[Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence)
```python
def lengthOfLIS(nums):
    tails, size = [0]*len(nums), 0
    for num in nums:
        i = binary(0, size, lambda x: tails[x] >= num)
        tails[i], size = num, max(i + 1, size)
    return size
```

[Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square)
```python
def isPerfectSquare(num):
    return binary(1, num, lambda x: x**2 >= num)**2 == num
```

[Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum)
```python
def splitArray(nums, m):

    def is_valid(target):
        subarray_sum = counter = 0
        for num in nums:
            subarray_sum += num
            if subarray_sum > target:
                subarray_sum = num
                counter += 1
                if counter >= m: return False
        return True

    array_sum = sum(nums)
    return binary(max(nums), is_valid(array_sum)
    ) if m > 1 else array_sum
```

[Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas)
```python
def minEatingSpeed(piles, H):

    def can_eat(K):
        hours = 0
        for pile in piles:
            hours += pile//K
            if pile%K:
                hours += 1
        return hours <= H

    return binary(1, max(piles), can_eat)
```

[Find Positive Integer Solution for a Given Equation](https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation)
```python
def findSolution(customfunction, z):
    lo, hi = 1, 1001
    pairs = []
    for x in range(1, 1001):
        if not customfunction.f(x, lo) < customfunction.f(x, hi) < z:
            y = binary(lo, hi, lambda b: customfunction.f(x, b) >= z)
            value = customfunction.f(x, y)
            if value >= z:
                if value == z: pairs += [[x, y]]
                hi = y
            else:
                lo = y
    return pairs
```

[Find the Smallest Divisor Given a Threshold](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold)
```python
def smallestDivisor(nums, threshold):
    return binary(1, max(nums),
        lambda x: sum((i + x - 1)//x for i in nums) <= threshold
    )
```

### [search.**rabin_karp**(*pattern*, *s*)](/search.py)
Apply the Rabin-Karp algorithm to an input string given a pattern. Return an array of match indices.

[Implement strStr()](https://leetcode.com/problems/implement-strstr)
```python
def strStr(haystack, needle):
	m = search.rabin_karp(needle, haystack)
	return m[0] if m else -1
```
