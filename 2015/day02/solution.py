

def get_paper_amount(dimensions):
	edges = dimensions.split('x')
	x = int(edges[0])
	y = int(edges[1])
	z = int(edges[2])

	smallest = min(x * y, y * z, z * x)
	paper_amount = 2 * (x * y + y * z + z * x) + smallest
	
	return paper_amount


def get_ribbon_amount(dimensions):
	edges = dimensions.split('x')
	edges_sorted = sorted([int(edges[0]), int(edges[1]), int(edges[2])])

	wrap = 2 * edges_sorted[0] + 2 * edges_sorted[1]
	bow = edges_sorted[0] * edges_sorted[1] * edges_sorted[2]

	return wrap + bow


def main():
	with open("input.txt") as f:
		contents = f.readlines()
		total_paper = 0
		total_ribbon = 0
		for dimension in contents:
			total_paper += get_paper_amount(dimension)
			total_ribbon += get_ribbon_amount(dimension)
		print("Part one: ", total_paper)
		print("Part two: ", total_ribbon)


if __name__ == "__main__":
	main()
