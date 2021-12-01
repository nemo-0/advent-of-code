

def get_increases(measurements):
	increases = 0 
	for i in range(1, len(measurements)):
		if measurements[i] > measurements[i - 1]:
			increases += 1

	return increases


def get_window_increases(measurements):
	increases = 0
	for i in range(len(measurements) - 3):
		first_window = sum(measurements[i:i+3])
		second_window = sum(measurements[i+1:i+4])
		
		if second_window > first_window:
			increases += 1

	return increases


def main():
	with open("input.txt") as f:
		contents = [int(n) for n in f.readlines()]

		print("Part one: ", get_increases(contents))
		print("Part two: ", get_window_increases(contents))


if __name__ == "__main__":
	main()