import sys
import bisect

class A:

    def __init__(self, function):
        self.function = function

    def __getitem__(self, k):
        return self.function(k)


def binary_search(lo, hi, function):
    return bisect.bisect_left(A(function), True, lo, hi)

def rabin_karp(pattern, s):
    m, n = len(pattern), len(s)
    s_hash = p_hash = 0
    roll = lambda h, x: (26*h + ord(x)) % sys.maxsize
    match = set()
    for a, b in zip(pattern, s):
        p_hash, s_hash = roll(p_hash, a), roll(s_hash, b)
    for i in range(n - m + 1):
        if s_hash == p_hash and all(s[i + j] == pattern[j] for j in range(m)):
            match.add(i)
        s_hash = (s_hash - ord(s[i]) * 26 ** m + ord(s[i + m])) % sys.maxsize
    return match
