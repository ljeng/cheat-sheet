# Data Structures

## Lists

### Arrays

#### Count the Repetitions

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
    }
    else if (c == '-') {
      result += sign * x;
      sign = -1;
      x = 0;
    }
    else if (c == '(') {
      stack.push(result);
      stack.push(sign);
      sign = 1;
      result = 0;
    }
    else if (c == ')') {
      result = (result + sign * x) * stack.pop() + stack.pop();
      x = 0;
    }
  }
  return sign * x + result;
}

```

### Queues

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

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the *minimum window substring*[^2] of `s` such that every character in `t`[^3] is included in the window. If there is no such substring, return the empty string `""`. The input will be generated such that the answer is *unique.*

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

#### Palindrome Pairs

#### *k*th Smallest in Lexicographical Order

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
[^3]: *including duplicates*
