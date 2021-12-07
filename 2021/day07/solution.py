

def get_min_fuel(positions, func=None):
	if func:
		fuel_costs = [sum([func(abs(j - i)) for j in positions]) for i in range(max(positions))]
	else:
		fuel_costs = [sum([abs(j - i) for j in positions]) for i in range(max(positions))]

	return min(fuel_costs)


def main():
	with open("input.txt") as f:
		contents = [int(n) for n in f.readline().split(",")]

		print(f"Part one: {get_min_fuel(contents)}")
		print(f"Part two: {get_min_fuel(contents, lambda x: x * (x + 1) // 2)}")


if __name__ == "__main__":
	main()