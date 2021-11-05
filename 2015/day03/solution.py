

def get_unique_visits(directions, robo_santa=False):
	santa_visits = [(0, 0)]
	robo_santa_visits = [(0, 0)]

	visit_list = santa_visits
	for i, direction in enumerate(directions):
		if robo_santa:
			if i % 2 == 0:
				visit_list = santa_visits
			else:
				visit_list = robo_santa_visits

		if direction == "^":
			visit = (visit_list[-1][0], visit_list[-1][1] + 1)
		elif direction == "v":
			visit = (visit_list[-1][0], visit_list[-1][1] - 1)
		elif direction == ">":
			visit = (visit_list[-1][0] + 1, visit_list[-1][1])
		else:
			visit = (visit_list[-1][0] - 1, visit_list[-1][1])
		visit_list.append(visit)

	santa_visits.extend(robo_santa_visits)
	
	return len(set(santa_visits))
	

def main():
	with open("input.txt") as f:
		contents = f.read().strip()
		print("Part one: ", get_unique_visits(contents))
		print("Part two: ", get_unique_visits(contents, True))


if __name__ == "__main__":
	main()
