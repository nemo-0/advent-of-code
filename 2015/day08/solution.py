import re


reg = re.compile(r"\\x[0-9a-f]{2}")

def get_mem_len(text):
	new_text = text[1:-1] 
	chars = len(new_text)
	matches = re.findall(reg, new_text)

	chars -= len(matches) * 3
	chars -= new_text.count(r"\\")
	chars -= new_text.count('"')

	return chars


def get_encoded_len(text):
	chars = len(text)
	chars += text.count('"')
	chars += text.count("\\")
	chars += 2

	return chars


def main():
	with open("input.txt") as f:
		contents = f.readlines()

		total_code = 0
		total_mem = 0
		total_encoded = 0
		for line in contents:
			stripped = line.strip()
			total_code += len(stripped)
			total_mem += get_mem_len(stripped)
			total_encoded += get_encoded_len(stripped)

		print("Part one: ", total_code - total_mem)
		print("Part two: ", total_encoded - total_code)
		

if __name__ == "__main__":
	main()