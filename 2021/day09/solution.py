import collections
import functools


def analyze(area):
	risk_and_basin = []
	for i in range(len(area)):
		for j in range(len(area[i])):
			curr_height = area[i][j]
			neighbours = {(i, j): curr_height}
			for coords in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
				curr_i, curr_j = i + coords[0], j + coords[1]
				if is_valid_index(len(area), len(area[i]), curr_i, curr_j):
					neighbours[(curr_i, curr_j)] = area[curr_i][curr_j]

			if len(set(neighbours.values())) == 1:
				continue
			if min(neighbours.values()) == curr_height:
				risk = curr_height + 1
				min_coords = (0, 0)
				for key, value in neighbours.items():
					if value == curr_height:
						min_coords = key
						break
				basin_size = get_basin_size(area, min_coords[0], min_coords[1])
				risk_and_basin.append((risk, basin_size))

	return risk_and_basin


def is_valid_index(i, j, curr_i, curr_j):
	return 0 <= curr_i < i and 0 <= curr_j < j


def get_basin_size(area, i, j):
	visited = set()
	size = 0
	queue = collections.deque([(i, j)])

	while queue:
		i, j = queue.pop()
		if (i, j) in visited:
			continue
		if not is_valid_index(len(area), len(area[0]), i, j):
			continue 
		if area[i][j] == 9:
			continue

		size += 1
		visited.add((i, j))
		for coords in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
			curr_i, curr_j = i + coords[0], j + coords[1]
			queue.extend([(curr_i, curr_j)])

	return size


def main():
	with open("input.txt") as f:
		contents = [[int(height) for height in line.strip()] for line in f.readlines()]
		risk_and_basin = analyze(contents)
		risk_sum = sum([pair[0] for pair in risk_and_basin])
		sizes_multiplied = functools.reduce(lambda x, y: x * y, 
			list(reversed(sorted([pair[1] for pair in risk_and_basin])))[:3])

		print(f"Part one: {risk_sum}")
		print(f"Part two: {sizes_multiplied}")


if __name__ == "__main__":
	main()