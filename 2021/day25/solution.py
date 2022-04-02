

EAST, SOUTH, EMPTY, MOVED = ">", "v", ".", True

def get_first_motionless_step(cucumbers):
	steps = 0

	while True:
		current_moves, cucumbers = move_cucumbers(cucumbers) 
		steps += 1

		if current_moves == 0:
			return steps


def move_cucumbers(cucumbers):
	moves = 0

	for i in range(len(cucumbers)):
		for j in range(len(cucumbers[0])):
			current_tile = cucumbers[i][j]
			if current_tile[1] == EAST and current_tile[0] != MOVED:
				next_tile = cucumbers[i][(j + 1) % len(cucumbers[0])]
				if next_tile[1] == EMPTY and next_tile[0] != MOVED:
					current_tile[0] = MOVED
					current_tile[1] = EMPTY
					next_tile[0] = MOVED
					next_tile[1] = EAST
					moves += 1

	cucumbers = [[[not MOVED, pos[1]] for pos in line] for line in cucumbers]

	for i in range(len(cucumbers[0])):
		for j in range(len(cucumbers)):
			current_tile = cucumbers[j][i]
			if current_tile[1] == SOUTH and current_tile[0] != MOVED:
				next_tile = cucumbers[(j + 1) % len(cucumbers)][i]
				if next_tile[1] == EMPTY and next_tile[0] != MOVED:
					current_tile[0] = MOVED
					current_tile[1] = EMPTY
					next_tile[0] = MOVED
					next_tile[1] = SOUTH
					moves += 1

	cucumbers = [[[not MOVED, pos[1]] for pos in line] for line in cucumbers]

	return moves, cucumbers


def main():
	with open("input.txt") as f:
		cucumbers = [[[not MOVED, pos] for pos in line.strip()] for line in f.readlines()]

		print(f"Part one: {get_first_motionless_step(cucumbers)}")


if __name__ == "__main__":
	main()