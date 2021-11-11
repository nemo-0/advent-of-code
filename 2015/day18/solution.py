

ON = "#"
OFF = "."

def animate(grid, broken=False):
	m = len(grid)
	n = len(grid[0])
	new_grid = [[OFF for i in range(n)] for j in range(m)]

	for i in range(m):
		for j in range(n):
			new_grid[i][j] = get_next_state(grid[i][j], get_turned_on_neighbours(grid, i, j))

	if broken:
		new_grid[0][0] = new_grid[0][n - 1] = new_grid[m - 1][0] = new_grid[m - 1][n - 1] = ON

	return new_grid


def get_next_state(light, turned_on):
	if light == ON:
		if turned_on in (2, 3):
			return ON
	else:
		if turned_on == 3:
			return ON

	return OFF


def is_valid(len_outer, len_inner, i, j):
	return 0 <= i < len_outer and 0 <= j < len_inner


def get_turned_on_neighbours(grid, i, j):
	m = len(grid)
	n = len(grid[0])

	turned_on = 0
	for checked_i, checked_j in [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (-1, -1), (1, -1), (1, 1)]:
		current_i, current_j = i + checked_i, j + checked_j
		if is_valid(m, n, current_i, current_j) and grid[current_i][current_j] == ON:
			turned_on += 1

	return turned_on


def main():
	with open("input.txt") as f:
		grid = [[c for c in line.strip()] for line in f.readlines()]

		for i in range(100):
			grid = animate(grid)

		print("Part one: ", sum(inner.count("#") for inner in grid))

		f.seek(0)

		grid = [[c for c in line.strip()] for line in f.readlines()]
		m = len(grid)
		n = len(grid[0])

		grid[0][0] = grid[0][n - 1] = grid[m - 1][0] = grid[m - 1][n - 1] = ON
		
		for i in range(100):
			grid = animate(grid, True)

		print("Part two: ", sum(inner.count("#") for inner in grid))


if __name__ == "__main__":
	main()