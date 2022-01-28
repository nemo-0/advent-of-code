import re


DOTS_REG = re.compile("(\\d+),(\\d+)")
FOLD_REG = re.compile("fold along (\\w+)=(\\d+)")
DOT, UNMARKED = "#", "."

def parse_input(file_contents):
	dots = []
	fold_instructions = []

	for line in file_contents:
		result_dots = re.match(DOTS_REG, line)
		result_fold = re.match(FOLD_REG, line)
		if result_dots:
			dots.append([int(result_dots[1]), int(result_dots[2])])
		elif result_fold:
			fold_instructions.append([result_fold[1], int(result_fold[2])])

	return dots, fold_instructions


def make_dots_map(dots):
	max_x = max([pair[0] for pair in dots])
	max_y = max([pair[1] for pair in dots])
	dots_map = [[UNMARKED for j in range(max_x + 1)] for i in range(max_y + 1)]

	for pair in dots:
		x, y = pair
		dots_map[y][x] = DOT

	return dots_map


def fold(dots_map, fold_instructions, n=1):
	fold_instructions = fold_instructions[:n]

	for instruction in fold_instructions:
		direction, value = instruction
		if direction == "y":
			up, down = dots_map[:value-1], dots_map[value:]
			for i in range(len(up)):
				for j in range(len(up[i])):
					up[i][j] = DOT if up[i][j] == DOT or down[-i-1][j] == DOT else UNMARKED
			dots_map = up
		elif direction == "x":
			left = [line[:value] for line in dots_map]
			right = [line[value:] for line in dots_map]
			for i in range(len(left)):
				for j in range(len(left[i])):
					left[i][j] = DOT if left[i][j] == DOT or right[i][-j-1] == DOT else UNMARKED
			dots_map = left

	return dots_map


def main():
	with open("input.txt") as f:
		dots, fold_instructions = parse_input(f)
		dots_map = make_dots_map(dots)

		dots_map_part_one = fold(dots_map, fold_instructions)
		dots_map_part_two = fold(dots_map, fold_instructions, len(fold_instructions))

		print(f"Part one: {sum(line.count(DOT) for line in dots_map_part_one)}")
		print("Part two:")
		for line in dots_map_part_two:
			print(*[x if x == DOT else " " for x in line])


if __name__ == "__main__":
	main()