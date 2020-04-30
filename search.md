### [class search.**Search**()](/search.py)

**rabin_karp**(*input_string*, *pattern*)

Apply Rabin-Karp's algorithm to an input string, given a pattern. Return an array of match index's in the input string.

[Implement strStr()](https://leetcode.com/problems/implement-strstr/)
```python
def strStr(haystack: str, needle: str):
	matches = Search().rabin_karp(haystack, needle)
	if (len(matches) == 0):
		print(-1)
		return -1
	else:
		print(matches[0])
		return matches[0]
```