import itertools
import collections
import functools

def get_combinations(weights, groups):
	weight_sum = sum(weights) / groups
	return [seq for i in range(1, len(weights) + 1) for seq in itertools.combinations(weights, i) if sum(seq) == weight_sum]


def get_qe_of_ideal_config(combinations):
	lengths = collections.defaultdict(list)
	for c in combinations:
		lengths[len(c)].append(c)
	
	smallest_len = min(lengths.keys())
	smallest_count = len(lengths[smallest_len])

	qes = [compute_qe(c) for c in lengths[smallest_len]]
	return min(qes)


def compute_qe(group):
	return functools.reduce(lambda x, y: x * y, group)


def main():
	with open("input.txt") as f:
		contents = [int(n) for n in f.readlines()]
		
		print("Part one: ", get_qe_of_ideal_config(get_combinations(contents, 3)))
		print("Part two: ", get_qe_of_ideal_config(get_combinations(contents, 4)))

if __name__ == "__main__":
	main()