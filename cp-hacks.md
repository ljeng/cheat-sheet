### Fast O(*n*) Tricks
The following Python functions operate in O(*n*) time but are fast enough to pass an online judge for a problem that is intended to be solved in constant, logarithmic, or O(sqrt(n)) time.

* `arr.insert(i, value)`
* `arr.remove(value)`
* `arr.pop(i)`
* `arr[i:j]` definitely works if `i` is small enough or `j` is large enough. I haven't tested for other values.
* All insort functions including `bisect.insort(A, item)`

### 2-Line Memoization
In college, you learned memoization the traditional way:
```python
def main():

    def recurse(x):
        if x not in memo:
            # solve recurse(x)
            # let value = recurse(x)
            memo[x] = value
        return memo[x]
    
    memo = dict()
```
There's a much faster way to do this that only requires two lines of additional code.
```python
import functools

def main():

    @functools.lru_cache(None)
    def recurse(x):
        # solve recurse(x)
```
