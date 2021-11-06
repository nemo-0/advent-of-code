import re


bad_sub = re.compile("ab|cd|pq|xy")
repeated_chars = re.compile("(.)\\1")
three_vowels = re.compile("([aeiou].*){3,}")
repeated_pair = re.compile("(..).*\\1")
repeated_with_gap = re.compile("(.).\\1")

def is_nice(text, new_rules=False):
	if new_rules:
		if not has_repeated_pair(text):
			return False
		if not has_repeated_with_gap(text):
			return False
	else:
		if has_bad_substrings(text):
			return False
		if not has_repeated_chars(text):
			return False
		if not has_three_vowels(text):
			return False

	return True


def has_bad_substrings(text):
	return re.search(bad_sub, text)


def has_repeated_chars(text):
	return re.search(repeated_chars, text)


def has_three_vowels(text):
	return re.search(three_vowels, text)


def has_repeated_pair(text):
	return re.search(repeated_pair, text)


def has_repeated_with_gap(text):
	return re.search(repeated_with_gap, text)


def main():
	with open("input.txt") as f:
		contents = f.readlines()

		counter = 0
		counter_new_rules = 0
		for s in contents: 
			if is_nice(s):
				counter += 1
			if is_nice(s, True):
				counter_new_rules += 1

		print("Part one: ", counter)
		print("Part two: ", counter_new_rules)


if __name__ == "__main__":
	main()
