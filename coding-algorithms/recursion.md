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
  for (int i = 0; i <= n; i++) cut[i] = i - 1;
  for (int i = 0; i < n; i++)
    for (int k = 0; k < 2; k++)
      for (int j = k; j < min(i + k + 1, n - i) && s[i - j + k] == s[i + j];)
        cut[i + ++j] = min(cut[i + j + 1], cut[i - j + k] + 1);
  return cut[n];
}

```

#### Dungeon Game

The demons had captured the princess and imprisoned her in *the bottom-right corner* of a `dungeon`. The `dungeon` consists of `m * n` rooms laid out in a 2D grid. Our valiant knight was initially positioned in *the top-left room* and must fight his way through `dungeon` to rescue the princess. The knight has an initial health point represented by a positive integer. If at any point his health point drops to `0` or below, he dies immediately. Some of the rooms are guarded by demons[^3], so the knight loses health upon entering these rooms; other rooms are either empty[^4] or contain magic orbs that increase the knight's health[^5]. To reach the princess as quickly as possible, the knight decides to move only *rightward* or *downward* in each step. Return the knight's minimum initial health so that he can rescue the princess. *Note* that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

```c++
#include <algorithm>
#include <climits>
#include <vector>

using namespace std;

int calculateMinimumHP(vector<vector<int>>& dungeon) {
  int m = dungeon.size(), n = dungeon[0].size();
  vector<vector<int>> dp(2, vector<int>(n + 1, INT_MAX));
  dp[0][--n] = 1;
  for (int i = --m; i >= 0; i--) {
    swap(dp[0], dp[1]);
    for (int j = n; j >= 0; j--)
      dp[0][j] = max(min(dp[1][j], dp[0][j + 1]) - dungeon[i][j], 1);
  }
  return dp[0][0];
}

```

#### Russian Doll Envelopes

#### Zuma Game

[^1]: A *substring* is a contiguous *non-empty* sequence of characters within a string.
[^2]: A *palindrome* is a string that reads the same forward and backward.
[^3]: represented by negative integers
[^4]: represented as 0
[^5]: represented by positive integers
