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
  vector<vector<bool>> is_match(2, vector<bool>(n + 1, false));
  is_match[0][0] = true;
  for (int j = 1; j < n; j++)
      if (p[j] == '*')
        is_match[0][j + 1] = is_match[0][j - 1];
  for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
      if (p[j] == s[i] || p[j] == '.') is_match[1][j + 1] = is_match[0][j];
      else if (p[j] == '*' && j)
        is_match[1][j + 1] = is_match[1][j - 1]
          || (p[j - 1] == s[i] || p[j - 1] == '.')
          && (is_match[0][j + 1] || is_match[1][j] || is_match[1][j + 1]);
      else if (p[j] != '*') is_match[1][j + 1] = false;
    }
    is_match[0] = is_match[1];
  }
  return is_match[0][n];
}

```

#### Scramble String

#### Distinct Subsequences

Given two strings `s` and `t`, return the number of distinct *subsequences* of `s` which equals `t`. The answer fits on a 32-bit signed integer.

```c++
#include <string>
#include <vector>

using namespace std;

int numDistinct(string s, string t) {
  int m = s.size(), n = t.size();
  if (n > m) return 0;
  vector<unsigned long long> num_distinct(n + 1);
  num_distinct[0] = 1;
  for (int i = 0; i < m; i++)
    for (int j = n; j > 0; j--)
      if (s[i] == t[j - 1])
        num_distinct[j] += num_distinct[j - 1];
  return num_distinct[n];
}

```

#### Distinct Subsequences

Given two strings `s` and `t`, return the number of distinct *subsequences* of `s` which equals `t`. The answer fits on a 32-bit signed integer.

```c++
#include <string>
#include <vector>

using namespace std;

int numDistinct(string s, string t) {
  int m = s.size(), n = t.size();
  if (n > m) return 0;
  vector<unsigned long long> num_distinct(n + 1);
  num_distinct[0] = 1;
  for (int i = 0; i < m; i++)
    for (int j = n; j > 0; j--)
      if (s[i] == t[j - 1])
        num_distinct[j] += num_distinct[j - 1];
  return num_distinct[n];
}

```

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
    for (int k = 0; k < 2; k++) {
      int j = k;
      while (j < min(i + k + 1, n - i) && s[i - j + k] == s[i + j])
        cut[i + j] = min(cut[i - j + k] + 1, cut[i + ++j]);
    }
  return cut[n];
}

```

#### Dungeon Game

The demons had captured the princess and imprisoned her in *the bottom-right corner* of a `dungeon`. The `dungeon` consists of `m * n` rooms laid out in a 2-D grid. Our valiant knight was initially positioned in *the top-left room* and must fight his way through `dungeon` to rescue the princess. The knight has an initial health point represented by a positive integer. If at any point his health point drops to `0` or below, he dies immediately. Some of the rooms are guarded by demons[^4], so the knight loses health upon entering these rooms; other rooms are either empty[^5] or contain magic orbs that increase the knight's health[^6]. To reach the princess as quickly as possible, the knight decides to move only *rightward* or *downward* in each step. Return the knight's minimum initial health so that he can rescue the princess. Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

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

#### Best Time to Buy and Sell Stock

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i`<sup>th</sup> day, and an integer `k`. Find the maximum profit you can achieve. You may complete at most `k` transactions: i.e. you may buy at most `k` times and sell at most `k` times. You may not engage in multiple transactions simultaneously[^7].

```python
import itertools

def maxProfit(k, prices):
    n = len(prices)
    if k < n >> 1:
        dp = [[0] * n for _ in range(2)]
        for j in range(1, k + 1):
            dp[1][0] = 0
            profit = dp[0][0] - prices[0]
            for i in range(1, n):
                dp[1][i] = max(dp[1][i - 1], profit + prices[i])
                profit = max(profit, dp[0][i] - prices[i])
            dp[0] = dp[1][:]
        return dp[0][-1]
    else: return sum(max(b - a, 0) for a, b in itertools.pairwise(prices))

