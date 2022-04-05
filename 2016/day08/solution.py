

ON, OFF = "#", "."

def get_pixels(instructions):
	screen = [[OFF for _ in range(50)] for _ in range(6)]

	for instruction in instructions:
		if "rect" in instruction:
			splitted = instruction.replace("x", " ").split()
			wide, tall = int(splitted[1]), int(splitted[2])
			screen = rec(screen, wide, tall)
		else:
			splitted = instruction.replace("=", " ").split()
			i, n = int(splitted[3]), int(splitted[5])
			if "column" in instruction:
				screen = rotate_column(screen, i, n)
			else:
				screen = rotate_row(screen, i, n)

	return screen


def rec(screen, wide, tall):
	for i in range(tall):
		for j in range(wide):
			screen[i][j] = ON

	return screen


def rotate_column(screen, x, n):
	column = [screen[i][x] for i in range(len(screen))]
	column = column[-n:] + column[:-n]

	for i in range(len(screen)):
		screen[i][x] = column[i]

	return screen


def rotate_row(screen, y, n):
	screen[y] = screen[y][-n:] + screen[y][:-n]

	return screen


def main():
	with open("input.txt") as f:
		instructions = [line.strip() for line in f.readlines()]
		pixels = get_pixels(instructions)
		lit_pixels = sum([line.count(ON) for line in pixels])

		print(f"Part one: {lit_pixels}")
		print("Part two: ")
		for line in pixels:
			print(*[pixel if pixel == ON else " " for pixel in line])


if __name__ == "__main__":
	main()