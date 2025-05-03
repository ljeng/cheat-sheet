# Algorithms

## Searching

**Knuth-Morris-Pratt**

```c++
#include <string>
#include <vector>

using namespace std;

vector<int> KnuthMorrisPratt(string pattern, string text) {
  int j, m = pattern.length(), t = 0, k = 0, n = text.length();
  vector<int> lps(m + 1);
  for (j = 1; j < m; lps[++j] = t) {
    while (t && pattern[j] != pattern[t]) t = lps[t];
    t += pattern[j] == pattern[t];
  }
  j = 0;
  vector<int> matches;
  while (k < n) {
    while (j && text[k] != pattern[j]) j = lps[j];
    j += text[k++] == pattern[j];
    if (j == m) {
      matches.push_back(k - j);
      j = lps[j];
    }
  }
  return matches;
}

```

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

- `[4, 5, 6, 7, 0, 1, 4]` if it was rotated `4` times.
- `[0, 1, 4, 4, 5, 6, 7]` if it was rotated `7` times.

Notice that *rotating* an array `[a[0], a[1], a[2], ..., a[n - 1]]` 1 time results in the array `[a[n - 1], a[0], a[1], a[2], ..., a[n - 2]]`. Given the sorted rotated array `nums` that may contain *duplicates*, return the minimum element of this array. You must decrease the overall operation steps as much as possible.

```c++
#include <vector>

int findMin(std::vector<int>& nums) {
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
#### Max Sum of Rectangle No Larger than `k`

Given an `m * n` matrix `matrix` and an integer `k`, return the max sum of a rectangle in the matrix such that its sum is no larger than `k`. It is *guaranteed* that there will be a rectangle with a sum no larger than `k`.

```c++
#include <algorithm>
#include <climits>
#include <set>
#include <vector>

using namespace std;

int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
  int m = matrix.size(), n = matrix[0].size(), max_sum = INT_MIN;
  for (int j1 = 0; j1 < n; j1++) {
    vector<int> prefix(m);
    for (int j2 = j1; j2 < n; j2++) {
      for (int i = 0; i < m; i++) prefix[i] += matrix[i][j2];
      set<int> sums;
      sums.insert(0);
      int current = 0, current_max = INT_MIN;
      for (int x : prefix) {
        current += x;
        auto it = sums.lower_bound(current - k);
        if (it != sums.end()) current_max = max(current_max, current - *it);
        sums.insert(current);
      }
      max_sum = max(max_sum, current_max);
    }
  }
  return max_sum;
}
```

# Find `k`th Smallest Pair Distance

The *distance of a pair* of integers `a` and `b` is defined as the absolute difference between `a` and `b`. Given an integer array `nums` and an integer `k`, return the `k`<sup>th</sup> smallest *distance among all the pairs* `nums[i]` and `nums[j]` where `0 <= i < j < nums.length`.

```c++
#include <algorithm>
#include <vector>

using namespace std;

int smallestDistancePair(vector<int>& nums, int k) {
  sort(nums.begin(), nums.end());
  int n = nums.size();
  int lo = 0, hi = nums[n - 1] - nums[0];
  while (lo < hi) {
    int mid = (lo + hi) >> 1;
    int distance = -n;
    for (int i = 0, j = 0; i < n; i++) {
      while (j < n && nums[j] <= nums[i] + mid) j++;
      distance += j - i;
    }
    if (distance < k) lo = ++mid;
    else hi = mid;
  }
  return lo;
}

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

#### Text Justification

Given an array of strings `words` and a width `maxWidth`, format the text such that each line has exactly `maxWidth` characters and is fully[^5] justified. You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces `' '` when necessary so that each line has exactly `maxWidth` characters. Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right. The last line of text should be left-justified, and no extra space is inserted between words.

- A word is defined as a character sequence consisting of non-space characters only.
- Each word's length is guaranteed to be greater than `0` and not exceed `maxWidth`.
- The input array `words` contains at least one word.

```python
def fullJustify(words, maxWidth):
    n = width = 0
    line = []
    justified = []
    for word in words:
        k = len(word)
        if n + width + k > maxWidth:
            if n > 1:
                n -= 1
                div, mod = divmod(maxWidth - width, n)
                spaces = [div] * n
                for i in range(mod): spaces[i] += 1
                spaces.append(0)
                justified.append(''.join(word + space * ' '
                    for word, space in zip(line, spaces)))
            else: justified.append(line[0].ljust(maxWidth))
            n = width = 0
            line = []
        n += 1
        width += k
        line.append(word)
    return justified + [' '.join(line).ljust(maxWidth)]

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
  int i = 1, n = ratings.size();
  int counter[3] = {0, 0, n};
  while (i < n) {
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

`RandomizedCollection` is a data structure that contains a collection of numbers, possibly duplicates[^6]. It should support inserting and removing specific elements and also reporting a random element.

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
[^5]: left and right
[^6]: a multiset
