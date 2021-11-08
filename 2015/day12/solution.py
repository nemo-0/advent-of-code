import re
import json


reg = re.compile("-?\\d+")

def get_sum(json_doc):
	matches = [int(match) for match in re.findall(reg, json_doc)]

	return sum(matches)


def skip_red(object_decoded):
	if "red" in object_decoded.values():
		return 0
	else:
		return object_decoded


def get_sum_without_red(json_doc):
	colors = str(json.loads(json_doc, object_hook=skip_red))
	
	return get_sum(colors)


def main():
	with open("input.txt") as f:
		contents = f.readline().strip()

	print("Part one: ", get_sum(contents))
	print("Part two: ", get_sum_without_red(contents))


if __name__ == "__main__":
	main()