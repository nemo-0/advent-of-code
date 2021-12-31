import collections
import statistics


def get_score_corrupted(lines):
	score = 0
	pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
	points = {")": 3, "]": 57, "}": 1197, ">": 25137}
	for line in lines:
		characters = collections.deque()
		for character in line:
			if character in pairs.keys():
				characters.append(character)
			else:
				opening = characters.pop()
				if pairs[opening] != character:
					score += points[character]
					break

	return score


def get_score_incomplete(lines):
	scores = []
	pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
	points = {")": 1, "]": 2, "}": 3, ">": 4}
	for line in lines:
		is_corrupted = False
		line_score = 0
		characters = collections.deque()
		for character in line:
			if character in pairs.keys():
				characters.append(character)
			else:
				opening = characters.pop()
				if pairs[opening] != character:
					is_corrupted = True
					break
		if not is_corrupted:
			while len(characters) > 0:
				opening = characters.pop()
				closing = pairs[opening]
				line_score = line_score * 5 + points[closing]
			scores.append(line_score)			

	return statistics.median(scores)


def main():
	with open("input.txt") as f:
		contents = [line.strip() for line in f.readlines()]
		print(f"Part one: {get_score_corrupted(contents)}")
		print(f"Part two: {get_score_incomplete(contents)}")


if __name__ == "__main__":
	main()