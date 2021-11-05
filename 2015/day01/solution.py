

def get_floor(instructions, part_two=False):
	floor = 0
	basement_position = 0
	for i, instruction in enumerate(instructions):
		if instruction == "(":
			floor += 1
		else:
			floor -= 1

		if part_two:
			if floor == -1:
				basement_position = i + 1
				return basement_position

	return floor


def main():
	with open("input.txt") as f:
		contents = f.read().strip()
		print(get_floor(contents))
		print(get_floor(contents, True))

if __name__ == "__main__":
	main()
