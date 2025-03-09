# Algorithms

## Searching

#### Shortest Palindrome

You are given a string `s`. You can convert `s` to a palindrome[^1] by adding characters in front of it. Return the shortest palindrome you can find by performing this transformation.

```c++
#include <algoithm>
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
    while (t && superstring[j] != superstring[t]) t = lps[t - 1];
    if (superstring[j] == superstring[t]) t++;
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

#### Create Maximum Number

#### Strong Password Checker

#### Find the Closest Palindrome

## Big-O Notation

## Dijkstra's

## A\*

[^1]: A *palindrome* is a string that reads the same forward and backward.
