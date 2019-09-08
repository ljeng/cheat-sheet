## Stacks and Queues
### All Nearest Smaller Values
For each position in a sequence of numbers, search among the previous indices for the last index that contains a smaller value. Return a list of indices.
```python
def all_nearest_smaller_values(sequence):
	stack, index_list = [], []
	for i in range(len(sequence)):
		while stack and sequence[stack[-1]] >= sequence[i]: stack.pop()
		# if no smaller nearest value, append -1
		index_list += [stack[-1] if stack else -1]
		stack += [i]
	# output type = list of indices
	return index_list
```
### String Parsing
This is the basic implementation:
```python
# evaluate is a helper function for the main function parse_string
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
				outer += str(evaluate(inner))
				inner = ''
		if (counter and char != open_bracket) or counter > 1: inner += char
		elif not counter and char != close_bracket: outer += char
	return evaluate(outer)
```
#### Example 1
Implement a basic calculator to evaluate a simple expression string. The expression string may contain open `(` and closing parentheses `)`, the plus `+` or minus sign `-`, non-negative integers and empty spaces ` `. We modify the basic implentation to solve this:
```python
def evaluate(s): sum(int(char) for char in s.replace('--', '+').replace('-', '+-').split('+') if char)


def parse_string(s):
	counter, inner, outer = 0, '', ''
	for char in s:
		if char == '(': counter += 1
		elif char == ')':
			counter -= 1
			if not counter:
				outer += str(parse_string(inner))
				inner = ''
		if (counter and char != '(') or counter > 1: inner += char
		elif not counter and char != ')': outer += char
	return evaluate(outer)
```
We have an input string:

| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Character | ( | 5 | - | ( | 1 | + | ( | 5 | ) | ) | ) |

Now we're going to parse it starting from the innermost parentheses and going outward.

| `(` index | `)` index | inner | evaluate(inner) |
| --- | --- | --- | --- |
| 6 | 8 | 5 | 5 |
| 3 | 9 | 1+5 | 6 |
| 0 | 10 | 5-6 | -1 |
| whole string | whole string | -1 | -1 |

#### Example 2
Given an encoded string, return its decoded string. The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets repeated positive integer `k` times. The decoded string doesn't contain any brackets or digits. This time we need to modify the main function because we need to store `k`:
```python
def evaluate(s, k): return k*s

def parse_string(s, k = 1):
    counter, inner, outer, k_string = 0, '', '', ''
    for char in s:
        if char == '[': counter += 1
        elif char == ']':
            counter -= 1
            if not counter:
                outer += parse_string(inner, int(k_string))
                inner, k_string = '', ''
        if (counter and char != '[') or counter > 1: inner += char
        elif not counter:
            if char.isdigit(): k_string += char
            elif char != ']': outer += char
    return evaluate(outer, k)
```
We have an encoded string:

| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Character | 4 | [ | f | 2 | [ | a | b | o | m | l | ] |

Again, we parse it starting from the innermost brackets going outward:

| k | `[` index | `]` index | inner | evaluate(inner, k) |
| --- | --- | --- | --- | --- |
| 2 | 4 | 10 | aboml | abomlaboml |
| 4 | 1 | 10 | fabomlaboml | fabomlabomlfabomlabomlfabomlabomlfabomlaboml |