```

#### Expression Add Operators

Given a string `num` that contains only digits and an integer `target`, return *all possibilities* to insert the binary operators `+`, `-`, and/or `*` between the digits of `num` so that the resultant expression evaluates to the `target` value. Note that operands in the returned expressions should not contain leading zeros.

```python
import collections

operator = '+-*'
State = collections.namedtuple('State',
  ['i', 'expression', 'eval', 'multiplier'])

def addOperators(num, target):
    n = len(num)
    x = int(num[0])
    stack = [State(i=1, expression=num[:1], eval=x, multiplier=x)]
    if num[0] != '0':
        for i in range(2, n + 1):
            expression = num[:i]
            x = int(expression)
            stack.append(State(i, expression, eval=x, multiplier=x))
    possibilities = []
    while stack:
        u = stack.pop()
        for i in range(u.i, n):
            if i > u.i and num[u.i] == '0': break
            i += 1
            u_string = num[u.i:i]
            u_int = int(u_string)
            for operator, x, multiplier in zip(operator,
                [u_int, -u_int, u.multiplier * (u_int - 1)],
                [1, -1, u.multiplier]):
                stack.append(State(i,
                    expression=f'{u.expression}{operator}{u_string}',
                    eval = u.eval + x,
                    multiplier = multiplier * u_int))
        if (u.i, u.eval) == (n, target): possibilities.append(u.expression)
    return possibilities

```

#### Zuma Game

#### Decode Ways

A message containing letters from `A-Z` can be encoded into numbers using the following mapping:

```
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
```

To *decode* an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above[^8].

For example, `11106` can be mapped into:

- `AAJF` with the grouping `(1 1 10 6)`
- `KJF` with the grouping `(11 10 6)`

The grouping `(1 11 06)` is invalid because `06` cannot be mapped into `F` since `6` is different from `06`.

*In addition* to the mapping above, an encoded message may contain the `*` character, which can represent any digit from `1` to `9`[^9]. For example, the encoded message `1*` may represent any of the encoded messages `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, or `19`. Decoding `1*` is equivalent to decoding any of the encoded messages it can represent. Given a string `s` consisting of digits and `*` characters, return the *number* of ways to *decode it*. Since the answer may be very large, return it *modulo* `10^9 + 7`.

```python
import numpy as np

mod = 10**9 + 7

def numDecodings(s):
    ways = np.array([1, 0, 0])
    for x in s:
        if x.isdigit(): y = [[x > '0', 1, x <= '6'], [x == '1', x == '2']]
        else: y = [[9, 9, 6], [1, 1]]
        ways = np.array([1,
          ways[0],
          ways[0]]) * ([sum(ways * y[0]) % mod] + y[1])
    return int(ways[0])

```

```c++
#include <cctype>
#include <numeric>
#include <string>
#include <vector>

using namespace std;

const int mod = pow(10, 9) + 7;

int numDecodings(string s) {
  vector<long> ways = {1, 0, 0};
  for (char x : s) {
    vector<vector<int>> y = isdigit(x) 
      ? vector<vector<int>>{{x > '0', 1, x <= '6'}, {x == '1', x == '2'}}
      : vector<vector<int>>{{9, 9, 6}, {1, 1}};
    ways = {(inner_product(ways.begin(), ways.end(), begin(y[0]), 0L)) % mod,
      (1L * ways[0] * y[1][0]) % mod,
      (1L * ways[0] * y[1][1]) % mod};
  }
  return ways[0];
}

```

[^1]: not partial
[^2]: A *substring* is a contiguous *non-empty* sequence of characters within a string.
[^3]: A *palindrome* is a string that reads the same forward and backward.
[^4]: represented by negative integers
[^5]: represented as 0
[^6]: represented by positive integers
[^7]: you must sell the stock before you buy again
[^8]: there may be multiple ways
[^9]: `0` is excluded
