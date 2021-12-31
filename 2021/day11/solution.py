import collections


def count_flashes(grid, steps=100):
	total_flashes = 0
	for i in range(1, steps + 1):
		grid = increase_energy_levels(grid)
		grid, flashes = flash(grid)
		total_flashes += flashes

	return total_flashes


def find_synchronized_flash(grid):
	i = 0
	while True:
		grid = increase_energy_levels(grid)
		grid, _ = flash(grid)
		i += 1

		if is_synchronized_flash(grid):
			return i


def is_valid_index(i, j, curr_i, curr_j):
	return 0 <= curr_i < i and 0 <= curr_j < j


def increase_energy_levels(grid):
	grid = [[level + 1 for level in line] for line in grid]

	return grid


def flash(grid):
	flashes = 0
	flash_coords = [(i, j) for i in range(len(grid)) 
	for j in range(len(grid[0])) if grid[i][j] > 9]

	grid, curr_flashes = carry_flash_wave(grid, flash_coords)
	flashes += curr_flashes

	grid = [[0 if level > 9 else level for level in line] for line in grid]
	return grid, flashes


def carry_flash_wave(grid, flash_coords):
	flashes = 0
	neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
	visited = set()
	queue = collections.deque(flash_coords)

	while queue:
		i, j = queue.pop()
		if (i, j) in visited:
			continue
		if grid[i][j] > 9:
			flashes += 1
			visited.add((i, j))
			for coords in neighbours:
				curr_i, curr_j = i + coords[0], j + coords[1]
				if is_valid_index(len(grid), len(grid[i]), curr_i, curr_j):
					grid[curr_i][curr_j] += 1
					queue.extend([(curr_i, curr_j)])
	
	return grid, flashes


def is_synchronized_flash(grid):
	flat_grid = [level for line in grid for level in line]

	return flat_grid.count(0) == len(flat_grid)


def main():
	with open("input.txt") as f:
		contents = [[int(level) for level in line.strip()] for line in f]
		print(f"Part one: {count_flashes(contents)}")
		print(f"Part two: {find_synchronized_flash(contents)}")


if __name__ == "__main__":
	main()