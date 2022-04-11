import re

MARKER_REG = re.compile(r"\((\d+)x(\d+)\)")

def get_decompressed_len(text):
	start_search = 0

	while True:
		found = MARKER_REG.search(text, start_search)

		if found is None:
			break

		chars, times = int(found.group(1)), int(found.group(2))
		start, end = int(found.start()), int(found.end())
		text = text[:start] + text[end:end+chars] * times + text[end+chars:]

		start_search = start + chars * times

	return len(text)


def get_decompressed_len_v2(text):
	found = MARKER_REG.search(text)

	if found is None:
		return len(text)
	else:
		chars, times = int(found.group(1)), int(found.group(2))
		start, end = int(found.start()), int(found.end())

		return len(text[:start]) + get_decompressed_len_v2(text[end:end+chars]) * times + get_decompressed_len_v2(text[end+chars:])



def main():
	with open("input.txt") as f:
		contents = f.readline()

		print(f"Part one:  {get_decompressed_len(contents)}")
		print(f"Part two: {get_decompressed_len_v2(contents)}")


if __name__ == "__main__":
	main()