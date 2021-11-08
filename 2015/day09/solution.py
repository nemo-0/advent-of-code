import re
import itertools
import collections


reg = re.compile("(\\w+) to (\\w+) = (\\d+)")
locations_and_distances = collections.defaultdict(dict)
distances = []

def parse_data(line):
	result = re.match(reg, line)
	if result:
		location_from = result.group(1)
		location_to = result.group(2)
		distance = int(result.group(3))

		locations_and_distances[location_from][location_to] = distance
		locations_and_distances[location_to][location_from] = distance


def get_routes():
	all_routes = itertools.permutations(locations_and_distances.keys())
	
	for route in all_routes:
		total_distance = 0
		for i in range(len(route) - 1):
			total_distance += locations_and_distances[route[i]][route[i + 1]]
		distances.append(total_distance)


def main():
	with open("input.txt") as f:
		contents = f.readlines()
		for line in contents:
			parse_data(line)

	get_routes()
	print("Part one: ", min(distances))
	print("Part two: ", max(distances))
	

if __name__ == "__main__":
	main()