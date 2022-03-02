import copy


LIGHT_PIXEL, DARK_PIXEL = "#", "."

def enchance(image, algorithm, steps):
	line_padding = [DARK_PIXEL for _ in range(len(image[0]))]
	for i in range(steps * 2):
		image.insert(0, line_padding)
		image.append(line_padding)
	for i in range(len(image)):
		image[i] =  [DARK_PIXEL for i in range(steps * 2)] + image[i] + [DARK_PIXEL for i in range(steps * 2)]
	enchanced = []
	for i in range(steps):
		enchanced = copy.deepcopy(image)

		for i in range(1, len(image) - 1):
			for j in range(1, len(image[0]) - 1):
				enchanced[i][j] = convert_pixel(image, algorithm, i, j)

		image = enchanced

	return enchanced

	
def convert_pixel(image, algorithm, pixel_i, pixel_j):
	binary_num = ""
	for i in range(pixel_i - 1, pixel_i + 2):
		for j in range(pixel_j - 1, pixel_j + 2):
			to_add = "0" if image[i][j] == DARK_PIXEL else "1"
			binary_num += to_add

	index = int(binary_num, 2)

	return algorithm[index]


def main():
	with open("input.txt") as f:
		algorithm = f.readline().strip()
		f.readline()
		image = [[pixel for pixel in line.strip()] for line in f.readlines()]
		enchanced = enchance(image, algorithm, 2)
		enchanced = [line[2:-2] for line in enchanced[2:-2]]  # remove the border
		print(f"Part one: {sum([line.count(LIGHT_PIXEL) for line in enchanced])}")

		enchanced_part_two = enchance(image, algorithm, 50)
		enchanced_part_two = [line[50:-50] for line in enchanced_part_two[50:-50]]  # remove the border
		print(f"Part two: {sum([line.count(LIGHT_PIXEL) for line in enchanced_part_two])}")


if __name__ == "__main__":
	main()