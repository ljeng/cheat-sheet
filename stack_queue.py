def all_nearest_smaller_values(sequence):
	stack, index_list = [], []
	for i in range(len(sequence)):
		while stack and sequence[stack[-1]] >= sequence[i]: stack.pop()
		# if no smaller nearest value, append -1
		index_list += [stack[-1] if stack else -1]
		stack += [i]
	# output type = list of indices
	return index_list


def evaluate(s):
	# write your function here
	pass


def parse_string(s, open_bracket = '(', close_bracket = ')'):
	counter, inner, outer = 0, '', ''
	for char in s:
		if char == open_bracket: counter += 1
		elif char == close_bracket:
			counter -= 1
			if not counter:
				outer += evaluate(inner)
				inner = ''
		if (counter and char != open_bracket) or counter > 1: inner += char
		elif not counter and char != close_bracket: outer += char
	return evaluate(outer)