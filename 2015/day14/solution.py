import re


reg = re.compile("(\\w+) can fly (\\d+) km/s for (\\d+) seconds, but then must rest for (\\d+) seconds.")
reindeers = {}


def parse_data(line):
	match = re.match(reg, line)

	if match:
		reindeer = match.group(1)
		speed = int(match.group(2))
		fly_time = int(match.group(3))
		rest_time = int(match.group(4))

		reindeers[reindeer] = [speed, fly_time, rest_time]


def get_distance(seconds=2503):
	distances = {}
	for reindeer in reindeers.keys():
		speed, fly_time, rest_time = reindeers[reindeer]
		count = seconds // (fly_time + rest_time)
		remainder_seconds = seconds % (fly_time + rest_time)

		distance = 0
		if fly_time < remainder_seconds:
			count += 1
		else:
			distance += (speed * remainder_seconds)

		distance += (count * fly_time * speed)
		distances[reindeer] = distance

	return distances


def get_points(duration=2503):
	reindeer_scores = {reindeer: 0 for reindeer in reindeers.keys()}
	seconds = 1
	while seconds <= duration:
		current_scores = get_distance(seconds)
		max_score = max(current_scores.values())
		leading_reindeers = [r for r in current_scores.keys() if current_scores[r] == max_score]

		for r in leading_reindeers:
			reindeer_scores[r] += 1

		seconds += 1
		
	return reindeer_scores


def main():
	with open("input.txt") as f:
		contents = f.readlines()

		for line in contents:
			parse_data(line)
	
	print("Part one: ", max(get_distance().values()))
	print("Part two: ", max(get_points().values()))


if __name__ == "__main__":
	main()