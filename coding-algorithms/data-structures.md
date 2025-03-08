# Data Structures

## Lists

### Arrays

#### Count the Repetitions

### Linked Lists

### Stacks

#### Longest Valid Parentheses

### Queues

#### Integer to English Words

Convert a non-negative integer `num` to its English words representation.

```python
from collections import deque

ONES = ['',
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
TENS = ['',
    'Ten',
    'Twenty',
    'Thirty',
    'Forty',
    'Fifty',
    'Sixty',
    'Seventy',
    'Eighty',
    'Ninety']
POWER1000 = ['', 'Thousand', 'Million', 'Billion']

def numberToWords(num):
    superqueue = deque()
    i = 0
    while num:
        num, mod = divmod(num, 1000)
        if mod:
            subqueue = deque()
            if mod >= 100:
                div, mod = divmod(mod, 100)
                subqueue.extendleft([ONES[div], 'Hundred'])
            if mod >= 20:
                div, mod = divmod(mod, 10)
                subqueue.appendleft(TENS[div])
            subqueue.extendleft([ONES[mod], POWER1000[i]])
            superqueue.extendleft(subqueue)
        i += 1
    if superqueue:
        return ' '.join(word for word in superqueue if word)
    else:
        return 'Zero'

```

## Hash

### Sets

### Maps

### Tables

#### Substring with Concatenation of All Words

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
    states = [State()]
    last = 0
    lds = ''
    for x in s:
        last, p = len(states), last
        states.append(State())
        states[last].word = states[p].word + x
        while p != -1 and x not in states[p].next:
            states[p].next[x] = last
            p = states[p].link
        if p >= 0:
            q = states[p].next[x]
            if len(states[q].word) == len(states[p].word) + 1:
                states[last].link = q
                lds = max([lds, states[q].word], key=len)
            else:
                states.append(State(states[q].link))
                last += 1
                states[last].next = states[q].next.copy()
                states[last].word = states[p].word + x
                lds = max([lds, states[last].word], key=len)
                while p >= 0 and states[p].next.get(x, None) == q:
                    states[p].next[x] = last
                    p = states[p].link
                last -= 1
                states[q].link = states[last].link = last + 1
        else:
            states[last].link = 0
    return lds

```
