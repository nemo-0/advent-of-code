

def is_valid(incremented_pass):
	forbidden = ["i", "o", "l"]

	if any((c in forbidden) for c in incremented_pass):
		return False

	has_increasing_chars = False
	for i in range(len(incremented_pass) - 2):
		if ord(incremented_pass[i]) == (ord(incremented_pass[i + 1]) - 1) == (ord(incremented_pass[i + 2]) - 2):
			has_increasing_chars = True
			break

	used_chars = ""
	pairs = 0
	for i in range(len(incremented_pass) - 1):
		if incremented_pass[i] == incremented_pass[i + 1] and incremented_pass[i] not in used_chars:
			pairs += 1
			used_chars += incremented_pass[i]

	has_pairs = pairs >= 2

	return has_increasing_chars and has_pairs


def get_next_pass(password):	
	is_valid_pass = False

	while not is_valid_pass:
		reversed_pass = list(password)[::-1]
		i = 0
		for c in reversed_pass:
			if c == "z":
				reversed_pass[i] = "a"
			else:
				reversed_pass[i] = chr(ord(c) + 1)
				break
			i += 1
		
		password = "".join(reversed_pass[::-1])

		is_valid_pass = is_valid(password)
	
	return password


def main():
	puzzle_input = "hepxcrrq"

	password_part_one = get_next_pass(puzzle_input)
	print("Part one: ", password_part_one)

	password_part_two = get_next_pass(password_part_one)
	print("Part two: ", password_part_two)


if __name__ == "__main__":
	main()
