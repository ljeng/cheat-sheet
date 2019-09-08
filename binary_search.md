### Index of First True
Given a range of elements sorted by a boolean key, `index_of_first` finds the first index in a range that satisfies a user-specified condition. The basic implementation:
```python
import bisect


class A:
	def __getitem__(self, k):
		# write your condition here


def index_of_first(start, end): return bisect.bisect_left(A(), True, start, end)
```
#### Example 1
A mountain is a list of numbers with the following properties:
* The length of the list is at least 3.
* The numbers strictly increase until some index *i* which is the peak, and then they strictly decrease.
Given a list that's definitely a mountain, return the index of the peak.

We will modify the basic implementation to solve this problem.
```python
import bisect

def peak_index(mountain):

	class Range:
		def __getitem__(self, k): return mountain[k] > mountain[k + 1]

	def index_of_first(start, end): return bisect.bisect_left(A(), True, start, end)

	return index_of_first(1, len(mountain) - 2)
	
```
We have a mountain:

| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mountain | 40 | 48 | 61 | 75 | 100 | 99 | 98 | 39 | 30 | 10 |

We create a boolean list that returns whether `mountain[k] > mountain[k + 1]` for `k` in range `start = 1, end = len(mountain) - 2`.

| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mountain | 40 | 48 | 61 | 75 | 100 | 99 | 98 | 39 | 30 | 10 |
| `mountain[k] > mountain[k + 1]` | | False | False | False | True | True | True | True | True | |

When we call `bisect.bisect_left`, it returns the index of the first `True` value.
#### Example 2
You're a product manager leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad. Suppose you have *n* versions `[0, 1...n - 1]` and you want to find out the first bad one, which causes all the following ones to be bad. You're given an API `is_bad(version)` which will return whether `version` is bad. Implement a function to find the first bad version.

Solution:
```python
import bisect

def first_bad_version(n):

	class A:
		def __getitem__(self, k): return is_bad(k + 1)

	def index_of_first(start, end): return bisect.bisect_left(A(), True, start, end) + 1

	return index_of_first(0, n - 1)
	
```
Time complexity: O(log *n*)

Space complexity: O(1)