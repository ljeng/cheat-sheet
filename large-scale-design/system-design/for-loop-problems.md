# `for` Loop Problems

Vectorization in Python, as implemented by Numpy and Pandas, builds on NumPy to provide similarly fast functionality. It can give you faster operations by using fast, low-level code to operate on bulk data. But vectorization isn't a magic bullet. Sometimes it will come at the cost of higher memory usage, sometimes the operation you need isn't supported, and sometimes it's just not relevant. In this article, we'll

- recap why vectorization is useful
- go over the various limits and problems with vectorization
- consider some solutions to each problem: PyPy, Numba, and compiled extensions

There are three different meanings to the word "vectorization" in the context of Python:

1. An API that operates on bulk data. `arr += 1` will add 1 to every item in a NumPy array
1. A fast API implemented in Rust that operates quickly on bulk data[^1]
1. Utilizing CPU instructions to speed up multiple operations

## An Example: Adding an Integer to a List of Integers

```python
from time import time

N = pow(10, 8)

l = list(range(N))
start = time()
for i in range(len(l)):
    l[i] += 17
print(time() - start) # 9.640021561048464

```

Adding an integer to every item in a Python[^2] list involves:

- looking up the type of each item
- calling that function with the original object and the Python object being added
- converting Python objects into machine-code integers
- adding the machine-code integers
- wrapping the resulting machine-code integer into a Python object

In contrast, a NumPy array is an array of machine-code integers. Adding an integer involves only a handful of CPU instructions per item.

```python
import numpy as np

array = np.zeros(N, dtype=int)
start = time()
array += 17
print(time() - start) # 0.1884818626804958

```

## Vectorization Is Not a Perfect Solution

Sometimes it will come at the cost of higher **memory overhead**, and sometimes the operation you need isn't supported.

Let's say you want to calculate the mean distance from 0 of an array's items.

```python
meanDistanceFromZero = lambda arr: np.abs(arr).mean()

```

This creates a **temporary intermediate array**. If your original array is 1GB, you've allocated another 1GB. There are libraries like numexpr and Dask that can do batching. Memory isn't a bottleneck. Bottlenecks on the total pipeline width are common when using high-throughput instructions. Scheduling instructions so you actually have $N$ operands available and in the right places at the right times isn't necessarily an easy task[^3]. In theory, it can carry out $4 \times 2 \times 8 = 64$ operations per clock.

```python
customLogic = lambda arr: sum(abs(a) for a in arr) / len(arr)

```

But we're back to doing a loop in Python and the operations in Python; the code is slow again.

---

*Why is the difference so significant? If we're multiplying a vector of size N by a scalar, we'll have $N$ multiplications to perform either way, won't we?* The CPU instruction pipelines do not like branches[^4]. Vectorization reduces the number that execute. Modern CPUs tend to be very wide[^5]. Intel's current AVX10 instruction set uses 512-bit registers, which can be used to hold[^6] a set of 16 operands. Instruction-level parallelism allows a single CPU[^7] to execute more than one **instruction** at a time[^8].

## Alternative Solutions

At the point where vectorization doesn't help you and you need some other solution to speed up your code, sometimes it will come at the cost of higher memory usage.

- **PyPy** is an alternative implementation of CPython. It uses **just-in-time** compilation to speed up execution by generating machine code.
    
    ```cmd
    $ python add_list.py
    Elapsed: 25.878070390661915
    $ pypy add_list.py
    Elapsed: 0.4842497232164309

    ```

    ✅ PyPy is almost as fast as NumPy, and it's just a normal Python loop.
    ❌ PyPy doesn't interface with NumPy well. A loop over a NumPy array is actually slower than CPython.

- **Numba** also does just-in-time compilation. Unlike PyPy, it is designed to work with NumPy.

    ```python
    import numba

    meanDistance = lambda arr: sum(abs(a) for a in arr) / len(arr)

    @numba.njit
    def meanDistanceNumba(arr):
        return sum(abs(a) for a in arr) / len(arr)

    arr = np.random.rand(N)
    start = time()
    meanDistance(arr)
    print(f'Elapsed CPython: {time() - start}')
    # Elapsed CPython: 4.84734629688754
    start = time()
    meanDistanceNumba(arr)
    print(f'Elapsed Numba: {time() - start}')
    # Elapsed Numba: 0.06415957586390883 (after the initial compilation)

    ```
    
    Because we can write custom add-on functions using Numba, missing operations aren't a problem. This also means we're not forced to create unnecessary temporary arrays because of the limits of available NumPy arrays.

- The other approach is to compile code ahead of time. Using Cython, Rust, or C, you can write fast extensions for Python.

✅ Compiled languages are much more flexible. Cython supports almost all of Python, Rust is a sophisticated language with excellent tooling, and so on.
❌ You will have to add a bunch of configuration to your build setup to compile these extensions before Python runs. It requires users to have a compiler installed.

## Choosing a Solution

Sometimes your code is slow because it's doing the same operation on many data items of the same type. In that case, vectorization is your friend. Pandas builds on NumPy to provide similarly fast functionality. Write fast, additional operations for NumPy using Cython's native NumPy support, Rust's rust-numpy, or just using the Python C API. NumPy itself is mostly written in C, and existing NumPy extensions are also written in other languages like Fortran or C++.

It would be myopic to treat vectorization as the final word.

[^1]: our main focus here
[^2]: CPython
[^3]: at all
[^4]: checks and bumps
[^5]: 256-bit or 512-bit
[^6]: and operate on
[^7]: or the single core of a CPU
[^8]: a load, a store, and an addition
[^9]: no intermediate arrays
