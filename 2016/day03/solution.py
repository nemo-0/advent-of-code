

def is_valid_triangle(a, b, c):
	return a + b > c and a + c > b and b + c > a


def count_valid_triangles(triangles):
	valid_triangles = 0
	for a, b, c in triangles:
		if is_valid_triangle(a, b, c):
			valid_triangles += 1

	return valid_triangles


def main():
	with open("input.txt") as f:
		triangles = [[int(side) for side in line.strip().split()] for line in f.readlines()]
		print(f"Part one: {count_valid_triangles(triangles)}")

		triangles_part_two = [triangle for i in range(0, len(triangles), 3) for triangle in zip(*triangles[i:i+3])]
		print(f"Part two: {count_valid_triangles(triangles_part_two)}")


if __name__ == "__main__":
	main()