import bisect


class A:

    def __init__(self, function):
        self.function = function

    def __getitem__(self, k):
        return self.function(k)


def binary_search(lo, hi, function):
    return bisect.bisect_left(A(function), True, start, end)