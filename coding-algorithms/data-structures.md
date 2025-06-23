# Data Structures

## Table of Contents

- [Lists](#lists)
    - [Arrays](#arrays)
    - [Linked Lists](#linked-lists)
    - [Stacks](#stacks)
    - [Queues](#queues)
- [Hash](#hash)
    - [Sets](#sets)
    - [Maps](#maps)
    - [Tables](#tables)
    - [Dictionary](#dictionary)
- [Trees](c#trees)
    - [Binary](#binary)
    - [Heaps](#heaps)

## Lists

### Arrays

#### Count the Repetitions

#### Sliding Window Median

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

For example:

- If `arr = [2, 3, 4]`, the median is `3`.
- If `arr = [1,2,3,4]`, the median is `(2 + 3) / 2 = 2.5`.

You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within ${10}^{-5}$ of the actual value will be accepted.

```c++
#include <iterator>
#include <set>
#include <vector>

vector<double> medianSlidingWindow(vector<int>& nums, int k) {
  multiset<int> window(nums.begin(), nums.begin() + k);
  auto it = next(window.begin(), k / 2);
  vector<double> median;
  for (int i = k; ; i++) {
    median.push_back((double(*it) + *prev(it, k % 2 ^ 1)) / 2);
    if (i == nums.size()) return median;
    window.insert(nums[i]);
    if (nums[i] < *it) it--;
    if (nums[i - k] <= *it) it++;
    window.erase(window.lower_bound(nums[i - k]));
}

```

### Linked Lists

#### All $\Theta(1)$ Data Structure

Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the `AllOne` class:

- `AllOne()` Initializes the object of the data structure.
- `inc(String key)` Increments the count of the string `key` by `1`. If `key` does not exist in the data structure, insert it with count `1`.
- `dec(String key)` Decrements the count of the string `key` by `1`. If the count of `key` is `0` after the decrement, remove it from the data structure. It is guaranteed that `key` exists in the data structure before the decrement.
- `getMaxKey()` Returns one of the keys with the maximal count. If no element exists, return an empty string `""`.
- `getMinKey()` Returns one of the keys with the minimum count. If no element exists, return an empty string `""`.

Each function must run in $\Theta(1)$ time complexity.

```c++
#include <iterator>
#include <list>
#include <string>
#include <unordered_map>
#include <unordered_set>

using namespace std;

struct Node {
  int count;
  unordered_set<string> keys;
};

class AllOne {
public:
  list<Node> nodes;
  unordered_map<string, list<Node>::iterator> key_node;

  AllOne() {}
  
  void inc(string key) {
    if (key_node.count(key)) {
      auto it_current = key_node[key];
      auto it_next = next(it_current);
      int count = it_current->count + 1;
      if (it_next == nodes.end() || it_next->count != count)
        it_next = nodes.insert(it_next, {count, {}});
      it_current->keys.erase(key);
      it_next->keys.insert(key);
      key_node[key] = it_next;
      if (it_current->keys.empty()) nodes.erase(it_current);
    }
    else {
      if (nodes.empty() || nodes.front().count > 1) nodes.push_front({1, {}});
      nodes.front().keys.insert(key);
      key_node[key] = nodes.begin();
    }
  }
  
  void dec(string key) {
    auto it_current = key_node[key];
    int count = it_current->count - 1;
    it_current->keys.erase(key);
    if (count) {
      auto it_prev = it_current == nodes.begin()
        ? nodes.end()
        : prev(it_current);
      if (it_prev->count != count || it_current == nodes.begin())
        it_prev = nodes.insert(it_current, {count, {}});
      it_prev->keys.insert(key);
      key_node[key] = it_prev;
    }
    else key_node.erase(key);
    if (it_current->keys.empty()) nodes.erase(it_current);
  }
  
  string getMaxKey() {
    return nodes.empty() ? "" : *(prev(nodes.end())->keys.begin());
  }
  
  string getMinKey() {
    return nodes.empty() ? "" : *(nodes.front().keys.begin());
  }
};

```

### Stacks

#### Longest Valid Parentheses

Given a string containing just the characters `(` and `)`, return the length of the longest valid[^1] parentheses substring[^2].

```python
def longestValidParentheses(s):
    index = [-1]
    m = 0
    for i, x in enumerate(s):
        if x == '(': index.append(i)
        else:
            index.pop()
            if index: m = max(m, i - index[-1])
            else: index.append(i)
    return m

```

#### Largest Rectangle in Histogram

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return the area of the largest rectangle in the histogram.

```python
def largestRectangleArea(heights):
    heights.append(0)
    stack = [-1]
    area = 0
    for i, height in enumerate(heights):
        while height < heights[stack[-1]]:
            area = max(area, heights[stack.pop()] * (i - stack[-1] - 1))
        stack.append(i)
    return area

```

#### Basic Calculator

Given a string `s` representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation. You are *not* allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

```java
import java.util.Stack;

public int calculate(String s) {
  int sign = 1, x = 0, result = 0;
  Stack<Integer> stack = new Stack<Integer>();
  for (int i = 0; i < s.length(); i++){
    char c = s.charAt(i);
    if (Character.isDigit(c)) x = 10 * x + (int)(c - '0');
    else if (c == '+') {
      result += sign * x;
      sign = 1;
      x = 0;
    } else if (c == '-') {
      result += sign * x;
      sign = -1;
      x = 0;
    } else if (c == '(') {
      stack.push(result);
      stack.push(sign);
      sign = 1;
      result = 0;
    } else if (c == ')') {
      result = (result + sign * x) * stack.pop() + stack.pop();
      x = 0;
    }
  }
  return sign * x + result;
}

```

#### Reconstruct Itinerary

You are given a list of airline `tickets` where `tickets[i] = [from[i], to[i]]` represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it. All of the tickets belong to a man who departs from `"JFK"`, thus, the itinerary must begin with `"JFK"`. If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary `["JFK", "LGA"]` has a smaller lexical order than `["JFK", "LGB"]`. You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

```python
import collections

def findItinerary(tickets):
    airports = ['JFK']
    adjacency = collections.defaultdict(list)
    for from_, to in sorted(tickets, reverse=True): adjacency[from_].append(to)
    itinerary = []
    while airports:
        while adjacency[airports[-1]]: airports.append(adjacency[airports[-1]].pop())
        itinerary.append(airports.pop())
    return itinerary[::-1]

```

#### Tag Validator

Given a string representing a code snippet, implement a tag validator to parse the code and return whether it is valid. A code snippet is valid if all the following rules hold:

1. The code must be wrapped in a *valid closed tag*. Otherwise, the code is invalid.
1. A *closed tag*[^3] has exactly the following format: `<TAG_NAME>TAG_CONTENT</TAG_NAME>`. Among them, `<TAG_NAME>` is the start tag, and `</TAG_NAME>` is the end tag. The `TAG_NAME` in start and end tags should be the same. A closed tag is *valid* if and only if the `TAG_NAME` and `TAG_CONTENT` are valid.
1. A *valid* `TAG_NAME` only contain *upper-case letters*, and has length in range `[1, 9]`. Otherwise, the `TAG_NAME` is *invalid*.
1. A *valid* `TAG_CONTENT` may contain other *valid closed tags*, *cdata* and any characters[^1] **except** unmatched `<`, unmatched start and end tag, and unmatched or closed tags with invalid `TAG_NAME`. Otherwise, the T`AG_CONTENT` is *invalid*.
1. A start tag is unmatched if no end tag exists with the same `TAG_NAME`, and vice versa. However, you also need to consider the issue of unbalanced when tags are nested.
1. A `<` is unmatched if you cannot find a subsequent `>`. And when you find a `<` or `</`, all the subsequent characters until the next `>` should be parsed as `TAG_NAME`[^3].
1. The cdata has the following format: `<![CDATA[CDATA_CONTENT]]>`. The range of `CDATA_CONTENT` is defined as the characters between `<![CDATA[` and the *first subsequent* `]]>`.
1. `CDATA_CONTENT` may contain *any characters*. The function of cdata is to forbid the validator to parse `CDATA_CONTENT`, so even it has some characters that can be parsed as tag[^1], you should treat it as *regular characters*.

```python
def isValid(code):
    def parseTag(i, k):
        j = i + k
        i = code.find('>', j)
        if i in {-1, j} or i - j > 9: return None, -1
        tag_name = code[j:i]
        if not all(x.isupper() for x in tag_name): return None, -1
        return tag_name, i

    i = 0
    tag_names = []
    while i < len(code):
        if i and not tag_names: return False
        if code.startswith('<![CDATA[', i):
            i = code.find(']]>', i + 9)
            if i == -1: return False
            i += 2
        elif code.startswith("</", i):
            tag_name, i = parseTag(i, 2)
            if not tag_names or tag_names.pop() != tag_name: return False
        elif code.startswith('<', i):
            tag_name, i = parseTag(i, 1)
            if not tag_name: return False
            tag_names.append(tag_name)
        i += 1
    return not tag_names

```

### Queues

#### Sliding Window Maximum

You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

```c++
#include <vector>
#include <deque>

using namespace std;

vector<int> maxSlidingWindow(vector<int>& nums, int k) {
  int n = nums.size();
  deque<int> index;
  k--;
  vector<int> max_sliding_window;
  for (int i = 0; i < n; i++) {
    if (!index.empty() && index.front() < i - k) index.pop_front();
    while (!index.empty() && nums[index.back()] < nums[i]) index.pop_back();
    index.push_back(i);
    if (i >= k) max_sliding_window.push_back(nums[index.front()]);
  }
  return max_sliding_window;
}

```

#### Integer to English Words

Convert a non-negative integer `num` to its English words representation.

```python
from collections import deque

one = ['',
    'One',
    'Two',
    'Three',
    'Four',
    'Five',
    'Six',
    'Seven',
    'Eight',
    'Nine',
    'Ten',
    'Eleven',
    'Twelve',
    'Thirteen',
    'Fourteen',
    'Fifteen',
    'Sixteen',
    'Seventeen',
    'Eighteen',
    'Nineteen']
ten = ['',
    'Ten',
    'Twenty',
    'Thirty',
    'Forty',
    'Fifty',
    'Sixty',
    'Seventy',
    'Eighty',
    'Ninety']
power1000 = ['', 'Thousand', 'Million', 'Billion']

def numberToWords(num):
    superwords = deque()
    i = 0
    while num:
        num, mod = divmod(num, 1000)
        if mod:
            subwords = deque()
            if mod >= 100:
                div, mod = divmod(mod, 100)
                subwords.extendleft([one[div], 'Hundred'])
            if mod >= 20:
                div, mod = divmod(mod, 10)
                subwords.appendleft(ten[div])
            subwords.extendleft([one[mod], power1000[i]])
            superwords.extendleft(subwords)
        i += 1
    if superwords: return ' '.join(word for word in superwords if word)
    else: return 'Zero'

```

## Hash

### Sets

### Maps

#### Substring with Concatenation of All Words

You are given a string `s` and an array of strings `words`. All the strings of words are of *the same length*. A *concatenated string* is a string that exactly contains all the strings of any permutation of words concatenated. For example, if `words = ["ab","cd","ef"]`, then `"abcdef"`, `"abefcd"`, `"cdabef"`, `"cdefab"`, `"efabcd"`, and `"efcdab"` are all concatenated strings. `"acdbef"` is not a concatenated string because it is not the concatenation of any permutation of words. Return an array of the starting indices of all the concatenated substrings in `s`. You can return the answer in *any order*.

```c++
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> findSubstring(string s, vector<string>& words) {
  int m = s.length(), n = words.size(), k = words[0].length();
  unordered_map<string, int> supercount;
  for (string word : words) supercount[word]++;
  vector<int> starting_indices;
  if (m >= n * k) for (int j = 0; j < k; j++) {
    int start = j, end = j, count = 0;
    unordered_map<string, int> subcount;
    while (end + k <= m) {
      string substring = s.substr(end, k);
      end += k;
      if (supercount.count(substring)) {
        count++, subcount[substring]++;
        while (subcount[substring] > supercount[substring])
          subcount[s.substr(start, k)]--, start += k, count--;
        if (count == n) starting_indices.push_back(start);
      }
      else {
        count = 0, start = end;
        subcount.clear();
      }
    }
  }
  return starting_indices;
}

```

#### Minimum Window Substring

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the *minimum window substring*[^2] of `s` such that every character in `t`[^4] is included in the window. If there is no such substring, return the empty string `""`. The input will be generated such that the answer is *unique.*

```c++
#include <climits>
#include <string>
#include <unordered_map>

using namespace std;

string minWindow(string source, string target) {
  int i = 0, j = 0, n = target.size(), pos = 0, len = INT_MAX;
  unordered_map<char, int> character_count;
  for (char x : target) character_count[x]++;
  while (j < source.size())
    for (n -= character_count[source[j++]]-- > 0;
      !n;
      n += !character_count[source[i++]]++)
      if (j - i < len) len = j - (pos = i);
  return len < INT_MAX ? source.substr(pos, len) : "";
}

```

### Tables

### Dictionary

## Trees

#### Word Search

#### Range Sum Query 2-D - Mutable

Given a 2-D matrix `matrix`, handle multiple queries of the following types:

1. *Update* the value of a cell in `matrix`.
1. Calculate the *sum* of the elements of `matrix` inside the rectangle defined by its *upper left corner* `(row1, col1)` and *lower right corner* `(row2, col2)`.

Implement the `NumMatrix` class:

- `NumMatrix(int[][] matrix)` Initializes the object with the integer matrix `matrix`.
- `void update(int row, int col, int val)` Updates the value of `matrix[row][col]` to be `val`.
- `int sumRegion(int row1, int col1, int row2, int col2)` Returns the *sum* of the elements of `matrix` inside the rectangle defined by its *upper left corner* `(row1, col1)` and *lower right corner* `(row2, col2)`.

```c++
class NumMatrix {
public:
  int m, n;
  vector<vector<int>> matrix;
  vector<vector<int>> bit;

  NumMatrix(vector<vector<int>>& matrix) {
    m = matrix.size(), n = matrix[0].size();
    this->matrix = vector<vector<int>>(m, vector<int>(n));
    bit = vector<vector<int>>(m + 1, vector<int>(n + 1));
    for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) update(i, j, matrix[i][j]);
  }
  
  void update(int row, int col, int val) {
    int delta = val - matrix[row][col];
    matrix[row][col] = val;
    for (int i = row + 1; i <= m; i += i & -i)
      for (int j = col + 1; j <= n; j += j & -j)
        bit[i][j] += delta;
  }

  int sum(int row, int col) {
    int x = 0;
    for (int i = row; i > 0; i -= i & -i)
      for (int j = col; j > 0; j -= j & -j)
        x += bit[i][j];
    return x;
  }
  
  int sumRegion(int row1, int col1, int row2, int col2) {
    return sum(row1, col1) - sum(row1, ++col2) - sum(++row2, col1) + sum(row2, col2);
  }
};

```

#### Palindrome Pairs

#### `k`th Smallest in Lexicographical Order

### Binary

#### Binary Tree Maximum Path Sum

A *path* in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence *at most once*. Note that the path does not need to pass through the root. The *path sum* of a path is the sum of the node's values in the path. Given the `root` of a binary tree, return the maximum *path sum* of any *non-empty path*.

```python
import sys

def maxPathSum(root):
    stack = [(root, False)]
    path_sum = -sys.maxsize
    node_sum = dict()
    while stack:
        node, visited = stack.pop()
        if visited:
            left = max(node_sum.get(node.left, 0), 0)
            right = max(node_sum.get(node.right, 0), 0)
            path_sum = max(path_sum, node.val + left + right)
            node_sum[node] = node.val + max(left, right)
        else:
            stack.append((node, True))
            for child in (node.left, node.right):
                if child: stack.append((child, False))
    return path_sum

```

### Heaps

#### The Skyline Problem

A city's *skyline* is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the *skyline* formed by these buildings collectively.

The geometric information of each building is given in the array buildings where `buildings[i] = [left[i], right[i], height[i]]`:

- `left[i]` is the *x*-coordinate of the left edge of the `i`th building.
- `right[i]` is the *x*-coordinate of the right edge of the `i`th building.
- `height[i]` is the height of the `i`th building.

You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height `0`. The skyline should be represented as a list of "key points" *sorted by their **x**-coordinate* in the form `[[x[1], y[1]], [x[2], y[2]], ...]`. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a *y*-coordinate *0* and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour. There must be no consecutive horizontal lines of equal height in the output skyline. For instance, `[..., [2, 3], [4, 5], [7, 5], [11, 5], [12, 7], ...]` is not acceptable; the three lines of height `5` should be merged into one in the final output as such: `[..., [2, 3], [4, 5], [12, 7], ...]`.

```python
import heapq
import itertools
import sys

def getSkyline(buildings):
    height_right = [(0, sys.maxsize)]
    skyline = [[0, 0]]
    for left, height, right in sorted(itertools.chain(*[[(l, -h, r),
        (r, 0, 0)] for l, r, h in buildings])):
        while left >= height_right[0][1]: heapq.heappop(height_right)
        if height: heapq.heappush(height_right, (height, right))
        height = -height_right[0][0]
        if skyline[-1][1] != height: skyline.append([left, height])
    skyline.pop(0)
    return skyline

```

#### Rearrange String `k` Distance Apart

Given a string `s` and an integer `k`, rearrange `s` such that the same characters are *at least* distance `k` from each other. If it is not possible to rearrange the string, return an empty string `""`.

```python
import collections
import heapq

def rearrangeString(s, k):
    heap = [(-count, character) for character, count in collections.Counter(s).items()]
    heapq.heapify(heap)
    queue = collections.deque()
    rearranged = []
    while heap:
        count, character = heapq.heappop(heap)
        queue.append((count + 1, character))
        rearranged.append(character)
        if len(queue) >= k:
            x = count, character = queue.popleft()
            if count < 0: heapq.heappush(heap, x)
    return ''.join(rearranged) if len(rearranged) == len(s) else ''

```

#### Course Schedule

There are `n` different online courses numbered from `1` to `n`. You are given an array `courses` where `courses[i] = [duration[i], lastDay[i]]` indicate that the `i`<sup>th</sup> course should be taken *continuously* for `duration[i]` days and must be finished before or on `lastDay[i]`. You will start on the `1`<sup>st</sup> day and you cannot take two or more courses simultaneously. Return the maximum number of courses that you can take.

```python
import heapq

def scheduleCourse(courses):
    days = 0
    durations = []
    for duration, lastDay in sorted(courses, key = lambda x: x[1]):
        days += duration
        heapq.heappush(durations, -duration)
        if days > lastDay: days += heapq.heappop(durations)
    return len(durations)

```

## Graphs

#### Longest Duplicate Substring

Given a string `s`, consider all duplicated substrings: (contiguous) substrings of `s` that occur 2 or more times. The occurrences may overlap. Return any duplicated substring that has the longest possible length. If `s` does not have a duplicated substring, the answer is `""`.

```python
class State:
    def __init__(self, link=-1):
        self.link = link
        self.word = ''
        self.next = dict()

def longestDupSubstring(s):
    automaton = [State()]
    last = 0
    lds = ''
    for x in s:
        last, p = len(automaton), last
        automaton.append(State())
        automaton[last].word = automaton[p].word + x
        while p >= 0 and x not in automaton[p].next:
            automaton[p].next[x] = last
            p = automaton[p].link
        if p >= 0:
            q = automaton[p].next[x]
            if len(automaton[q].word) == len(automaton[p].word) + 1:
                automaton[last].link = q
                lds = max([lds, automaton[q].word], key=len)
            else:
                automaton.append(State(automaton[q].link))
                last += 1
                automaton[last].word = automaton[p].word + x
                automaton[last].next = automaton[q].next.copy()
                lds = max([lds, automaton[last].word], key=len)
                while p >= 0 and automaton[p].next.get(x, None) == q:
                    automaton[p].next[x] = last
                    p = automaton[p].link
                last -= 1
                automaton[q].link = automaton[last].link = last + 1
        else: automaton[last].link = 0
    return lds

```

[^1]: well-formed
[^2]: A *substring* is a contiguous *non-empty* sequence of characters within a string.
[^3]: not necessarily valid
[^4]: *including duplicates*
