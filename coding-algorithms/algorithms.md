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
  int t = 0, j = 1;
  lps[0] = 0;
  while (j < m) {
    while (t && superstring[j] != superstring[t]) t = lps[--t];
    t += superstring[j] == superstring[t];
    lps[j++] = t;
  }
  return reversed.substr(0, s.length() - lps.back()) + s;
}

```

### Binary Search

#### Median of Two Sorted Arrays

## Divide-and-conquer

## Greediness

#### Wildcard Matching

Given an input string `s` and a pattern `p`, implement wildcard pattern matching with support for `?` and `*` where:

- `?` Matches any single character.
- `*` Matches any sequence of characters[^2].

The matching should cover the entire input string (not partial).

```c++
#include <string>

using namespace std;

bool isMatch(string s, string p) {
  int m = s.size(), n = p.size();
  int i = 0, j = 0, k = 0, asterisk = -1;
  while (i < m) {
    if (j < n && p[j] == s[i] || p[j] == '?') i++, j++;
    else if (j < n && p[j] == '*') asterisk = j++, k = i;
    else if (asterisk != -1) j = asterisk + 1, i = ++k;
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
[^2]: including the empty sequence
