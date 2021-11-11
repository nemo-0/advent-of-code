import re
import functools
import operator


reg = re.compile("(\\w+): capacity (-?\\d+), durability (-?\\d+), flavor (-?\\d+), texture (-?\\d+), calories (-?\\d+)")
ingredients = []

def parse(line):
	result = re.match(reg, line)

	if result:
		capacity = int(result.group(2))
		durability = int(result.group(3))
		flavor = int(result.group(4))
		texture = int(result.group(5))
		calories = int(result.group(6))

		ingredients.append([capacity, durability, flavor, texture, calories])


def get_scores(spoons=100, include_calories=False, max_calories=500):
	scores = []
	scores_part_two = []
	for frosting in range(0, spoons + 1):
		for candy in range(0, spoons + 1 - frosting):
			for butterscotch in range(0, spoons + 1 - frosting - candy):
				sugar = spoons - frosting - candy - butterscotch

				cookie_scores = [ingredients[0][i] * frosting + ingredients[1][i] * candy + ingredients[2][i] * butterscotch + ingredients[3][i] * sugar for i in range(5)]

				if min(cookie_scores) <= 0:
					continue

				total_score = functools.reduce(operator.mul, cookie_scores[:-1])
				scores.append(total_score)

				if cookie_scores[4] == max_calories:
					scores_part_two.append(total_score)

	if include_calories:
		return scores_part_two
	else:
		return scores


def main():
	with open("input.txt") as f:
		contents = f.readlines()

		for line in contents:
			parse(line.strip())
		
		print("Part one: ", max(get_scores()))
		print("Part two: ", max(get_scores(include_calories=True)))


if __name__ == "__main__":
	main()


