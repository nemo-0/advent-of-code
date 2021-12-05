import re


REG_LINES = re.compile("(\\d+,\\d+) -> (\\d+,\\d+)")

def parse(puzzle_input):
	coords = []
	for line in puzzle_input:
		result = re.match(REG_LINES, line)
		if result:
			coords1, coords2 = result.group(1).split(","), result.group(2).split(",")
			coords1, coords2 = (int(coords1[0]), int(coords1[1])), (int(coords2[0]), int(coords2[1]))
			coords.append((coords1, coords2))

	return coords


def get_lines(puzzle_input, part_two=False):
	coords = parse(puzzle_input)
	columns = max([group[0] for line in coords for group in line])
	rows = max([group[1] for line in coords for group in line])

	diagram = [[0 for _ in range(columns + 1)] for _ in range(rows + 1)]

	for line in coords:
		x1, y1 = line[0][0], line[0][1]
		x2, y2 = line[1][0], line[1][1]

		if x1 == x2:
			i_from, i_to = min(y1, y2), max(y1, y2)
			for i in range(i_from, i_to + 1):
				diagram[i][x1] += 1
		elif y1 == y2:
			i_from, i_to = min(x1, x2), max(x1, x2)
			for i in range(i_from, i_to + 1):
				diagram[y1][i] += 1
		else:
			if part_two:
				column_step = 1 if x1 < x2 else -1
				row_step = 1 if y1 < y2 else -1
				
				for i, j in zip(range(y1, y2, row_step), range(x1, x2, column_step)):
					diagram[i][j] += 1
				diagram[y2][x2] += 1

	points = sum([1 for line in diagram for point in line if point > 1])
	return points


def main():
	with open("input.txt") as f:
		contents = f.readlines()

		print(f"Part one: {get_lines(contents)}")
		print(f"Part two: {get_lines(contents, True)}")


if __name__ == "__main__":
	main()