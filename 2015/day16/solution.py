import collections
import re


tape = {"children": 3, 
		"cats": 7, 
		"samoyeds": 2, 
		"pomeranians": 3, 
		"akitas": 0,
		"vizslas": 0,
		"goldfish": 5,
		"trees": 3,
		"cars": 2,
		"perfumes": 1}

aunts = collections.defaultdict(dict)
reg = re.compile("Sue (\\d+): (\\w+): (\\d+), (\\w+): (\\d+), (\\w+): (\\d+)")

def parse_data(line):
	result = re.match(reg, line)

	if result:
		aunt = result.group(1)

		aunts[aunt][result.group(2)] = int(result.group(3))
		aunts[aunt][result.group(4)] = int(result.group(5))
		aunts[aunt][result.group(6)] = int(result.group(7))


def find_aunt():
	for aunt in aunts.keys():
		if all(item in tape.items() for item in aunts[aunt].items()):
			return aunt

	return None


def is_real_aunt(aunt):
	for item in aunts[aunt].keys():
		if item in ("cats", "trees"):
			if aunts[aunt][item] <= tape[item]:
				return False
		elif item in ("pomeranians", "goldfish"):
			if aunts[aunt][item] >= tape[item]:
				return False
		elif aunts[aunt][item] != tape[item]:
			return False

	return True


def main():
	with open("input.txt") as f:
		contents = f.readlines()

		for line in contents:
			parse_data(line)

		print("Part one: ", find_aunt())

		for aunt in aunts.keys():
			if is_real_aunt(aunt):
				print("Part two: ", aunt)
		

if __name__ == "__main__":
	main()