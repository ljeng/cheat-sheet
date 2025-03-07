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
                subqueue.extendleft([self.ONES[div], 'Hundred'])
            if mod >= 20:
                div, mod = divmod(mod, 10)
                subqueue.appendleft(self.TENS[div])
            subqueue.extendleft([self.ONES[mod], self.POWER1000[i]])
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

#### *k*th Smallest in Lexicographical Order

#### Reverse Pairs

#### Palindrome Pairs

### Binary

#### Binary Tree Maximum Path Sum

### Heaps

## Graphs
