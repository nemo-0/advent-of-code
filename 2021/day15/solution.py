import heapq
import copy


def find_lowest_risk(cave):
	visited = []
	not_visited = [[0, [0, 0]]]
	end_node = [len(cave) - 1, len(cave[0]) - 1]
	while not_visited:
		current_risk, node = heapq.heappop(not_visited)
	
		if node in visited:
			continue

		if node == end_node:
			return current_risk

		for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
			next_x, next_y = node[0] + x, node[1] + y
			if is_valid_index(next_x, next_y, cave):
				next_risk = current_risk + cave[next_x][next_y]
				heapq.heappush(not_visited, [next_risk, [next_x, next_y]])

		visited.append(node)
	return None


def is_valid_index(x, y, cave):
	return 0 <= x < len(cave) and 0 <= y < len(cave[0])


def main():
	with open("input.txt") as f:
		cave = [[(int(risk_level)) for risk_level in line.strip()] for line in f]
		lowest_risk = find_lowest_risk(cave)
		print(f"Part one: {lowest_risk}")

		extended_cave = copy.deepcopy(cave)
		max_x, max_y = len(cave), len(cave[0])
		for _ in range(1, 5):
			for i in range(len(cave)):
				new_data = [risk % 9 + 1 for risk in extended_cave[i][-max_y:]]
				extended_cave[i].extend(new_data)

		for _ in range(1, 5):
			for row in extended_cave[-max_x:]:
				new_data = [risk % 9 + 1 for risk in row]
				extended_cave.append(new_data)

		lowest_risk_part_two = find_lowest_risk(extended_cave)
		print(f"Part two: {lowest_risk_part_two}")


if __name__ == "__main__":
	main()