# Mathematics

## Table of Contents

- [Counting](#counting)
- [Probability](#probability)
- [Discrete Math](#discrete-math)
- [Combinatorics](#combinatorics)

#### Divide Two Integers

Given two integers `dividend` and `divisor`, divide two integers *without* using multiplication, division, and mod operator. The integer division should truncate toward zero, which means losing its fractional part. For example, `8.345` would be truncated to `8`, and `-2.7335` would be truncated to `-2`. Return the *quotient* after dividing `dividend` by `divisor`. Assume we are dealing with an environment that could only store integers within the *32-bit* signed integer range: `[−2^31, 2^31 − 1]`. For this problem, if the quotient is *strictly greater than* `2^31 - 1`, then return `2^31 - 1`, and if the quotient is *strictly less than* `-2^31`, then return `-2^31`.

```python
import statistics

int_min = -1 << 31
int_max = -int_min - 1

def divide(dividend, divisor):
    negative = (dividend > 0) ^ (divisor > 0)
    dividend, divisor = abs(dividend), abs(divisor)
    quotient = 0
    while dividend >= divisor:
        d, multiple = divisor, 1
        while d << 1 <= dividend:
            d <<= 1
            multiple <<= 1
        dividend -= d
        quotient += multiple
    if negative: quotient *= -1
    return statistics.median([int_min, quotient, int_max])

```

#### $\sqrt(x)$

Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The returned integer should be non-negative as well. You must not use any built-in exponent function or operator. For example, do not use `pow(x, 0.5)`.

```cpp
#include <cmath>

double SQRT0 = 8000;
double EPSILON = 1;

int mySqrt(int x) {
  double y = SQRT0;
  while (fabs(y * y - x) > EPSILON) y = (y + x / y) / 2;
  return static_cast<int>(y);
}

```

#### Self Crossing

#### Perfect Rectangle

#### Largest Palindrome Product

#### Non-negative Integers without Consecutive Ones

Given a positive integer `n`, return the number of the integers in the range `[0, n]` whose binary representations do not contain consecutive ones.

```cpp
int log_max = 31;

int findIntegers(int n) {
  int fibonacci[log_max];
  fibonacci[0] = 1, fibonacci[1] = 2;
  for (int i = 2;
    i < log_max;
    fibonacci[i++] = fibonacci[i - 1] + fibonacci[i - 2]);
  int counter = 0;
  for (int i = --log_max, bit = 0; i >= 0; i--) {
    if (n & (1 << i)) {
      counter += fibonacci[i];
      if (bit) return counter;
      bit = 1;
    }
    else bit = 0;
  }
  return ++counter;
}
```

#### Reaching Points

Given four integers `sx`, `sy`, `tx`, and `ty`, return `true` if it is possible to convert the point `(sx, sy)` to the point `(tx, ty)` through some operations, or `false` otherwise. The allowed operation on some point `(x, y)` is to convert it to either `(x, x + y)` or `(x + y, y)`.

```python
def reachingPoints(sx, sy, tx, ty):
    while sx < tx and sy < ty: tx, ty = tx % ty, ty % tx
    return all([sx == tx,
        sy <= ty,
        not (ty - sy) % sx]) or all([sy == ty,
        sx <= tx,
        not (tx - sx) % sy])

```

#### `n`th Magical Number

A positive integer is magical if it is divisible by either `a` or `b`. Given the three integers `n`, `a`, and `b`, return the `n`th magical number. Since the answer may be very large, return it modulo `10^9 + 7`.

```python
import math
from math import ceil

mod = 10**9 + 7

def nthMagicalNumber(n, a, b):
    lcm = math.lcm(a, b)
    div, m = divmod(n, lcm // a + lcm // b - 1)
    magical_number = m / (1 / a + 1 / b)
    return (div * lcm + min(ceil(magical_number / a) * a,
        ceil(magical_number / b) * b)) % mod

```

## Counting

#### Climbing Stairs

You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb ` or `2` steps. In how many distinct ways can you climb to the top?

```cpp
#include <cmath>

int climbStairs(int n) {
  double sqrt5 = sqrt(5);
  return round(pow((sqrt5 + 1) / 2, ++n) / sqrt5);
}

```

#### Max Points on a Line

Given an array of `points` where `points[i] = [x[i], y[i]]` represents a point on the *xy*-plane, return the maximum number of points that lie on the same straight line.

```python
import collections
import math

def maxPoints(points):
    n = len(points)
    counter = [0] * 3
    for i in range(n):
        m = collections.defaultdict(int)
        counter[1:] = [1, 0]
        for j in range(i + 1, n):
            dx, dy = points[j][0] - points[i][0], points[j][1] - points[i][1]
            if dx == dy == 0: counter[1] += 1
            else:
                gcd = math.gcd(dx, dy)
                if gcd:
                    dx //= gcd
                    dy //= gcd
                if dx < 0: dx, dy = -dx, -dy
                elif not dx: dy = 1
                d = dx, dy
                m[d] += 1
                counter[2] = max(counter[2], m[d])
        counter[0] = max(counter[0], counter[1] + counter[2])
    return counter[0]

```

#### Number of Digit One

## Probability

#### Random Pick with Weight

You are given a *0-indexed* array of positive integers `w` where `w[i]` describes the *weight* of the `i`th index. You need to implement the function `pickIndex()`, which *randomly* picks an index in the range `[0, w.length - 1]`[^1] and returns it. The *probability* of picking an index `i` is `w[i] / sum(w)`.

- For example, if `w = [1, 3]`, the probability of picking index `0` is `1 / (1 + 3) = 0.25`[^2], and the probability of picking index `1` is `3 / (1 + 3) = 0.75`[^3].

```python
import collections
import random

Alias = collections.namedtuple('Alias', ['indexes', 'alias'])

class Solution:
    def __init__(self, w):
        self.sum_w = sum(w)
        full = [dict(), dict()]
        for i, x in enumerate(w):
            x *= len(w)
            full[x >= self.sum_w][i] = x
        self.aliases = []
        while all(full):
            under, underweight = full[0].popitem()
            over, overweight = full[1].popitem()
            weight = underweight + overweight - self.sum_w
            full[weight >= self.sum_w][over] = weight
            self.aliases.append(Alias(indexes=[under, over],
                alias=underweight))
        for over in full[1]:
            self.aliases.append(Alias(indexes=[over], alias=self.sum_w))

    def pickIndex(self):
        alias = random.choice(self.aliases)
        return alias.indexes[random.uniform(0, self.sum_w) > alias.alias]

```

## Discrete Math

## Combinatorics

#### Permutation Sequence

The set `[1, 2, 3, ..., n]` contains a total of `n!` unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for `n = 3`:

1. `"123"`
1. `"132"`
1. `"213"`
1. `"231"`
1. `"312"`
1. `"321"`

Given `n` and `k`, return the `k`<sup>th</sup> permutation sequence.

```python
import math
import sortedcontainers

def getPermutation(n, k):
    k -= 1
    set_ = sortedcontainers.SortedList(range(1, n + 1))
    permutation = []
    while n:
        n -= 1
        i, k = divmod(k, math.factorial(n))
        permutation.append(str(set_.pop(i)))
    return ''.join(permutation)

```

## *n*-choose-*k*

The number of ways to choose $k$ items from $n$ items without repetition and without order is

$$\pmatrix{
    n \\
    k \\
\pmatrix} = \frac{n!}{k! {(n - k)}!}$$

for

$$0 \leq k \leq n$$

or

```python
import math

math.comb(n, k)

```

[^1]: *inclusive*
[^2]: `25%`
[^3]: `75%`
