# Data Structures

## Lists

### Arrays

#### Count the Repetitions

### Linked Lists

### Stacks

#### Longest Valid Parentheses

Given a string containing just the characters `(` and `)`, return the length of the longest valid (well-formed) parentheses substring[^1].

```c++
#include <algorithm>
#include <stack>
#include <string>

using namespace std;

int longestValidParentheses(string s) {
  stack<int> index;
  index.push(-1);
  int m = 0;
  for (int i = 0; i < s.length(); i++) {
    if (s[i] == '(') index.push(i);
    else {
      index.pop();
      if (index.empty()) index.push(i);
      else m = max(m, i - index.top());
    }
  }
  return m;
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
    superqueue = deque()
    i = 0
    while num:
        num, mod = divmod(num, 1000)
        if mod:
            subqueue = deque()
            if mod >= 100:
                div, mod = divmod(mod, 100)
                subqueue.extendleft([one[div], 'Hundred'])
            if mod >= 20:
                div, mod = divmod(mod, 10)
                subqueue.appendleft(ten[div])
            subqueue.extendleft([one[mod], power1000[i]])
            superqueue.extendleft(subqueue)
        i += 1
    if superqueue: return ' '.join(word for word in superqueue if word)
    else: return 'Zero'

```

## Hash

### Sets

### Maps

#### Substring with Concatenation of All Words

### Tables

### Dictionary

## Trees

#### Word Search

#### Palindrome Pairs

#### *k*th Smallest in Lexicographical Order

#### Reverse Pairs

### Binary

#### Binary Tree Maximum Path Sum

### Heaps

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

[^1]: A *substring* is a contiguous *non-empty* sequence of characters within a string.
