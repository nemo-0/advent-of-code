import re
import itertools
import collections

reg = re.compile("(\\w+) would (\\w+) (\\d+) happiness units by sitting next to (\\w+).")
people = collections.defaultdict(dict)
arrangement_happiness = []

def parse_data(line):
	match = re.match(reg, line)
	if match:
		attendee = match.group(1)
		action = match.group(2)
		seated_next = match.group(4)

		happiness = ""
		if action == "gain":
			happiness = int(match.group(3))
		else:
			happiness = -int(match.group(3))

		people[attendee][seated_next] = happiness 
	

def get_arrangements():
	all_arrangements = itertools.permutations(people.keys())

	for arrangement in all_arrangements:
		total_happiness = 0
		for i in range(len(arrangement) - 1):
			total_happiness += people[arrangement[i]][arrangement[i + 1]]
			total_happiness += people[arrangement[i + 1]][arrangement[i]]

		total_happiness += people[arrangement[-1]][arrangement[0]]
		total_happiness += people[arrangement[0]][arrangement[-1]]  
		arrangement_happiness.append(total_happiness)


def main():
	with open("input.txt") as f:
		contents = f.readlines()

		for line in contents:
			parse_data(line)

	get_arrangements()
	print("Part one: ", max(arrangement_happiness))

	for person in people:
		people[person]["Me"] = 0

	people["Me"] = {person: 0 for person in people.keys()}
	arrangement_happiness.clear()
	get_arrangements()
	print("Part two: ", max(arrangement_happiness))


if __name__ == "__main__":
	main()