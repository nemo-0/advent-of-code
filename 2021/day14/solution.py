

def run_insertion_process(template, rules, steps):
	pairs = {pair: template.count(pair) for pair in rules.keys()}
	elements = dict()
	for _ in range(steps):
		for pair, pair_count in list(pairs.items()):
			if pair_count > 0:
				pairs[pair] -= pair_count
				element = rules[pair]
				first_new_pair = pair[0] + element
				second_new_pair = element + pair[1]
				pairs[first_new_pair] += pair_count
				pairs[second_new_pair] += pair_count
		
	for pair, pair_count in pairs.items():
	 	elements[pair[0]] = elements.get(pair[0], 0) + pair_count
	elements[template[-1]] += 1

	return elements


def main():
	with open("input.txt") as f:
		template = f.readline().strip()
		f.readline()
		rules = dict()
		for line in f.readlines():
			pair, element = line.strip().split(" -> ")
			rules[pair] = element

		elements = run_insertion_process(template, rules, 10)
		print(f"Part one: {max(elements.values()) - min(elements.values())}")

		elements = run_insertion_process(template, rules, 40)
		print(f"Part one: {max(elements.values()) - min(elements.values())}")


if __name__ == "__main__":
	main()