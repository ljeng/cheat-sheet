# Recursion

#### Regular Expression Matching

Given an input string `s` and a pattern `p`, implement regular expression matching with support for `.` and `*` where:

- `.` matches any single character.
- `*` matches zero or more of the preceding element.

The matching should cover the entire input string[^1].

```c++
#include <string>
#include <vector>

using namespace std;

bool isMatch(string s, string p) {
  int m = s.length(), n = p.length();
  vector<vector<int>> is_match(m + 1, vector<int>(n + 1));
  is_match[0][0] = true;
  for (int j = 0; j < n; j++)
    is_match[0][j + 1] = p[j] == '*' && is_match[0][j - 1];
  for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) {
    if (p[j] == s[i] || p[j] == '.') is_match[i + 1][j + 1] = is_match[i][j];
    else if (p[j] == '*') {
      is_match[i + 1][j + 1] = is_match[i + 1][j - 1];
      is_match[i + 1][j + 1] |= (p[j - 1] == s[i] || p[j - 1] == '.')
        && (is_match[i][j + 1] || is_match[i + 1][j]);
    }
  }
  return is_match[m][n];
}

```

#### Scramble String

#### Palindrome Partitioning

Given a string `s`, partition `s` such that every substring[^2] of the partition is a palindrome[^3]. Return the *minimum* cuts needed for a palindrome partitioning of `s`.

```c++
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

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

The demons had captured the princess and imprisoned her in *the bottom-right corner* of a `dungeon`. The `dungeon` consists of `m * n` rooms laid out in a 2D grid. Our valiant knight was initially positioned in *the top-left room* and must fight his way through `dungeon` to rescue the princess. The knight has an initial health point represented by a positive integer. If at any point his health point drops to `0` or below, he dies immediately. Some of the rooms are guarded by demons[^4], so the knight loses health upon entering these rooms; other rooms are either empty[^5] or contain magic orbs that increase the knight's health[^6]. To reach the princess as quickly as possible, the knight decides to move only *rightward* or *downward* in each step. Return the knight's minimum initial health so that he can rescue the princess. Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

```c++
#include <algorithm>
#include <climits>
#include <vector>

using namespace std;

int calculateMinimumHP(vector<vector<int>>& dungeon) {
  int m = dungeon.size(), n = dungeon[0].size();
  vector<vector<int>> health(2, vector<int>(n + 1, INT_MAX));
  health[0][--n] = 1;
  for (int i = --m; i >= 0; i--) {
    swap(health[0], health[1]);
    for (int j = n; j >= 0; j--)
      health[0][j] = max(min(health[1][j], health[0][j + 1]) - dungeon[i][j],
        1);
  }
  return health[0][0];
}

```

#### Zuma Game

[^1]: not partial
[^2]: A *substring* is a contiguous *non-empty* sequence of characters within a string.
[^3]: A *palindrome* is a string that reads the same forward and backward.
[^4]: represented by negative integers
[^5]: represented as 0
[^6]: represented by positive integers
