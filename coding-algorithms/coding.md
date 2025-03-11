# Coding

## C++

#### Count the Repetitions

## APIs

## Object-Oriented Design and Programming

#### Insert, Delete, GetRandom $O(1)$ - Duplicates Allowed

`RandomizedCollection` is a data structure that contains a collection of numbers, possibly duplicates[^1]. It should support inserting and removing specific elements and also reporting a random element.

Implement the `RandomizedCollection` class:

- `RandomizedCollection()` Initializes the empty `RandomizedCollection` object.
- `bool insert(int val)` Inserts an item `val` into the multiset, even if the item is already present. Returns `true` if the item is not present, `false` otherwise.
- `bool remove(int val)` Removes an item `val` from the multiset if present. Returns `true` if the item is present, `false` otherwise. Note that if `val` has multiple occurrences in the multiset, we only remove one of them.
- `int getRandom()` Returns a random element from the current multiset of elements. The probability of each element being returned is *linearly related* to the number of the same values the multiset contains.

You must implement the functions of the class such that each function works on average $O(1)$ time complexity. `getRandom` will only be called if there is *at least one* item in the `RandomizedCollection`.

```python
import collections
import random

class RandomizedCollection:
    def __init__(self):
        self.vals = []
        self.val_index = collections.defaultdict(list)

    def insert(self, val):
        self.vals.append((val, len(self.val_index[val])))
        self.val_index[val].append(len(self.vals) - 1)
        return len(self.val_index[val]) == 1

    def remove(self, val):
        if self.val_index[val]:
            i = self.val_index[val].pop()
            last = last_val, last_index = self.vals.pop()
            if i < len(self.vals):
                self.vals[i] = last
                self.val_index[last_val][last_index] = i
            return True
        return False

    def getRandom(self):
        return random.choice(self.vals)[0]

```

## How to Test Your Code

## Corner Cases and Edge Cases

#### Valid Number

[^1]: a multiset
