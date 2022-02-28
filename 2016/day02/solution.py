

def get_code(instructions, part_two=False):
	coords = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
	
	if part_two:
		position = (-2, 0)
		keypad = {(0, 2): 1, (-1, 1): 2, (0, 1): 3, (1, 1): 4, (-2, 0): 5, (-1, 0): 6, (0, 0): 7, (1, 0): 8, (2, 0): 9,
		 (-1, -1): "A", (0, -1): "B", (1, -1): "C", (0, -2): "D"}
	else:
		position = (0, 0)
		keypad = {(-1, 1): 1, (0, 1): 2, (1, 1): 3, (-1, 0): 4, (0, 0): 5, (1, 0): 6, (-1, -1): 7, (0, -1): 8, (1, -1): 9}
	
	code = ""
	number = keypad[position]

	for instruction in instructions:
		for direction in instruction:
			try:
				x, y = position[0] + coords[direction][0], position[1] + coords[direction][1]
				number = keypad[(x, y)]
				position = (x, y)
			except KeyError:
				continue

		code += str(number)
	return code


def main():
	with open("input.txt") as f:
		instructions = [line.strip() for line in f.readlines()]

	print(f"Part one: {get_code(instructions)}")
	print(f"Part two: {get_code(instructions, part_two=True)}")


if __name__ == "__main__":
	main()