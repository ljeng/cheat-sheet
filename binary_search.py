import bisect


def is_true(x):
	# write your function here
	pass


class Range:

	def __getitem__(self, k): return is_true(k)


def index_of_first_true(arr):
	return bisect.bisect_left(Range(), True, 0, len(arr) - 1)