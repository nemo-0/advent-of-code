import collections


def get_num_of_paths(connections, allow_two_visits=False):
	paths_to_check = collections.deque([False, ["start", cave_to]] for cave_to in connections["start"])
	valid_paths = 0

	while paths_to_check:
		visited_twice, path = paths_to_check.pop()
		current_cave = path[-1]

		for neighbour_cave in connections[current_cave]:
			if neighbour_cave == "start":
				continue
			visited_twice_this_path = visited_twice
			if neighbour_cave in path and neighbour_cave.islower():
				if allow_two_visits and not visited_twice:
					visited_twice_this_path = True
				else:
					continue

			new_path = path + [neighbour_cave]
			
			if neighbour_cave == "end":
				valid_paths += 1
				continue

			paths_to_check.append([visited_twice_this_path, new_path])

	return valid_paths


def main():
	with open("input.txt") as f:
		contents = [line.strip().split("-") for line in f.readlines()]
		caves_and_neighbours = collections.defaultdict(set)
		for pair in contents:
			cave_from, cave_to = pair
			caves_and_neighbours[cave_from].add(cave_to)
			caves_and_neighbours[cave_to].add(cave_from)
			
		print(f"Part one: {get_num_of_paths(caves_and_neighbours)}")
		print(f"Part two: {get_num_of_paths(caves_and_neighbours, True)}")


if __name__ == "__main__":
	main()