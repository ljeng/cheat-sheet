# Mathematics

#### Self Crossing

#### Perfect Rectangle

#### Largest Palindrome Product

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

## Counting

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
