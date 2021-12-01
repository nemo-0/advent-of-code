
def generate_code(previous_code):
	next_code = previous_code * 252533
	next_code %= 33554393

	return next_code


def get_code(target_row, target_column):
	current_row, current_column = (1, 1)
	diagonal_size = 1
	code = 20151125

	while (current_row, current_column) != (target_row, target_column):
		code = generate_code(code)

		if current_column == diagonal_size:
			current_column = 1
			diagonal_size += 1
			current_row = diagonal_size
		else:
			current_column += 1
			current_row -= 1

	return code


def main():
	target_row = 2947
	target_column = 3029

	print("Part one: ", get_code(target_row, target_column))


if __name__ == "__main__":
	main()