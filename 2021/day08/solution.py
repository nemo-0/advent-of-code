import collections


def count_digits(entries):
	segment_counts = [2, 4, 3, 7]
	digit_lens = [len(digit) for entry in entries for digit in entry]
	digit_count = [digit_lens.count(segments) for segments in segment_counts]

	return sum(digit_count)


def get_output_values(entries):
	all_values = []
	for entry in entries:
		patterns, digits = [set(value) for value in entry[0]], [set(value) for value in entry[1]]
		patterns_lens = collections.defaultdict(list)
		[patterns_lens[len(pattern)].append(pattern) for pattern in patterns]
		pattern_mapping = {1: patterns_lens[2][0], 4: patterns_lens[4][0], 7: patterns_lens[3][0], 8: patterns_lens[7][0]}
		
		for pattern in patterns_lens[5]:
			if len(pattern.intersection(pattern_mapping[1])) == 2:
				pattern_mapping[3] = pattern
			elif len(pattern.intersection(pattern_mapping[4])) == 3:
				pattern_mapping[5] = pattern
			else:
				pattern_mapping[2] = pattern

		for pattern in patterns_lens[6]:
			if len(pattern.intersection(pattern_mapping[4])) == 4:
				pattern_mapping[9] = pattern
			elif len(pattern.intersection(pattern_mapping[1])) == 2:
				pattern_mapping[0] = pattern
			else: 
				pattern_mapping[6] = pattern
		
		output_value = ""
		for digit in digits:
			for key, value in pattern_mapping.items():
				if value == digit:
					output_value += str(key)
					break

		all_values.append(int(output_value))
	return all_values


def main():
	with open("input.txt") as f:
		contents = [line.split("|") for line in f.readlines()]
		patterns = [entry[0].strip().split(" ") for entry in contents]
		digits = [entry[1].strip().split(" ") for entry in contents]
		
		print(f"Part one: {count_digits(digits)}")
		print(f"Part two: {sum(get_output_values(tuple(zip(patterns, digits))))}")



if __name__ == "__main__":
	main()