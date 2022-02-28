

NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3

def get_distance(instructions, part_two=False):
	directions = {NORTH: (0, 1), EAST: (1, 0), SOUTH: (0, -1), WEST: (-1, 0)}
	visited = [(0, 0)]
	facing = NORTH
	x, y = 0, 0
	for instruction in instructions:
		direction, blocks = instruction[0], int(instruction[1:])

		if direction == "R":
			facing = (facing + 1) % 4
		elif direction == "L":
			facing = (facing - 1) % 4

		for _ in range(blocks):
			x += directions[facing][0]
			y += directions[facing][1]

			if part_two and ((x, y) in visited):
				return abs(x) + abs(y)

			visited.append((x, y))

	return abs(x) + abs(y)


def main():
	with open("input.txt") as f:
		contents = f.readline().split(", ")

		print(f"Part one: {get_distance(contents)}")
		print(f"Part two: {get_distance(contents, part_two=True)}")


if __name__ == "__main__":
	main()