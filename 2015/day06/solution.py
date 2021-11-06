import re


grid = [[0 for i in range(0, 1000)] for n in range(0, 1000)]
grid2 = [[0 for i in range(0, 1000)] for n in range(0, 1000)]

def turn_on(pair_from, pair_to, part_two=False):
	for i in range(pair_from[0], pair_to[0] + 1):
		for j in range(pair_from[1], pair_to[1] + 1):
			if part_two:
				grid2[i][j] += 1
			else:
				grid[i][j] = 1


def turn_off(pair_from, pair_to, part_two=False):
	for i in range(pair_from[0], pair_to[0] + 1):
		for j in range(pair_from[1], pair_to[1] + 1):
			if part_two:
				value = grid2[i][j] - 1
				grid2[i][j] = value if value > -1 else 0
			else:
				grid[i][j] = 0


def toggle(pair_from, pair_to, part_two=False):
	for i in range(pair_from[0], pair_to[0] + 1):
		for j in range(pair_from[1], pair_to[1] + 1):
			if part_two:
				grid2[i][j] += 2
			else:
				grid[i][j] = not grid[i][j]


def main():
	with open("input.txt") as f:
		contents = f.readlines()
		regex = re.compile("(turn on|turn off|toggle) (\\d+),(\\d+) through (\\d+),(\\d+)")
		for content in contents:
			line = re.match(regex, content)
			if line:
				command = line.group(1)
				start_x = int(line.group(2))
				start_y = int(line.group(3))
				end_x = int(line.group(4))
				end_y = int(line.group(5))

			if command == "turn on":
				turn_on((start_x, start_y), (end_x, end_y))
				turn_on((start_x, start_y), (end_x, end_y), True)
			elif command == "turn off":
				turn_off((start_x, start_y), (end_x, end_y))
				turn_off((start_x, start_y), (end_x, end_y), True)
			else:
				toggle((start_x, start_y), (end_x, end_y))
				toggle((start_x, start_y), (end_x, end_y), True)

	print("Part one: ", sum(nested.count(1) for nested in grid))
	print("Part two: ", sum(sum(nested) for nested in grid2))


if __name__ == "__main__":
	main()