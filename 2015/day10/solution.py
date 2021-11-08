import itertools


def get_look_and_say(sequence):
	groups = itertools.groupby(sequence)
	result = [(number, sum(1 for _ in group)) for number, group in groups]
	
	new_sequence = "".join("{}{}".format(count, number) for number, count in result)
	
	return new_sequence


def main():
	puzzle_input = "1113122113"

	for _ in range(40):
		puzzle_input = get_look_and_say(puzzle_input)
	print("Part one: ", len(puzzle_input))

	for _ in range(10):
		puzzle_input = get_look_and_say(puzzle_input)

	print("Part two: ", len(puzzle_input))
	
		
if __name__ == "__main__":
	main()