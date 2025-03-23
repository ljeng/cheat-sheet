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
    return (median[0] + median[(m + n) % 2 ^ 1]) / 2

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
- `*` Matches any sequence of characters[^2].

The matching should cover the entire input string[^3].

```c++
#include <string>

using namespace std;

bool isMatch(string s, string p) {
  int i = 0, j = 0, k = 0, asterisk = -1;
  int m = s.size(), n = p.size();
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

#### Create Maximum Number

#### Strong Password Checker

#### Find the Closest Palindrome

## Big-O Notation

## Dijkstra's

## A\*

[^1]: A *palindrome* is a string that reads the same forward and backward.
[^2]: put one inside the other
[^3]: including the empty sequence
[^4]: not partial
