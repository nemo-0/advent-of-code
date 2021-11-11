import itertools


def get_combinations(containers, liters=150, part_two=False):
	total = 0
	min_total = 0
	min_containers = len(containers)
	for i in range(len(containers) + 1):
		for sequence in itertools.combinations(containers, i):
			if sum(sequence) == liters:
				total += 1
				if i <= min_containers:
					min_containers = i
					min_total += 1

	if part_two:
		return min_total
	else:				
		return total


def main():
	with open("input.txt") as f:
		containers = [int(container) for container in f.readlines()]

		print("Part one: ", get_combinations(containers))
		print("Part two: ", get_combinations(containers, part_two=True))


if __name__ == "__main__":
	main()