# Algorithms

## Searching

#### Shortest Palindrome

You are given a string `s`. You can convert `s` to a palindrome[^1] by adding characters in front of it. Return the shortest palindrome you can find by performing this transformation.

```c++
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

string shortestPalindrome(string s) {
  string reversed = string(s.rbegin(), s.rend());
  string superstring = s + ' ' + reversed;
  int m = superstring.length();
  vector<int> lps(m);
  for (int t = 0, j = 1; j < m; lps[j++] = t) {
    while (t && superstring[j] != superstring[t]) t = lps[--t];
    t += superstring[j] == superstring[t];
  }
  return reversed.substr(0, s.length() - lps.back()) + s;
}

```

### Binary Search

#### Median of Two Sorted Arrays

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return *the median* of the two sorted arrays. The overall run time complexity should be $\Theta(\log \min{(m, n)})$.

```python
import bisect

def findMedianSortedArrays(nums1, nums2):
    nums1, nums2 = sorted((nums1, nums2), key=len)
    m, n = len(nums1), len(nums2)
    j = (m + n - 1) // 2 - 1
    i = bisect.bisect_left(range(m),
      True,
      key = lambda x: x > j or nums1[x] >= nums2[j - x])
    j -= i
    median = sorted(nums1[i : i+2] + nums2[j+1 : j+3])
    return (median[0] + median[(m + n) & 1 ^ 1]) / 2

```

#### Find Minimum in Rotated Sorted Array

Suppose an array of length `n` sorted in ascending order is *rotated* between `1` and `n` times. For example, the array `nums = [0, 1, 4, 4, 5, 6, 7]` might become:

- [`4, 5, 6, 7, 0, 1, 4]` if it was rotated `4` times.
- `[0, 1, 4, 4, 5, 6, 7]` if it was rotated `7` times.

Notice that *rotating* an array `[a[0], a[1], a[2], ..., a[n - 1]]` 1 time results in the array `[a[n - 1], a[0], a[1], a[2], ..., a[n - 2]]`. Given the sorted rotated array `nums` that may contain *duplicates*, return the minimum element of this array. You must decrease the overall operation steps as much as possible.

```c++
#include <vector>

using namespace std;

int findMin(vector<int>& nums) {
  int lo = 0, mid, hi = nums.size() - 1;
  while (lo < hi) {
    mid = (lo + hi) >> 1;
    if (nums[mid] > nums[hi]) lo = ++mid;
    else if (nums[mid] < nums[hi]) hi = mid;
    else hi--;
  }
  return nums[lo];
}

```

#### Russian Doll Envelopes

You are given a 2-D array of integers envelopes where `envelopes[i] = [w[i], h[i]]` represents the width and the height of an envelope. One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height. Return the maximum number of envelopes you can Russian doll[^2]. You cannot rotate an envelope.

```python
import bisect

def maxEnvelopes(envelopes):
    lis = []
    for w, h in sorted(envelopes, key = lambda x: (x[0], -x[1])):
        i = bisect.bisect_left(lis, h)
        if i < len(lis): lis[i] = h
        else: lis.append(h)
    return len(lis)

```

## Divide-and-conquer

## Greediness

#### Wildcard Matching

Given an input string `s` and a pattern `p`, implement wildcard pattern matching with support for `?` and `*` where:

- `?` Matches any single character.
- `*` Matches any sequence of characters[^3].

The matching should cover the entire input string[^4].

```c++
#include <string>

using namespace std;

bool isMatch(string s, string p) {
  int i = 0, j = 0, k = 0, asterisk = -1, m = s.size(), n = p.size();
  while (i < m) {
    if (j < n && (p[j] == s[i] || p[j] == '?')) i++, j++;
    else if (j < n && p[j] == '*') k = i, asterisk = j++;
    else if (asterisk != -1) i = ++k, j = asterisk + 1;
    else return false; 
  }
  while (j < n && p[j] == '*') j++;
  return j == n;
}

```

#### Candy

There are `n` children standing in a line. Each child is assigned a rating value given in the integer array `ratings`. You are giving candies to these children subjected to the following requirements:

- Each child must have at least one candy.
- Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.

```c++
#include <algorithm>
#include <vector>

using namespace std;

int candy(vector<int>& ratings) {
  int n = ratings.size();
  vector<int> counter = {0, 0, n};
  for (int i = 1; i < n;) {
    if (ratings[i - 1] != ratings[i]) {
      for (counter[0] = 0;
        i < n && ratings[i - 1] < ratings[i];
        i++, counter[2] += ++counter[0]);
      for (counter[1] = 0;
        i < n && ratings[i - 1] > ratings[i];
        i++, counter[2] += ++counter[1]);
      counter[2] -= min(counter[0], counter[1]);
    }
    else i++;
  }
  return counter[2];
}

```

#### Create Maximum Number

#### Patching Array

Given a sorted integer array `nums` and an integer `n`, add/patch elements to the array such that any number in the range `[1, n]` inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.

```c++
#include <vector>

int minPatches(std::vector<int>& nums, int n) {
  int i = 0, patches = 0;
  for (long m = 1; m <= n; patches++)
    m += i < nums.size() && nums[i] <= m ? nums[i++] : m;
  return patches - i;
}

```

#### Strong Password Checker

#### Find the Closest Palindrome

## Big-O Notation

#### Insert, Delete, GetRandom $\Theta(1)$ - Duplicates Allowed

`RandomizedCollection` is a data structure that contains a collection of numbers, possibly duplicates[^5]. It should support inserting and removing specific elements and also reporting a random element.

Implement the `RandomizedCollection` class:

- `RandomizedCollection()` Initializes the empty `RandomizedCollection` object.
- `bool insert(int val)` Inserts an item `val` into the multiset, even if the item is already present. Returns `true` if the item is not present, `false` otherwise.
- `bool remove(int val)` Removes an item `val` from the multiset if present. Returns `true` if the item is present, `false` otherwise. Note that if `val` has multiple occurrences in the multiset, we only remove one of them.
- `int getRandom()` Returns a random element from the current multiset of elements. The probability of each element being returned is *linearly related* to the number of the same values the multiset contains.

You must implement the functions of the class such that each function works in $\Theta(1)$ time complexity. `getRandom` will only be called if there is *at least one* item in the `RandomizedCollection`.

```python
import collections
import random

class RandomizedCollection:
    def __init__(self):
        self.vals = []
        self.val_index = collections.defaultdict(list)

    def insert(self, val):
        self.vals.append((val, len(self.val_index[val])))
        self.val_index[val].append(len(self.vals) - 1)
        return len(self.val_index[val]) == 1

    def remove(self, val):
        if self.val_index[val]:
            i = self.val_index[val].pop()
            last = last_val, last_index = self.vals.pop()
            if i < len(self.vals):
                self.vals[i] = last
                self.val_index[last_val][last_index] = i
            return True
        return False

    def getRandom(self):
        return random.choice(self.vals)[0]

```

## Dijkstra's

## A\*

[^1]: A *palindrome* is a string that reads the same forward and backward.
[^2]: put one inside the other
[^3]: including the empty sequence
[^4]: not partial
[^5]: a multiset
