# cheat-sheet
This cheat sheet contains concise implementations of common data structures and algorithms (DS&As) in Python. The purpose of this cheat sheet is to give you a short list of DS&As that are worth memorizing because they are frequently used, yet most people struggle with them. Some of the problems you encounter may not use the exact same algorithms, but rather with minor modifications. I have excluded DS&As that most computer science graduates can implement with very little thought, such as tree traversals.
## [Binary Search](https://github.com/ljeng/cheat-sheet/blob/master/binary_search.py)
### Index of First True
Given a range of elements sorted by a boolean key, `index_of_first_true` finds the first index of an element whose key is true. The helper function `is_true` is up to the user to write.

#### Example
I'm thinking of an integer between -2<sup>31</sup> and 2<sup>31</sup> that you are to guess. Every time you make a guess, I will tell you whether my integer is higher or lower. I will write `is_true` such as it returns True if your guess is equal to or more than my integer, otherwise False.
```python
def is_true(guess):
    # set my_integer to the integer you are thinking of in the line below
    # my_integer = 0
    return guess >= my_integer
```
Now, if I call `index_of_first_true` on `start = -2**31` and `end = 2**31`, it will return the integer I'm thinking of.

Time complexity: O(log *n*)

Space complexity: O(1)
## Bit Manipulation
### Single Number
Given an array of integers, every element appears *k* times except for one, which appears *p* times. Find that single one.

Constraints: *k* > 1, *p* > 0, *p*%*k* != 0
## [Dynamic Programming](https://github.com/ljeng/cheat-sheet/blob/master/dynamic_programming.py)
### Longest Common Subsequence
Given two sequences *x* and *y*, finds the length of the longest common subsequence.

Time complexity: O(*mn*)

Space complexity: O(*mn*)
### Knapsack Problem
Given a set of items, each with a weight and a value, determines the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

Time complexity: O(*mn*)

Space complexity: O(*mn*)
### Best Time to Buy and Sell Stock
You are given the following parameters:
* a list of integers `prices` for which the *i*th element is the price of a given stock on day *i*
* a non-negative integer `fee` which is is the transaction fee
* a non-negative integer `k`
* a boolean `cooldown`

Design an algorithm to find the maximum profit subject to the following restrictions:
* You may complete at most *k* transactions.
* You may not buy more than one share of a stock at a time and must sell the stock before you buy again.
* If `cooldown == True`, you cannot buy stock on the next day.
* Buy and sell together count as one transaction regarding the transaction fee.
### Matrix Chain Multiplication
Given a sequence of matrices, finds the most efficient way to multiply these matrices. There are many options because no matter how the product is parenthesized, the result obtained will remain the same. For example, for four matrices *A*, *B*, and *C*, we would have (*AB*)*C* = *A*(*BC*). However, the order in which the product is parenthesized affects the number of simple arithmetic operations needed to compute the product.
#### Example
*A* is a 2 × 6 matrix, *B* is a 6 × 1 matrix, and *C* is a 1 × 12 matrix. Computing (*AB*)*C* needs 2 × 6 × 1 + 2 × 1 × 12 = 36 operations, while computing *A*(*BC*) needs 6 × 1 × 12 + 2 × 6 × 12 = 216 operations. The input is a list of matrix dimensions, in this case `dimensions = [2, 6, 1, 12]`. The output is the minimum cost of the matrix multiplication, which is 36.

Matrix chain multiplication clones are by far the most common O(*n*<sup>3</sup>) dynamic programming problems.

Time complexity: O(*n*<sup>3</sup>)

Space complexity: O(*n*<sup>2</sup>)
## [Shortest Path Algorithms](https://github.com/ljeng/cheat-sheet/blob/master/shortest_path.py)
### Djikstra's Algorithm
Finds shortest paths from a source with all non-negative cycles.

Time complexity: O(*E* + *V* log *V*)
### Bellman-Ford Algorithm
Finds shortest paths from a source with possible negative cycles.
### Floyd-Warshall Algorithm
Finds all shortest paths.

Time complexity: O(*V*<sup>3</sup>)

Space complexity: O(*V*<sup>2</sup>)
### Deciding Which Algorithm to Use
Djikstra's: Only works for non-negative cycles, only finds shortest paths from a single source, fast runtime.

Bellman-Ford: Works for negative cycles, only finds shortest paths from a single source, medium runtime.

Floyd-Warshall: Works for negative cycles, finds all shortest paths, slow runtime. If you're doing a programming competition and don't have a strict runtime limit, you may consider using Floyd-Warshall given how little effort it takes to code.

## [Sorting](https://github.com/ljeng/cheat-sheet/blob/master/sorting.py)
### Quickselect
Finds the *k*th smallest element in an unordered list.

Time complexity: O(*n*) average, O(*n*<sup>2</sup>) worst
### Radix Sort
Sorts a sequence of integers in linear time. The advantage of using radix sort over the built-in `iterable.sort()` is it runs in linear time.

Time complexity: O(*wn*)

Space complexity: O(*wn*)
## Stacks and Queues
### All Nearest Smaller Values
For each position in a sequence of numbers, search among the previous positions for the last position that contains a smaller value. The input is a sequence. The output is a list of indices. If there is no nearest smaller value, it appends -1.

Time complexity: O(*n*)

Space complexity: O(*n*)
### String Parsing
I will use the words "parentheses" and "brackets" interchangeably when describing this algorithm. Given a string with brackets, evaluates the string such that the contents inside the brackets are evaluated first, as in PEMDAS.
## Competitive Programming Hacks
### O(*n*) Tricks
The following O(*n*) functions are very fast in terms of milliseconds:
* `A.pop(i)`
* `A.insert(i, x)`
* `bisect.insort(A, x)`

`list.pop(i)` is significantly faster than `list.remove(x)` even though they have the same Big-O complexity. Any problem with an intended solution runtime of O(1) or O(log *n*) would likely also accept these O(*n*) tricks.
### Memoization
There are two ways to implement memoization in Python. First, we have the traditional way you were taught in college.
```python
memo = dict()


def recursion(k):
    if k not in memo:
        # write your recursive function here
        memo[k] = ouput
    return memo[k]
```
Then we have the way we do it in programming competitions, which only takes two extra lines.
```python
import functools
@functools.LRU_cache(None)


def recursion(k):
    # write your recursive function here
```
