# Recursion

#### Regular Expression Matching

#### Scramble String

#### Palindrome Partitioning

Given a string `s`, partition `s` such that every substring[^1] of the partition is a palindrome[^2]. Return the *minimum* cuts needed for a palindrome partitioning of `s`.

```c++
#include <algorithm>
#include <string>
#include <vector>

int minCut(string s) {
  int n = s.size();
  vector<int> cut(n + 1);
  for (int i = 0; i <= n; i++) cut[i] = i;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j <= i && i + j < n && s[i - j] == s[i + j]; j++)
      cut[i + j + 1] = min(cut[i + j + 1], cut[i - j] + 1);
    for (int j = 1; j - 1 <= i && i + j < n && s[i - j + 1] == s[i + j]; j++)
      cut[i + j + 1] = min(cut[i + j + 1], cut[i - j + 1] + 1);
  }
  return cut[n];
}

```

#### Dungeon Game

#### Russian Doll Envelopes

#### Zuma Game

[^1]: A *substring* is a contiguous *non-empty* sequence of characters within a string.
[^2]: A *palindrome* is a string that reads the same forward and backward.
