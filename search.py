
class Search:

	def rabin_karp(self, input_string, pattern):
		input_length = len(input_string)
		pattern_length = len(pattern)

		if (pattern_length == 0 or pattern_length > input_length):
			return []

		input_hash_window = 0
		pattern_hash = 0
		prime_number = 499
		number_of_chars = 26
		match_index_list = []
		highest_multiplier = number_of_chars ** (pattern_length - 1) % prime_number

		for i in range(pattern_length):
			input_hash_window = (input_hash_window * number_of_chars + ord(input_string[i])) % prime_number
			pattern_hash = (pattern_hash * number_of_chars + ord(pattern[i])) % prime_number

		for i in range(input_length - pattern_length + 1):
			if input_hash_window == pattern_hash:
				add = True
				for j in range(pattern_length):
					if input_string[i + j] != pattern[j]:
						add = False
				if add:
					match_index_list.append(i)

			if i < (input_length - pattern_length):
				input_hash_window = (input_hash_window - highest_multiplier * ord(input_string[i])) % prime_number
				input_hash_window = (input_hash_window * number_of_chars + ord(input_string[i + pattern_length])) % prime_number
				input_hash_window = (input_hash_window + prime_number) % prime_number

		return match_index_list