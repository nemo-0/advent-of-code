import hashlib


def compute_hashes(key, prefix="00000"):
	hashcode = ""
	i = 0

	while not hashcode.startswith(prefix):
		i += 1
		value = f'{key}{i}'.encode("utf-8")
		hashcode = hashlib.md5(value).hexdigest()
	
	return i


def main():
	print("Part one: ", compute_hashes("ckczppom"))
	print("Part two: ", compute_hashes("ckczppom", "000000"))


if __name__ == "__main__":
	main()

